from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.w3schools.com/" )
print(driver.title)
print (driver.current_url)
driver.find_element_by_xpath("//*[@id='main']/div[1]/div[1]/a[2]").click()
print(driver.title)
print (driver.current_url)

