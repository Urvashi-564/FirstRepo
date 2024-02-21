from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.PARTIAL_LINK_TEXT,"Click Here").click()
win_handle=driver.window_handles
driver.switch_to.window(win_handle[1])
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h3")))
driver.close()
driver.switch_to.window(win_handle[0])
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h3")))
text1=driver.find_element(By.XPATH,"//h3").text
print(text1)
assert text1 == 'Opening a new window'


