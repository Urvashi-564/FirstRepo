from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"(//*[@name='name'])[1]").send_keys("Urvashi")
driver.find_element(By.NAME,'email').send_keys('urvashi@gmail.com')
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,'#inlineRadio1').click()
driver.find_element(By.XPATH,"(//*[@name='name'])[2]").clear()
driver.find_element(By.XPATH,"(//*[@name='name'])[2]").send_keys("hey")
driver.find_element(By.XPATH,"//*[@type='submit']").click()
submission_txt=driver.find_element(By.XPATH,"//*[@class='alert alert-success alert-dismissible']").text
print(submission_txt)
assert 'Success!' in submission_txt

driver.close()
