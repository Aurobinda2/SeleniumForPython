from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('http://demo.automationtesting.in/Windows.html')

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

#it return the current window ..By default parent window is return
handel1=driver.current_window_handle
print(handel1)
time.sleep(5)
handels=driver.window_handles

#It is used to switch from one windown to another by using window name
#Here handels[1] means second window name 
driver.switch_to_window(handels[1])
for window in handels:
    if window==driver.current_window_handle:
        driver.find_element_by_xpath("//*[@id='container']/header/div/div/div[2]/ul/li[4]/a").click()