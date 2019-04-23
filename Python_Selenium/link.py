from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.google.com/')
driver.maximize_window()

gmail_link=driver.find_element_by_link_text('Gmail')
if gmail_link.is_displayed() and gmail_link.is_enabled():

    #to get the link text
    print(gmail_link.text)
    #to get the link url
    print(gmail_link.get_attribute('href'))
    #click on link 
    gmail_link.click()

time.sleep(5)
driver.quit()





