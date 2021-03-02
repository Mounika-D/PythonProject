from selenium import webdriver

driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')

driver.get("https://login.salesforce.com/")


#css is the fastest finding locator

driver.find_element_by_css_selector("#username").send_keys("Mounika")  #css by id  #id
driver.find_element_by_css_selector(".password").send_keys("abcd@1234") #css by class substring   .class
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()  #find element by linktext(applicable for for links starting with 'a')
driver.find_element_by_xpath("//a[text()='Cancel']").click()  #finding xpath using text syn : //tagname[text()=’xxx’]

#print(driver.find_element_by_css_selector("div[class='inputgroup'] label").text)  #finding css using parent tag syn : ParentTag ChildTag
#print(driver.find_element_by_xpath("//div[@class='inputgroup']/label").text)   #finding css using parent tag syn : ParentTag/ChildTag
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)  #find xpath from grand parent to parent to child
#print(driver.find_element_by_css_selector("form[name='login'] div[1] label").text)  # not working because syntax in css is different (trainer explain later). if there are multiple index better go with xpath
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text) #css selector from parent to nth child(Que: can we do this with xpath?)



