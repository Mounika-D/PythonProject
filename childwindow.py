from selenium import webdriver
driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://the-internet.herokuapp.com/windows")
#driver.find_element_by_css_selector("div[class='example'] a").click()
driver.find_element_by_link_text("Click Here").click() #when tagname is 'a' we can go with link text attribute
driver.switch_to.window(driver.window_handles[1])    #method to switch to 1st child window
print(driver.find_element_by_tag_name("h3").text)  #we can use tag_name attribute if thee is unique tag name
driver.close()
driver.switch_to.window(driver.window_handles[0]) #method to switch to parent window
print(driver.find_element_by_css_selector("div[class='example'] h3").text)