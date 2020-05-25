
def setup_module(module):
     print("\n Print Setup Module")
def teardown_module(module):
     print("\n Print Teardown Module")

def setup_function(function):
    if function == test1:
        print("\n Setting up Test 1")
    elif function == test2:
        print("\n Setting up Test 2")
    else:
        print("\n Setting up Unknown Test")

def teardown_function(function):
    if function == test1:
        print("\n Teardown up Test 1")
    elif function == test2:
        print("\n Teardown up Test 2")
    else:
        print("\n Teardown up unknown Test")


def test1():
    print("Executing from Test1")
    assert True


def test2():
    print("Executing from Test2")
    assert True


def test_Randon():
    print("Executing from unknow test_Randon")
    assert True