from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')

button=driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

action=ActionChains(driver)
action.context_click(button).perform()


