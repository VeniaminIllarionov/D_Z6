from utils import dict


def test_get():
    assert dict.get_val([2, 2, 3], 1, "git") == 2
    assert dict.get_val([], 0, "test") == "test"


