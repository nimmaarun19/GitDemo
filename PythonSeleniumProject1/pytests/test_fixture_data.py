import pytest

from pytests.Baseclass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestFixexample(BaseClass):

    def test_editprofile(self,dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[2])
        print(dataload[1])

#passing parameters to use in test and test will run for all three parameters (THRICE)
@pytest.mark.usefixtures()
def test_crossbrowsers(browserload):
    print("cross browser execution")

#passing multiple parametes by grouping them, so that test run all three times use diff data's
@pytest.mark.usefixtures()
def test_crossbrowsers2(browserload2):
    print("cross browser execution: " + browserload2[0]+ " " + browserload2[1])