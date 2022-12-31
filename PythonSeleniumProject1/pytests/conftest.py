import pytest


@pytest.fixture(scope="class")
def setup():
    print("I am executing in fixture - FIRST")
    yield
    print("I am inside yeild and execute LAST")

@pytest.fixture()
def dataload():
    print("Data loading.....")
    return["Arun", "Ramesha", "nimmaarun@gmail.com"]

#passing parameters to use in test and test will run for all three parameters (THRICE)
@pytest.fixture(params=["chrome", "firefox", "edge"])
def browserload(request):
    return request.param

#passing multiple parametes by grouping them, so that test run all three times use diff data's
@pytest.fixture(params=[("chrome","Arun"), ("firefox", "Ramesha"), ("edge", "nimmaarun")])
def browserload2(request):
    return request.param