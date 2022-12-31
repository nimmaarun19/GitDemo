from selenium.webdriver.common.by import By

class ConfirmPageClass:

    def __init__(self, driver):
        self.driver = driver

    countryField = (By.ID, "country")
    countryName = (By.LINK_TEXT, "India")
    confirmCheckbox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    confirmButton = (By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
    successMsg = (By.CSS_SELECTOR, ".alert-success")

    def getCountryField(self):
        return self.driver.find_element(*ConfirmPageClass.countryField)

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPageClass.countryName)

    def getConfirmCheckbox(self):
        return self.driver.find_element(*ConfirmPageClass.confirmCheckbox)

    def getConfirmButton(self):
        return self.driver.find_element(*ConfirmPageClass.confirmButton)

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPageClass.successMsg)