import pytest

@pytest.mark.parametrize('i',range(0,50))
def test_num(i):
    if i in (15,19):
        pytest.fail("Number should be between Failed")
