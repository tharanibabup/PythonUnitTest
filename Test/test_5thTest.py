import pytest

@pytest.fixture()
def setup1():
    print("\n Setup 1")
    yield
    print("\n Teardown 1")


@pytest.fixture()
def setup2(request):
    print("\n Setup 2")
    
    def teardown_a():
        print("\n Teardown A")
    def teardown_b():
        print("\n Teardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)



def test_t1(setup1):
    print("Test 1 function is called")
    assert True

def test_t2(setup2):
    print("Test 2 function is called")
    assert True