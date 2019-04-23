from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://fs9.formsite.com/dAPGzG/lcnwzmq9qe/index.html?1551029142046')
driver.maximize_window()
first_name=driver.find_element(By.ID,"RESULT_TextField-2")
#to check textfield displayed or not and enabled or not
if first_name.is_displayed() and first_name.is_enabled():
    first_name.send_keys('Aurobinda')
    #to get text field value
    print(first_name.get_attribute('value'))
    
