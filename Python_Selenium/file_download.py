from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromeOptions=Options()
chromeOptions.add_experimental_option('prefs',{'download.default_directory':'E:\Auto_Download'})
driver=webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chromeOptions)
driver.maximize_window()
driver.get('http://demo.automationtesting.in/FileDownload.html')

#to download text field

driver.find_element_by_id('textbox').send_keys("I want to download text file")
driver.find_element_by_id('createTxt').click()
driver.find_element_by_id('link-to-download').click()


#to download  pdf  field

driver.find_element_by_id('pdfbox').send_keys("I want to download PDF file")
driver.find_element_by_id('createPdf').click()
driver.find_element_by_id('pdf-link-to-download').click()



