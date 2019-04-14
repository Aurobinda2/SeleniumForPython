from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='chromedriver.exe')

driver.maximize_window()
driver.get('https://fs9.formsite.com/dAPGzG/lcnwzmq9qe/index.html?1551029142046')

#is_selected() is used to check whether the radio button selected or not
status=driver.find_element_by_name('RESULT_RadioButton-16').is_selected()
#if slected then return True else return False
print(status)
#Below statement clisk the radio button with locator identified by name
driver.find_element_by_name('RESULT_RadioButton-16').click()

#check_boxs=driver.find_elements(By.NAME,'RESULT_CheckBox-15')
#for check in check_boxs:
    #print(check.text)

# work with check box
driver.find_element_by_id('RESULT_CheckBox-15_0').click()
driver.find_element_by_id('RESULT_CheckBox-15_3').click()
