#switch_to_alert().accept()
#switch_to_alert().dismis()

from selenium import webdriver
import time
driver=webdriver.Chrome('chromedriver.exe')
driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_confirm2')
driver.find_element_by_xpath('/html/body/button').click()

#switch_to_alert().accept() is used to accept the alert "ok" option
driver.switch_to_alert().accept()


#switch_to_alert().dismiss() is used to cancel the alert "Cancel " option
driver.switch_to_alert().dismiss()
