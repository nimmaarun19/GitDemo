
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.google.com")
print(driver.title)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
print(driver.current_url)
driver.back()
driver.refresh()
print(driver.current_url)
driver.forward()
print(driver.current_url)
driver.close()