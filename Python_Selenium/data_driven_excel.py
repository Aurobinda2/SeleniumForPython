from selenium import webdriver
import pyxl
path='E:/data.xlsx'
driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('http://newtours.demoaut.com/')
row=pyxl.row_count(path,'Sheet1')
for r in range(2,row+1):
    user_name=pyxl.read_data(path,'Sheet1',r,1)
    print(user_name)
    password=pyxl.read_data(path,'Sheet1',r,2)
    print(password)
    driver.find_element_by_name('userName').send_keys(user_name)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('login').click()
    if driver.title=='Find a Flight: Mercury Tours:':
        pyxl.write_data(path, 'Sheet1', r,3,'Passed')
    else:
        pyxl.write_data(path, 'Sheet1', r, 3, 'Failed')
    driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a').click()
driver.quit()
