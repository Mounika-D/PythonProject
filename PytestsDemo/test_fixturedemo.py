import pytest


@pytest.mark.usefixtures("setup")
class Testexample:
    def test_fixtureDemo(self):
        print("i will execute steps in fixture demo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixture demo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixture demo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixture demo3 method")


#the below test case is irrespective of above fixture
#def test_firstprogram():
    #print("when i will print")