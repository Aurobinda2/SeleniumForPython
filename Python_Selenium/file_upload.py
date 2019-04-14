from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')
driver.switch_to_frame(0)
driver.find_element_by_id('RESULT_FileUpload-11').send_keys('E:\images.jpg')

