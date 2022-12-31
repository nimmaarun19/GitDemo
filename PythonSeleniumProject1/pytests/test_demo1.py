#we need to run the below command from the directorty where its located - from CMD promt
#py.test -v -s
#py.test test_demo2.py -v -s (for running specific file name)
#py.test -k Creditcard -v -s (for running test containing specific test name)
#py.test -m smoke -v -s (for adding tags and running the test with tags like regression : e.g -  @pytest.mark.smoke)
#fixtures can be used to setup few before test and after test notations - conftest.py - a central repository
#use @pytest.mark.usefixtures("setup") above class to use them for all menthods in class
# to get report use : pytest --html=report.html
#py.test --browser chrome --html=report.html -s
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello World - This is my first pytest program")

@pytest.mark.xfail
def test_Creditcardtest():
    print("Hello World: This is mu second pytest program")

@pytest.mark.usefixtures()
def test_crossbrowsers(browserload):
    print("cross browser execution")

@pytest.mark.usefixtures()
def test_crossbrowsers2(browserload2):
    print("cross browser execution: " + browserload2[0]+ " " + browserload2[1])
