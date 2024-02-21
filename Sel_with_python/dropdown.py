from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# dropdown=Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
# dropdown.select_by_index(0)
# dropdown.select_by_visible_text("Female")
checkboxes=driver.find_elements(By.XPATH,"//*[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        print("iam in")
        checkbox.click()
        assert checkbox.is_selected()

radio_btns=driver.find_elements(By.XPATH,"//*[@type='radio']")
# for radio in radio_btns:
#     if radio.text.strip() == 'Radio2':
#         radio.click()
#         assert radio.is_selected()
radio_btns[2].click()

assert driver.find_element(By.ID,'displayed-text').is_displayed()
assert driver.find_element(By.ID,'hide-textbox').click()
assert not driver.find_element(By.ID,'displayed-text').is_displayed()