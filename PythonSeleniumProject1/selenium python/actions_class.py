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
#class which will allow us to do different actions:
action = ActionChains(driver)

action.scroll_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover"))
time.sleep(2)
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(3)
action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()



