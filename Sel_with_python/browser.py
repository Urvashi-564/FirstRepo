from selenium import  webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
title=driver.title
print(title)
assert title =='Selenium, API Testing, Software Testing & More QA Tutorials | Rahul Shetty Academy'
url=driver.current_url
assert url == 'https://rahulshettyacademy.com/'
driver.get("https://rahulshettyacademy.com/practice-project")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()