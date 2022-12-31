import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fix1(self):
        print("I am from method1")

    def test_fix2(self):
        print("I am from method2")

    def test_fix3(self):
        print("I am from method3")

    def test_fix4(self):
        print("I am from method4")