from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
name='urvi'
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
alert.accept()