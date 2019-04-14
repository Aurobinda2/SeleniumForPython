from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')
action=ActionChains(driver)
button=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

action.double_click(button).perform()

time.sleep(5)

driver.quit()



