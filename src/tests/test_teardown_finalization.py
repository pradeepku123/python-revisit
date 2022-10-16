import pytest


@pytest.fixture
def setup_teardown():
    """ This function are user to Setup The Test Envirnment & conclude  or teardown the Test """
    print('---------------> Setup <---------------')
    yield
    print('---------------> Teardown <---------------')


def test_tesardown_finalization(setup_teardown):
    """ This function for setup & teardown fixture """
    print('---------------> TEST Started <---------------')
