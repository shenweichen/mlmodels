# -*- coding:utf-8 -*-
"""

Author:
    Weichen Shen,wcshen1994@163.com

Reference:
    [1] Xiao J, Ye H, He X, et al. Attentional factorization machines: Learning the weight of feature interactions via attention networks[J]. arXiv preprint arXiv:1708.04617, 2017.
    (https://arxiv.org/abs/1708.04617)

"""

from tensorflow.python.keras.layers import Concatenate, add
from tensorflow.python.keras.models import Model


from ..utils import get_linear_logit
from ..input_embedding import *
from ..layers import PredictionLayer, AFMLayer, FM


def AFM(feature_dim_dict, embedding_size=8, use_attention=True, attention_factor=8,
        l2_reg_linear=1e-5, l2_reg_embedding=1e-5, l2_reg_att=1e-5, keep_prob=1.0, init_std=0.0001, seed=1024,
        final_activation='sigmoid',):
    """Instantiates the Attentonal Factorization Machine architecture.

    :param feature_dim_dict: dict,to indicate sparse field and dense field like {'sparse':{'field_1':4,'field_2':3,'field_3':2},'dense':['field_4','field_5']}
    :param embedding_size: positive integer,sparse feature embedding_size
    :param use_attention: bool,whether use attention or not,if set to ``False``.it is the same as **standard Factorization Machine**
    :param attention_factor: positive integer,units in attention net
    :param l2_reg_linear: float. L2 regularizer strength applied to linear part
    :param l2_reg_embedding: float. L2 regularizer strength applied to embedding vector
    :param l2_reg_att: float. L2 regularizer strength applied to attention net
    :param keep_prob: float in (0,1]. keep_prob after attention net
    :param init_std: float,to use as the initialize std of embedding vector
    :param seed: integer ,to use as random seed.
    :param final_activation: str,output activation,usually ``'sigmoid'`` or ``'linear'``
    :return: A Keras model instance.
    """

    if not isinstance(feature_dim_dict,
                      dict) or "sparse" not in feature_dim_dict or "dense" not in feature_dim_dict:
        raise ValueError(
            "feature_dim_dict must be a dict like {'sparse':{'field_1':4,'field_2':3,'field_3':2},'dense':['field_4','field_5']}")
    if not isinstance(feature_dim_dict["sparse"], dict):
        raise ValueError("feature_dim_dict['sparse'] must be a dict,cur is", type(
            feature_dim_dict['sparse']))
    if not isinstance(feature_dim_dict["dense"], list):
        raise ValueError("feature_dim_dict['dense'] must be a list,cur is", type(
            feature_dim_dict['dense']))

    sparse_input_dict, dense_input_dict = create_input_dict(feature_dim_dict)
    sequence_input_dict, sequence_pooling_dict, sequence_input_len_dict, sequence_max_len_dict = create_sequence_input_dict(
        feature_dim_dict)

    deep_sparse_emb_dict = create_embedding_dict(
        feature_dim_dict, embedding_size, init_std, seed, l2_reg_embedding)
    linear_sparse_emb_dict = create_embedding_dict(
        feature_dim_dict, 1, init_std, seed, l2_reg_embedding, 'linear')

    deep_emb_list = get_embedding_vec_list(
        deep_sparse_emb_dict, sparse_input_dict)
    linear_emb_list = get_embedding_vec_list(
        linear_sparse_emb_dict, sparse_input_dict)

    deep_emb_list = merge_sequence_input(deep_sparse_emb_dict, deep_emb_list, sequence_input_dict,
                                         sequence_input_len_dict, sequence_max_len_dict, sequence_pooling_dict)
    linear_emb_list = merge_sequence_input(linear_sparse_emb_dict, linear_emb_list, sequence_input_dict, sequence_input_len_dict,
                                           sequence_max_len_dict, sequence_pooling_dict)

    deep_emb_list = merge_dense_input(
        dense_input_dict, deep_emb_list, embedding_size, l2_reg_embedding)
    linear_logit = get_linear_logit(
        linear_emb_list, dense_input_dict, l2_reg_linear)

    fm_input = Concatenate(axis=1)(deep_emb_list)
    if use_attention:
        fm_logit = AFMLayer(attention_factor, l2_reg_att,
                            keep_prob, seed)(deep_emb_list)
    else:
        fm_logit = FM()(fm_input)

    final_logit = add([linear_logit, fm_logit])
    output = PredictionLayer(final_activation)(final_logit)
    inputs_list = get_inputs_list(
        [sparse_input_dict, dense_input_dict, sequence_input_dict, sequence_input_len_dict])
    model = Model(inputs=inputs_list, outputs=output)
    return model
