from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

#login using user details
driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()
time.sleep(5)

#find all three option on mouse hover
admin=driver.find_element_by_id('menu_admin_viewAdminModule')
usermgmt=driver.find_element_by_id('menu_admin_UserManagement')
user=driver.find_element_by_id('menu_admin_viewSystemUsers')

#Create a action chanin object by passing driver object
action=ActionChains(driver)

#It first move to first option on mouse hover then second then user then click on user
action.move_to_element(admin).move_to_element(usermgmt).move_to_element(user).click().perform()


