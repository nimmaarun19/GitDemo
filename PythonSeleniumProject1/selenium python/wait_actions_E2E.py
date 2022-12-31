import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\BrowserDrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# implicit wait globally for all elements during execution for max 2 secs
driver.implicitly_wait(2)

fruits = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:
    fruits.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

print(fruits)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

#explicit wait for the specific element
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print("Text is :" + driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").text == "Code applied ..!"

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum=0
for price in prices:
    sum = sum + int(price.text) #convert string to integer and add up the sum
    
print(sum)
totalamt = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalamt
discamt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert discamt < totalamt

finalfruits = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(2) p")
FF = []
for fruit in finalfruits:
    FF.append(fruit.text)

assert FF == fruits