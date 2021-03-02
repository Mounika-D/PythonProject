# Any pytest file should start with test_ or end with _test
#pytest method names should start with test(test_firstprogram)
#Any code should be wrapped in method only
# Method name should be meaningful
import pytest


#@pytest.mark.smoke
def test_firstprogram(setup):
    print("hello")
    print("hi")

@pytest.mark.xfail
def test_firstcreditcard():
    ex = "I am str test case"
    print(ex)
    print("2nd test")

