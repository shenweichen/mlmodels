from __future__ import absolute_import, division, print_function

import inspect
import sys
import os

import numpy as np
import  tensorflow as tf
from numpy.testing import assert_allclose
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.layers import Input, Masking
from tensorflow.python.keras.models import Model, load_model, save_model

from deepctr.inputs import SparseFeat, DenseFeat,VarLenSparseFeat
from deepctr.layers import  custom_objects

SAMPLE_SIZE=16

def gen_sequence(dim, max_len, sample_size):
    return np.array([np.random.randint(0, dim, max_len) for _ in range(sample_size)]), np.random.randint(1, max_len + 1, sample_size)


def get_test_data(sample_size=1000, sparse_feature_num=1, dense_feature_num=1, sequence_feature=('sum', 'mean', 'max'),
                  classification=True, include_length=False, hash_flag=False,prefix=''):


    feature_columns = []

    for i in range(sparse_feature_num):
        dim = np.random.randint(1, 10)
        feature_columns.append(SparseFeat(prefix+'sparse_feature_'+str(i), dim,hash_flag,tf.int32))
    for i in range(dense_feature_num):
        feature_columns.append(DenseFeat(prefix+'dense_feature_'+str(i), 1,tf.float32))
    for i, mode in enumerate(sequence_feature):
        dim = np.random.randint(1, 10)
        maxlen = np.random.randint(1, 10)
        feature_columns.append(
            VarLenSparseFeat(prefix+'sequence_' + str(i), dim, maxlen, mode))



    model_input = []
    sequence_input = []
    sequence_len_input = []
    for fc in feature_columns:
        if isinstance(fc,SparseFeat):
            model_input.append(np.random.randint(0, fc.dimension, sample_size))
        elif isinstance(fc,DenseFeat):
            model_input.append(np.random.random(sample_size))
        else:
            s_input, s_len_input = gen_sequence(
                fc.dimension, fc.maxlen, sample_size)
            sequence_input.append(s_input)
            sequence_len_input.append(s_len_input)



    if classification:
        y = np.random.randint(0, 2, sample_size)
    else:
        y = np.random.random(sample_size)

    x = model_input+ sequence_input
    if include_length:
        for i, mode in enumerate(sequence_feature):
            dim = np.random.randint(1, 10)
            maxlen = np.random.randint(1, 10)
            feature_columns.append(
                SparseFeat(prefix+'sequence_' + str(i)+'_seq_length', 1,embedding=False))

        x += sequence_len_input

    return x, y, feature_columns


