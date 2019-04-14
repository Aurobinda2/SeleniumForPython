from selenium import webdriver
driver=webdriver.Chrome(executable_path='chromedriver')
driver.get('https://www.amazon.in/')

#get cookies
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#add_customise cookies
my_cookies={'name':'My_Cookies','value':'12345678'}
driver.add_cookie(my_cookies)
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#delete_cookies

driver.delete_cookie('My_Cookies')

#delete_all_cookies

driver.delete_all_cookies()
