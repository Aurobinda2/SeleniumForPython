from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('chromedriver.exe')
driver.get('https://www.makemytrip.com/flights/')

user_ele=driver.find_element_by_id('hp-widget__sfrom')
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pass_ele=driver.find_element_by_id('hp-widget__sTo')
print(user_ele.is_displayed())
print(user_ele.is_enabled())

select_ele=driver.find_element_by_id('switch__input_1')
print(select_ele.is_selected())

#driver.find_element_by_id('ch_login_icon').click()

driver.find_element_by_id('hp-widget__sfrom').clear()

user_ele.send_keys('DEL')
pass_ele.send_keys('BBI')

driver.find_element_by_id('searchBtn').click()




