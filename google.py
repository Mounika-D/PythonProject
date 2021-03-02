from selenium import webdriver
driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')

driver.get("https://www.google.com/")
driver.find_element_by_css_selector("input[title='Search']").send_keys("amazon")
driver.find_element_by_name("btnK")
driver.find_element_by_css_selector("div[class='yuRUbf'] a h3 span")
