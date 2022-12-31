import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("nimmaarun@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Password")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(1)
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
message = driver.find_element(By.CLASS_NAME, "alert-success").text.strip("×")
print(message)
assert "Success" in message
