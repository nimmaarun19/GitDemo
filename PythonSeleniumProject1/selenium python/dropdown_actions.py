import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(3)
driver.find_element(By.ID, "autosuggest").send_keys("in")
time.sleep(3)
items = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(items))

for item in items:
    if item.text == "India":
        item.click()
        break
time.sleep(2)
print("Selected country name is : " + driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"