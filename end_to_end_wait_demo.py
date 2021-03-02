import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.implicitly_wait(5)       #applicable globally for every line
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("ap")
time.sleep(4)
list = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(list))
assert len(list) == 3

#buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")   #xpath parent to child
buttons = driver.find_elements_by_css_selector("div[class='product-action'] button")   #css parent to child
for button in buttons:
    button.click()
    '''
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_css_selector("div[class='action-block'] button").click()
#driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

'''
driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()




driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_css_selector(".promoBtn").click()

print(driver.find_element_by_css_selector(".promoInfo").text)
driver.find_element_by_xpath("//button[text()='Place Order']").click()
dropdown = Select(driver.find_element_by_css_selector("div[class='wrapperTwo'] div select"))
dropdown.select_by_visible_text("India")
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//span[@class='errorAlert'] button")
//button[normalize-space()='Proceed']
