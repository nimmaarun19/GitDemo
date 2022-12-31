import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Window handles
driver.find_element(By.CSS_SELECTOR, "#opentab").click()

handles  = driver.window_handles
driver.switch_to.window(handles[1])
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".register-btn").click()
driver.switch_to.window(handles[0])
time.sleep(3)
print(driver.find_element(By.TAG_NAME, "h1").text)
assert "Practice Page" == driver.find_element(By.TAG_NAME, "h1").text