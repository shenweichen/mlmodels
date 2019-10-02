import pytest

from deepctr.models import WDL
from ..utils import check_model, SAMPLE_SIZE, get_test_data


@pytest.mark.parametrize(
    'sparse_feature_num,dense_feature_num',
    [(2, 0), (0, 2)#,(2, 2)
     ]
)
def test_WDL(sparse_feature_num, dense_feature_num):
    model_name = "WDL"
    sample_size = SAMPLE_SIZE
    x, y, feature_columns = get_test_data(
        sample_size, sparse_feature_num, dense_feature_num)

    model = WDL(feature_columns, feature_columns,
                dnn_hidden_units=[4, 4], dnn_dropout=0.5)
    check_model(model, model_name, x, y)


if __name__ == "__main__":
    pass
