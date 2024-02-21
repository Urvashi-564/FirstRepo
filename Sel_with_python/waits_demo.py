from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//*[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
driver.find_element(By.XPATH,"//*[@class='search-button']").click()
list_on_ui=driver.find_elements(By.XPATH,"//div[@class='product']/h4")
fruits=[]
for list_item in list_on_ui:
    item=list_item.text
    fruits.append(item)
print(f"list of fruits from UI {fruits}")
actual_list=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
assert actual_list == fruits

wait1=WebDriverWait(driver,10)
wait1.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='product']/div/button")))
elements=driver.find_elements(By.XPATH, "//div[@class='product']/div/button")

for i in range(3):
    elements[i].click()

driver.find_element(By.XPATH,"//*[@class='cart-icon']//img").click()
driver.find_element(By.XPATH,"(//*[text()='PROCEED TO CHECKOUT'])").click()
total_amt=driver.find_elements(By.XPATH, "//tbody//td[5]")
sum=0
for price in total_amt:
    amt=price.text
    sum=sum + int(amt)
print(f"total amount is {sum}")

actual_amt=driver.find_element(By.XPATH, "//*[@class='discountAmt']").text
int(actual_amt)
print(f"actual amount on UI {actual_amt}")
assert sum==actual_amt
driver.find_element(By.XPATH, "//*[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"(//*[text()='Apply'])").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
amt_after_dicount=float(driver.find_element(By.XPATH, "//*[@class='discountAmt']").text)
actual_amt_post_discount=float(actual_amt)-float((int(actual_amt)*0.1))

print(actual_amt_post_discount)
print(amt_after_dicount)
assert amt_after_dicount==actual_amt_post_discount
assert float(driver.find_element(By.XPATH, "//*[@class='totAmt']").text) > float(driver.find_element(By.XPATH, "//*[@class='discountAmt']").text)

driver.find_element(By.XPATH,"(//*[text()='Place Order'])").click()


