#switch_to_frame(name)
#switch_to_frame(id)
#switch_to_default_content()

from selenium import webdriver
import time

driver=webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')

#switch_to_frame('Name of the frame')
driver.switch_to_frame('packageListFrame')
driver.find_element_by_link_text('com.thoughtworks.selenium.webdriven').click()

time.sleep(5)
#switch to main page //Basically used when switch from one frame to other frame
driver.switch_to_default_content()

driver.switch_to_frame('packageFrame')
driver.find_element_by_link_text('FunctionDeclaration').click()

time.sleep(5)
driver.switch_to_default_content()

driver.switch_to_frame('classFrame')
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]/a').click()


