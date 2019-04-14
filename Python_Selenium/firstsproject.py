from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
def chrome():
    driver=webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.facebook.com")
    print(driver.title)
    print(driver.current_url)
    #with open('fb.txt','w')as f:
    page_source=driver.page_source
    #f.write(page_source)
    time.sleep(7)
    driver.close()

def IE():
    driver=webdriver.Chrome(executable_path="chormedriver.exe")
    driver.get("https://www.facebook.com")
    print(driver.title)
    print(driver.current_url)
    page_source=driver.page_source
    time.sleep(7)
    driver.close()


def Firefox():
    driver = webdriver.Chrome("E:\Python_Selenium\chormedriver.exe")
    driver.get("https://www.facebook.com")
    print(driver.title)
    print(driver.current_url)
    page_source = driver.page_source

chrome()

