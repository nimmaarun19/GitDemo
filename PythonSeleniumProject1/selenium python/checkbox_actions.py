
#https://rahulshettyacademy.com/AutomationPractice/

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        time.sleep(2)
        assert checkbox.is_selected()

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
time.sleep(2)
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
time.sleep(2)
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "name").send_keys("Arun Ramesha")
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
assert "Arun" in alert.text
alert.accept()