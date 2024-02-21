from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//*[@class='form-group mt-2 mb-2']//input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("hello@123")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("hello@123")
driver.find_element(By.XPATH,"//*[text()='Save New Password']").click()