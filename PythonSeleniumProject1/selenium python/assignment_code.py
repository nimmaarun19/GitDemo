import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("learning")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])
time.sleep(3)
emailid = driver.find_element(By.CSS_SELECTOR, "div p:nth-child(2) strong a").text
driver.switch_to.window(handles[0])
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(emailid)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.text_to_be_present_in_element_value((By.CSS_SELECTOR, "#signInBtn"),"Sign In"))
alert = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print("Text displayed after submit is: " +alert)

assert "Incorrect" in alert