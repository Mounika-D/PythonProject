from selenium import webdriver

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.minimize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/courses")
driver.maximize_window()
driver.refresh()
driver.back()
driver.close()