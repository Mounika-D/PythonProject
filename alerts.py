from selenium import webdriver

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_name("enter-name").send_keys("all")


'''
#this is for positive scenario to click on ok
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
assert "all" in alert.text
alert.accept() # ok button
'''


#this is for negative scenario
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss() #cancel button
