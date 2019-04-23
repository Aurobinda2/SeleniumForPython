from selenium import webdriver
driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('E:/practice/table.html')
driver.maximize_window()
cell_value=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[1]").text
row_count=driver.find_elements_by_tag_name("tr")
print(len(row_count))

cell_count=driver.find_elements_by_tag_name("td")
print(len(cell_count))


driver.quit()