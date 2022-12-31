from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPageClass


class CheckoutPageClass:

    def __init__(self, driver):
        self.driver = driver

    cardLocator = (By.CSS_SELECTOR, ".h-100")
    cardName = (By.CSS_SELECTOR, "div h4 a")
    cardButton = (By.CSS_SELECTOR, "div button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutButton2 = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getCardLocators(self):
        return self.driver.find_elements(*CheckoutPageClass.cardLocator)

    def getCardTitles(self,phone):
        return phone.find_element(*CheckoutPageClass.cardName)

    def getCardButton(self,phone):
        return phone.find_element(*CheckoutPageClass.cardButton)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPageClass.checkoutButton)

    def getCheckoutButton2(self):
        self.driver.find_element(*CheckoutPageClass.checkoutButton2).click()
        confirmpage = ConfirmPageClass(self.driver)
        return confirmpage
