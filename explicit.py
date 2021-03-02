import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
#driver.implicitly_wait(5)  # applicable globally for every line
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("ap")
time.sleep(4)
list = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(list))
assert len(list) == 3

# buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")   #xpath parent to child
buttons = driver.find_elements_by_css_selector("div[class='product-action'] button")  # css parent to chil
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
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))


driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_css_selector(".promoBtn").click()
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
#print(driver.find_element_by_css_selector("span.promoInfo").text)
print(driver.find_element_by_css_selector("span.promoInfo").text)

driver.find_element_by_xpath("//button[text()='Place Order']").click()





