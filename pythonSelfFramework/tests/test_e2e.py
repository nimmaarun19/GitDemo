import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPageClass
from pageObjects.ConfirmPage import ConfirmPageClass
from pageObjects.HomePage import HomePageClass
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class Test_E2E(BaseClass):

    def test_e2e(self):
        self.driver.implicitly_wait(5)

        log = self.getlogger()
        homepage = HomePageClass(self.driver)
        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        checkoutpage = homepage.goToShop()
        log.info("Clicked on Shop and proceeding")
        #checkoutpage = CheckoutPageClass(self.driver)
        #phones_elements = self.driver.find_elements(By.CSS_SELECTOR, ".h-100")
        phones_elements = checkoutpage.getCardLocators()
        log.info("Getting all Card Locators")
        # search for blackberry phone and click on it
        for phone in phones_elements:
            prod = checkoutpage.getCardTitles(phone).text
            print(prod)
            if prod == 'Blackberry':
                checkoutpage.getCardButton(phone).click()
        time.sleep(2)
        checkoutpage.getCheckoutButton().click()
        time.sleep(2)
        confirmpage = checkoutpage.getCheckoutButton2()

        #confirmpage = ConfirmPageClass(self.driver)
        confirmpage.getCountryField().send_keys("Ind")
        self.verifyLinkPresence("India") # implementation is copied to utilities BaseClass
        confirmpage.getCountryName().click()
        time.sleep(2)
        confirmpage.getConfirmCheckbox().click()
        confirmpage.getConfirmButton().click()
        success_msg = confirmpage.getSuccessMsg().text
        time.sleep(2)
        log.info("Got the success message and asserting")
        self.driver.get_screenshot_as_file("Success.png")
        assert "Success" in success_msg

