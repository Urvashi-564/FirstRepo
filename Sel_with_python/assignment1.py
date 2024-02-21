import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
wait=WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[text()='Free Access to InterviewQues/ResumeAssistance/Material']")))
driver.find_element(By.XPATH,"//*[text()='Free Access to InterviewQues/ResumeAssistance/Material']").click()
window_handle=driver.window_handles
driver.switch_to.window(window_handle[1])
mail_text=driver.find_element(By.XPATH,"//*[contains(@href,'mailto:mentor@rahulshettyacademy.com')]").text
driver.switch_to.window(window_handle[0])
driver.find_element(By.ID,"username").send_keys(mail_text)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"signInBtn").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='login-form']/div[1]")))
incorrect_cred_alert=driver.find_element(By.XPATH,"//*[@id='login-form']/div[1]").text
print(f"Incorrect credentials alert message {incorrect_cred_alert}")





