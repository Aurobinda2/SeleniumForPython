#back() and forward() method

from selenium import webdriver
#from selenium.webdriver.common.keys impoprt Keys
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.w3schools.com")
print (driver.title)
time.sleep(5)
driver.get("https://www.facebook.com")
print (driver.title)
time.sleep(5)
driver.back()
print (driver.title)
time.sleep(5)
driver.forward()
print (driver.title)


