import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

frames = driver.find_element(By.CSS_SELECTOR, "#mce_0_ifr")
driver.switch_to.frame(frames)

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("This text entered is in frames")

print(driver.find_element(By.ID, "tinymce").text)

driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
