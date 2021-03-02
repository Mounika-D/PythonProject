from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
#for css and xpath it is irrespective of developer elements. we can create path with any attribute.
#driver.find_element_by_name("name").send_keys("Mounika")
driver.find_element_by_css_selector("input[name='name']").send_keys("Mounika")
#driver.find_element_by_class_name("ng-pristine").send_keys("Mounika") why this is not working(Trainer told class attribute is not unique)?

driver.find_element_by_name("email").send_keys("Dommaraju@gmail.com")

#driver.find_element_by_id("exampleInputPassword1").send_keys("abc@123")
driver.find_element_by_css_selector("#exampleInputPassword1").send_keys("abcd@123") #css selector using only #id

#driver.find_elements_by_class_name("form-check-input").click() not working
driver.find_element_by_id("exampleCheck1").click()


#Select class provide method to handle options in static drop down . tag name should be select

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")


driver.find_element_by_xpath("//input[@type='submit']").click()



#print(driver.find_element_by_class_name("alert-success").text)
#print(driver.find_element_by_css_selector("div[class*='alert-success']").text) tagname(div) is optional
#print(driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text) (syntax for full class name or full string)
#print(driver.find_element_by_xpath("//div[@class*='alert-success']").text) .  this is not working with substring(syntax is different for regx(substring)

#print(driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text) #this syntax is for regex or substring using xpath

#we can use assert instead of printing success message every time
message = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text

assert "success" in message

'''
"//tagname[@attribute='value']"
"tagname[attribute='value']"
'''