import pytest
# Fixtures can request other fixtures [Competed]
# A test/fixture can request more than one fixture at a time [Completed]
#Set The Decorator for fixures 

# This is AutoUse fixture Its Call Every time While Test Case Executed
@pytest.fixture(autouse=True)
def auto_use_fixture_explore():
    ''' Auto-use fixture exploration'''
    print('Auto Use Called')


@pytest.fixture
def helper_fixture():
    ''' Fixture Function for testing'''
    print('function Data')
    return 'PASS-1'

@pytest.fixture
def reuse_existing_fixture_function(helper_fixture):
    ''' This Fixture Funtion i am goining to Reuse the existing fixture function'''
    print('reuse_existing_fixture_function')
    return helper_fixture+'Reuse'

@pytest.fixture
def multi_reuse_existing_fixture_function(helper_fixture, reuse_existing_fixture_function):
    ''' Reuse more than one Fixture Funtion'''
    print('multi_reuse_existing_fixture_function')
    return [helper_fixture,reuse_existing_fixture_function]

def test_test_fixture_001(multi_reuse_existing_fixture_function):
    '''Test fixture function for testing'''
    print('Test Fixture_1')
    print(multi_reuse_existing_fixture_function,sep=' ',end='END')
    
    
def test_test_fixture_002():
    print('Test Fixture_2')