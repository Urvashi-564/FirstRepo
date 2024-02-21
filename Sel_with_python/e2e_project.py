from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.PARTIAL_LINK_TEXT,"Shop").click()
orig_devices=[]
phones=driver.find_elements(By.XPATH,"//*[@class='card-title']/a")
for phone in phones:
    orig_devices.append(phone.text)

for device in orig_devices:
    if device == 'Nokia Edge':
        driver.find_element(By.XPATH,"(//a[text()='Nokia Edge']//following::button)[1]").click()

driver.find_element(By.XPATH,"//*[contains(text(),'Checkout')]").click()
pricee=driver.find_element(By.XPATH,"//*[@class='text-right']/h3/strong").text
assert  pricee == '₹. 65000'
driver.find_element(By.XPATH,"//*[contains(text(),'Checkout')]").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

chk=driver.find_element(By.XPATH,"//*[@class='checkbox checkbox-primary']")
chk.click()

# assert chk.is_selected()
driver.find_element(By.XPATH,"//*[@class='btn btn-success btn-lg']").click()
success_txt=driver.find_element(By.XPATH,"//*[@class='alert alert-success alert-dismissible']").text
assert  'Thank you!' in  success_txt