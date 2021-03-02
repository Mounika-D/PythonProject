from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='/Users/ipraveen/Desktop/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)
driver.find_element_by_link_text("Shop").click()
phones = driver.find_elements_by_css_selector("div[class='card-body'] h4")
for phone in phones:
    print(phone.text)
    if phone.text == "Blackberry":
        driver.find_element_by_css_selector("button[class*=btn]").click()
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
wait = WebDriverWait(driver,10)

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions"))) # OR By.LINK_TEXT, "India"
driver.find_element_by_link_text("India").click()
'''
countries = driver.find_elements_by_css_selector("div[class='suggestions'] ul")
for country in countries:
    if country.text == "India":
        country.click()
'''

#driver.find_element_by_id("checkbox2").click()
#driver.find_element_by_xpath("//input[@id='checkbox2']").click() this line and above line are not working
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
success_text = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

assert "Success!" in success_text

driver.get_screenshot_as_file("screen.png")
