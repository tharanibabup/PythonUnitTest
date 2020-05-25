import pytest

#@pytest.fixture()
@pytest.fixture(autouse=True)
def setup():
    print("\n ********** Fixture *****************")
    print("\n Setup - Fixture")



#def test_t1(setup):
#    print("Test 1 function is called")
#    assert True

def test_t1():
    print("Test 1 function is called")
    assert True

#@pytest.mark.usefixtures("setup")
def test_t2():
    print("Test 2 function is called")
    assert True