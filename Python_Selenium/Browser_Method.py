from selenium import webdriver
driver=webdriver.Chrome(executable_path='chromedriver.exe')
#1)get()//Open Google page
driver.get('https://www.google.com/')

#2)driver.title //To get the page title
print(driver.title)

#3)driver.current_url //to get page url
print(driver.current_url)

#4)driver.page_source //to get page source
#string1=driver.page_source
#print(string1)

#5)driver.current_window_handle //to get current window
curr_window=driver.current_window_handle
print(curr_window)

#6)driver.close() //to close only focused browser
driver.close()

#7)driver.quite() //close all brower
#driver.quite()

