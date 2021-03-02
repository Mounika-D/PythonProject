from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").get_attribute("value"))  #using selenium
print(driver.execute_script('return document.getElementsByName("name")[0].value')) #using jse dom in console

#driver.find_element_by_link_text("Shop").click() #using selenium

#use below java script method only selenium does not work
shopbutton = driver.find_element_by_link_text("Shop")
driver.execute_script("arguments[0].click();", shopbutton)

#scrolling : selinium does not have capabilty for scrolling feature

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #we can get scroll methods from google .
# 0,document.body.scrollHeight : this means starting to max height of the page
