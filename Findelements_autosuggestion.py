import time

from selenium import webdriver

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)
Countries = driver.find_elements_by_css_selector("li[class='ui-menu-item']")
print(len(Countries))
for Country in Countries:
    if Country.text == "India":
        Country.click()
        break
print(driver.find_element_by_id("autosuggest").text) #this method does not work in dynamic dropdown

print(driver.find_element_by_id("autosuggest").get_attribute('value')) #this method is for dynamic dropdown only to extract text in that particular field irrespective of reloading the page

