from selenium import webdriver

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.facebook.com/')
driver.save_screenshot('E:/fb.png')
driver.get_screenshot_as_file('E:/fb2.png')

driver.close()
