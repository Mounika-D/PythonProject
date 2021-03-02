from selenium import webdriver
driver = webdriver.Chrome('/Users/ipraveen/Desktop/chromedriver')
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr") #method to switch frame. frames, iframes , frameset are the keyword to confirm it is a frame , id must be given for every frame
driver.find_element_by_css_selector("body[id='tinymce'] p").clear()
driver.find_element_by_css_selector("body[id='tinymce'] p").send_keys("I am able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_xpath("//h3[normalize-space()='An iFrame containing the TinyMCE WYSIWYG Editor']").text) #got rhis locator from selector hub using normalize space keyword
