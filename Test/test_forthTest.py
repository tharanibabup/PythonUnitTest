class TestClass:
    @classmethod
    def setup_class(cls):
        print("\n Setup TestClass !")

    @classmethod
    def teardown_class(cls):
        print("\n Teardown TestClass !")

    def setup_method(self, method):
        if method == self.test1:
            print("\n Setting up for test 1")
        elif method == self.test2:
            print("\n Setting up for test 2")
        else:
            print("\n Setting up for Unknown test")

    def teardown_method(self, method):
        if method == self.test1:
            print("\n Teardown for test 1")
        elif method == self.test2:
            print("\n Teardown for test 2")
        else:
            print("\n Teardown for unknow test")

    def test1(self):
        print("Executing from Test 1 function")
        assert True

    def test2(self):
        print("Executing from Test 2 function")
        assert True