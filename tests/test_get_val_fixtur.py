from utils import dict
import pytest


@pytest.mark.parametrize('collect, key, default', [
    ({'2': 'collect', '5': 'tok', '7': 'test'}, '5', 'tok'),
    ({'2': 'collect', '5': 'hopp'}, '2', 'collect'),
    ({'2': 'collect', '5': 'tok', '7': 'test'}, '9', 'git')])
def test_dict(collect, key, default):
    assert dict.get_val(collect, key) == default
