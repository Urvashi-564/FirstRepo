import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)
elemenst=driver.find_elements(By.CLASS_NAME,"ui-menu-item")
print(len(elemenst))
for ele in elemenst:
    country_name=ele.text
    if country_name == "India":
        ele.click()
        break

text=driver.find_element(By.ID,"autosuggest").get_attribute('value')
assert text == 'India'
print(text)