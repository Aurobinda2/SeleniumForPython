from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.google.com/')
driver.maximize_window()

#Shows type of Image Link (Directs to another page/location)
driver.find_element_by_xpath("//*[@id='hplogo']/a/img").click()
print(driver.title)
time.sleep(5)

#Image Button (Submits)
driver.get('http://newtours.demoaut.com/')
driver.maximize_window()
signin_img=driver.find_element_by_name('login')
print(signin_img.get_attribute('type'))
print(signin_img.get_attribute('value'))
time.sleep(5)

#General Image (No functionality)
driver.get('https://www.seleniumhq.org/')
driver.maximize_window()
signin_img=driver.find_element_by_xpath("//*[@id='sidebar']/img")
print(signin_img.get_attribute('type'))
print(signin_img.get_attribute('value'))
time.sleep(5)

driver.quit()

