from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('E:\drag_drop.html')

action=ActionChains(driver)

source1=driver.find_element_by_xpath("//*[@id='drag1']")
desti=driver.find_element_by_xpath("//*[@id='div1']")

action.drag_and_drop(source1,desti).perform()

