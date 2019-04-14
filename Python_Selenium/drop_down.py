from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://fs9.formsite.com/dAPGzG/lcnwzmq9qe/index.html?1551029142046')
element=driver.find_element_by_id('RESULT_RadioButton-12')
dpd=Select(element)
#dpd.select_by_visible_text("Morning")

dpd.select_by_value("Radio-2")

#dpd.select_by_index('1')

options_drop=dpd.options

print("Total drop_don element :",len(options_drop))
print ("Drop_don elements are :")
for ele in options_drop:
    print(ele.text)

