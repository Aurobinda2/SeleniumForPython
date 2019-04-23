from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://fs9.formsite.com/dAPGzG/lcnwzmq9qe/index.html?1551029142046')
driver.maximize_window()

standard_button=driver.find_element_by_xpath("//*[@id='q14']/table/tbody/tr/td[1]/label")
if standard_button.is_enabled() and not(standard_button.is_selected()):
    standard_button.click()
time.sleep(5)
driver.quit()