import pytest


@pytest.fixture(scope="class")
def setup():
    print("I am test set up")
    yield
    print("I am test tear down")


@pytest.fixture
def dataLoad():
    print("load data from conftest file")
    return ["urvashi", "sharma", "UN consulting"]


@pytest.fixture(params=[("hello", "chrome"), ("rahul", "firefox"), "IE"])
def crossbrowser(request):
    return request.param
