import pytest

@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hell", "Test failed as the Strings Do Not Match"

def test_secondCreditcard():
    a = 4
    b = 6
    assert a+2 == b, "addition did not match"


def test_fixturedemo(setup):
    print("I will execute steps in fixture method - SECOND")

