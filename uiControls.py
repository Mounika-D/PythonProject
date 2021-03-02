from selenium import webdriver

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))


for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()
radiobuttons = driver.find_elements_by_name("radioButton")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute('value') == "radio2":
        radiobutton.click()
#radiobuttons[2].click() we can use above 2 lines or this line to make it even more shorter (as radio buttob is clicked only once no need to iterate like check box)
        assert radiobuttons[1].is_selected()



#is displayed

#print(driver.find_element_by_id("displayed-text").is_displayed())
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
#print(driver.find_element_by_id("displayed-text").is_displayed())
assert not driver.find_element_by_id("displayed-text").is_displayed()