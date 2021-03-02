import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
count = 0
driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.implicitly_wait(5)  # applicable globally for every line
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("ap")
time.sleep(4)

driver.find_elements_by_xpath("//div[@class='products']/div")
buttons = driver.find_elements_by_css_selector("div[class='product-action'] button")  # css parent to child
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
total_amount = driver.find_element_by_css_selector(".totAmt").text
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
#driver.refresh()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo"))) #if we dont give this wait the browser will take automaticaly previous value (192) as it takes some time to apply code
discount_amount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discount_amount) < float(total_amount)


#sum of the values = total amount

values = driver.find_elements_by_xpath("//tr/td[5]/p")

for value in values:
    #print(value.text)
    count = count+int(value.text)
    #print(count)
    #print("....")
#print(count)
#print(total_amount)
assert int(count) == int(total_amount)





