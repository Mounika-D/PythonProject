from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
childmenu = driver.find_element_by_link_text("Top")
#action.move_to_element(childmenu).click().perform() trainer told this , below line is shortcut
action.click(childmenu).perform()


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver) #it should be there for each and every url


#action.move_to_element(driver.find_element_by_id("double-click")).double_click().perform() #we can use this as well for doubleclick
action.context_click(driver.find_element_by_id("double-click")).perform()

action.double_click(driver.find_element_by_id("double-click")).perform() #trainer told this
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#driver.find_element_by_name("confirmation").click()
#alert = driver.switch_to.alert
#print(alert.text)
#alert.dismiss()




