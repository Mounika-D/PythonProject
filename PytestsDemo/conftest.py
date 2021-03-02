import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print(" i will be executed last")

@pytest.fixture()
def dataLoad():
    print("data is being created")
    return["Mounika", "Dommaraju", "abc@gmail.com"]

@pytest.fixture(params=[("chrome", "Mounika" , "abc" ), ("firefox", "Dommaraju" , "def") , ("IE","ghi")])
def crossBrowser(request):
    return request.param