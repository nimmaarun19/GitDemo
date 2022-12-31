from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.CheckoutPage import CheckoutPageClass


class HomePageClass:

    def  __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    submitBtn = (By.CSS_SELECTOR, "input[type='submit']")
    dropdown = (By.ID, "exampleFormControlSelect1")
    successmsg = (By.CLASS_NAME, "alert-success")

    def goToShop(self):
        self.driver.find_element(*HomePageClass.shop).click()
        checkoutpage = CheckoutPageClass(self.driver)
        return checkoutpage

    def getemail(self):
        return self.driver.find_element(*HomePageClass.email)

    def getpwd(self):
        return self.driver.find_element(*HomePageClass.password)

    def getsubmitBtn(self):
        return self.driver.find_element(*HomePageClass.submitBtn)

    def getsuccessMsg(self):
        return self.driver.find_element(*HomePageClass.successmsg)

    def getselectDropdown(self):
        return self.driver.find_element(*HomePageClass.dropdown)