def layer_test(layer_cls, kwargs={}, input_shape=None, input_dtype=None,

               input_data=None, expected_output=None,

               expected_output_dtype=None, fixed_batch_size=False, supports_masking=False):
    # generate input data

    if input_data is None:

        if not input_shape:
            raise AssertionError()

        if not input_dtype:

            input_dtype = K.floatx()

        input_data_shape = list(input_shape)

        for i, e in enumerate(input_data_shape):

            if e is None:

                input_data_shape[i] = np.random.randint(1, 4)
        input_mask = []
        if all(isinstance(e, tuple) for e in input_data_shape):
            input_data = []

            for e in input_data_shape:
                input_data.append(
                    (10 * np.random.random(e)).astype(input_dtype))
                if supports_masking:
                    a = np.full(e[:2], False)
                    a[:, :e[1]//2] = True
                    input_mask.append(a)

        else:

            input_data = (10 * np.random.random(input_data_shape))

            input_data = input_data.astype(input_dtype)
            if supports_masking:
                a = np.full(input_data_shape[:2], False)
                a[:, :input_data_shape[1]//2] = True

                print(a)
                print(a.shape)
                input_mask.append(a)

    else:

        if input_shape is None:

            input_shape = input_data.shape

        if input_dtype is None:

            input_dtype = input_data.dtype

    if expected_output_dtype is None:

        expected_output_dtype = input_dtype

    # instantiation

    layer = layer_cls(**kwargs)

    # test get_weights , set_weights at layer level

    weights = layer.get_weights()

    layer.set_weights(weights)

    try:
        expected_output_shape = layer.compute_output_shape(input_shape)
    except Exception:
        expected_output_shape = layer._compute_output_shape(input_shape)

    # test in functional API
    if isinstance(input_shape, list):
        if fixed_batch_size:

            x = [Input(batch_shape=e, dtype=input_dtype) for e in input_shape]
            if supports_masking:
                mask = [Input(batch_shape=e[0:2], dtype=bool)
                        for e in input_shape]

        else:

            x = [Input(shape=e[1:], dtype=input_dtype) for e in input_shape]
            if supports_masking:
                mask = [Input(shape=(e[1],), dtype=bool) for e in input_shape]

    else:
        if fixed_batch_size:

            x = Input(batch_shape=input_shape, dtype=input_dtype)
            if supports_masking:
                mask = Input(batch_shape=input_shape[0:2], dtype=bool)

        else:

            x = Input(shape=input_shape[1:], dtype=input_dtype)
            if supports_masking:
                mask = Input(shape=(input_shape[1],), dtype=bool)

    if supports_masking:

        y = layer(Masking()(x), mask=mask)
    else:
        y = layer(x)

    if not (K.dtype(y) == expected_output_dtype):
        raise AssertionError()

    # check with the functional API
    if supports_masking:
        model = Model([x, mask], y)

        actual_output = model.predict([input_data, input_mask[0]])
    else:
        model = Model(x, y)

        actual_output = model.predict(input_data)

    actual_output_shape = actual_output.shape
    for expected_dim, actual_dim in zip(expected_output_shape,

                                        actual_output_shape):

        if expected_dim is not None:

            if not (expected_dim == actual_dim):
                raise AssertionError("expected_shape",expected_output_shape,"actual_shape",actual_output_shape)

    if expected_output is not None:

        assert_allclose(actual_output, expected_output, rtol=1e-3)

    # test serialization, weight setting at model level

    model_config = model.get_config()

    recovered_model = model.__class__.from_config(model_config)

    if model.weights:

        weights = model.get_weights()

        recovered_model.set_weights(weights)

        _output = recovered_model.predict(input_data)

        assert_allclose(_output, actual_output, rtol=1e-3)

    # test training mode (e.g. useful when the layer has a

    # different behavior at training and testing time).

    if has_arg(layer.call, 'training'):

        model.compile('rmsprop', 'mse')

        model.train_on_batch(input_data, actual_output)

    # test instantiation from layer config

    layer_config = layer.get_config()

    layer_config['batch_input_shape'] = input_shape

    layer = layer.__class__.from_config(layer_config)

    # for further checks in the caller function

    return actual_output


def has_arg(fn, name, accept_all=False):
    """Checks if a callable accepts a given keyword argument.



    For Python 2, checks if there is an argument with the given name.



    For Python 3, checks if there is an argument with the given name, and

    also whether this argument can be called with a keyword (i.e. if it is

    not a positional-only argument).



    # Arguments

        fn: Callable to inspect.

        name: Check if `fn` can be called with `name` as a keyword argument.

        accept_all: What to return if there is no parameter called `name`

                    but the function accepts a `**kwargs` argument.



    # Returns

        bool, whether `fn` accepts a `name` keyword argument.

    """

    if sys.version_info < (3,):

        arg_spec = inspect.getargspec(fn)

        if accept_all and arg_spec.keywords is not None:

            return True

        return (name in arg_spec.args)

    elif sys.version_info < (3, 3):

        arg_spec = inspect.getfullargspec(fn)

        if accept_all and arg_spec.varkw is not None:

            return True

        return (name in arg_spec.args or

                name in arg_spec.kwonlyargs)

    else:

        signature = inspect.signature(fn)

        parameter = signature.parameters.get(name)

        if parameter is None:

            if accept_all:

                for param in signature.parameters.values():

                    if param.kind == inspect.Parameter.VAR_KEYWORD:

                        return True

            return False

        return (parameter.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD,

                                   inspect.Parameter.KEYWORD_ONLY))


def check_model(model, model_name, x, y,check_model_io=True):
    """
    compile model,train and evaluate it,then save/load weight and model file.
    :param model:
    :param model_name:
    :param x:
    :param y:
    :param check_model_io: test save/load model file or not
    :return:
    """

    model.compile('adam', 'binary_crossentropy',
                  metrics=['binary_crossentropy'])
    model.fit(x, y, batch_size=100, epochs=1, validation_split=0.5)

    print(model_name+" test train valid pass!")
    model.save_weights(model_name + '_weights.h5')
    model.load_weights(model_name + '_weights.h5')
    os.remove(model_name + '_weights.h5') 
    print(model_name+" test save load weight pass!")
    if check_model_io:
        save_model(model, model_name + '.h5')
        model = load_model(model_name + '.h5', custom_objects)
        os.remove(model_name + '.h5') 
        print(model_name + " test save load model pass!")

    print(model_name + " test pass!")
