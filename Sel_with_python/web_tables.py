from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
drpdown=Select(driver.find_element(By.ID,"page-menu")).select_by_visible_text("10")
# driver.find_element(By.XPATH,"//*[@class='sort-icon sort-descending']").click()
item_list=driver.find_elements(By.XPATH,"//*[@class='table table-bordered']//tbody/tr/td[1]")
listt=[]
for item in item_list:
    veg_name=item.text
    listt.append(veg_name)
print(listt)
listt.sort()
print(listt)
driver.find_element(By.XPATH,"//*[@class='sort-icon sort-ascending']").click()
item_list_after_sortingUI=driver.find_elements(By.XPATH,"//*[@class='table table-bordered']//tbody/tr/td[1]")
listt2=[]
for item in item_list_after_sortingUI:
    veg_name=item.text
    listt2.append(veg_name)

print(f"items after sorting from ui {listt2}")
assert listt == listt2