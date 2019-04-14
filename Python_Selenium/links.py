from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://www.expedia.co.in/')
links=driver.find_elements(By.TAG_NAME,'a')
#for link in links:
    #print(link.text)
driver.find_element(By.LINK_TEXT,'Chennai Hotels').click()