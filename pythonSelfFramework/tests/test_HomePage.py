import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePageClass
from test_data.homePageData import HomePageDataClass
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):
    @pytest.mark.skip
    def test_formSubmission_dict(self,getData):

        homepage = HomePageClass(self.driver)
        homepage.getemail().send_keys(getData["email"])
        time.sleep(1)
        homepage.getpwd().send_keys(getData["pwd"])
        homepage.getsubmitBtn().click()
        time.sleep(1)
        self.selectOptionByText(homepage.getselectDropdown(), getData["gender"])
        message = homepage.getsuccessMsg().text.strip("×")
        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=[{"email":"nimmaarun@gmail.com", "pwd":"Password" , "gender":"Female"} ,
                            {"email":"ni@gmail.com", "pwd":"Pas" , "gender":"Male"}])
    def getData(self, request):
        return request.param

    def test_formSubmission_extrenal_data(self,extData):

        homepage = HomePageClass(self.driver)
        homepage.getemail().send_keys(extData["email"])
        time.sleep(1)
        homepage.getpwd().send_keys(extData["password"])
        homepage.getsubmitBtn().click()
        time.sleep(1)
        self.selectOptionByText(homepage.getselectDropdown(), extData["gender"])
        message = homepage.getsuccessMsg().text.strip("×")
        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params= HomePageDataClass.getTestData("testcase2"))
    def extData(self, request):
        return request.param