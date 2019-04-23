from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://fs9.formsite.com/dAPGzG/lcnwzmq9qe/index.html?1551029142046')
driver.maximize_window()

submit_button=driver.find_element(By.ID,"FSsubmit")
if submit_button.is_displayed() and submit_button.is_enabled():
    #get the value of Submit Button
    print(submit_button.get_attribute('type'))
    #get the type of submit button
    print(submit_button.get_attribute('value'))
    #click on submit button
    submit_button.click()
time.sleep(5)
driver.quit()