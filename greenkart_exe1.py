import time

from selenium import webdriver
list1=[]
list2=[]
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.implicitly_wait(5)  # applicable globally for every line
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(4)

driver.find_elements_by_xpath("//div[@class='products']/div")
buttons = driver.find_elements_by_css_selector("div[class='product-action'] button")  # css parent to child
for button in buttons:
    #print(button.find_element_by_xpath("parent::div/parent::div/h4").text) # traversing from child to grandparent and to uncle this is to optimize the code(19,20,21)
    button.click()


names1 = driver.find_elements_by_css_selector("div[class='product'] h4")
print(len(names1))
for name1 in names1:
    print(name1.text)
    list1.append(name1.text)
print(list1)

driver.find_element_by_css_selector("img[alt='Cart']").click()

driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()


#veggies =driver.find_elements_by_css_selector("p.product-name") #using css
veggies = driver.find_elements_by_xpath("//p[@class='product-name']") #using xpath
#Question : It(below 3 lines of code) is not working for normal for loop because length is showing as 6 instead of 3
'''
veggies =driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list2.append(veg.text)
'''
print(len(veggies))
for veg in range(3):
    print(veggies[veg].text)
    list2.append(veggies[veg].text)

print(list2)
assert list1 == list2


