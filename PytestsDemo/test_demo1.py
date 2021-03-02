import pytest


#@pytest.mark.smoke
@pytest.mark.skip
def test_first():
    msg = "hello"
    assert msg == "hi", " strings does not match"

def test_demotestcase(setup):
    print("this is for demo purpose")



def test_secondreditcard():
    a = 4
    b = 6
    assert a+b == 10, "addition does not match"