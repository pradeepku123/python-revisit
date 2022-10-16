import pytest


@pytest.fixture(scope='module')
def conftest_exploration():
    """ Conf_test Where Where Define Scope of Fixtures """
    print('------------> This is Fixture Scope Exploration <--------------------')
