import pytest


def test_testCase_001():
    print("test_testCase_001")
    assert 3 == 3


@pytest.mark.slow
def test_testCase_002():
    print("test_testCase_002")
    assert 3 == 3
