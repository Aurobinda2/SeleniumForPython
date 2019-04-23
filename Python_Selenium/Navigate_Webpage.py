from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.w3schools.com')
print(driver.title)
#1)to maximize window
driver.maximize_window()
#2) Switch to another browser(google.com)
driver.get('https://www.google.com/')
print(driver.title)
#3)back to previous url (facebook.com)
driver.back()
print(driver.title)
time.sleep(5)
#4)forward to previous url (google.com)
driver.forward()
print(driver.title)
#5)refresh the browser
driver.refresh()


driver.quit()



