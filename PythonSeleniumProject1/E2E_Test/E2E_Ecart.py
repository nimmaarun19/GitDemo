import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

phones_elements = driver.find_elements(By.CSS_SELECTOR, ".h-100")

#search for blackberry phone and click on it
for phone in phones_elements:
    prod = phone.find_element(By.CSS_SELECTOR, "div h4 a").text
    if prod == 'Blackberry':
        phone.find_element(By.CSS_SELECTOR, "div button").click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']").click()

success_msg = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
time.sleep(2)
driver.get_screenshot_as_file("Success.png")
assert "Success" in success_msg

driver.quit()