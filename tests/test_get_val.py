from utils import dict


def test_get():
    assert dict.get_val({'2' : 'collect', '5' : 'tok', '7' : 'test'}, '2') == 'collect'
    assert dict.get_val({'2' : 'collect', '5' : 'tok', '7' : 'test'}, '3', 'git') == 'git'
    assert dict.get_val({}, '3', 'git') == 'git'
