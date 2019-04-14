from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID,"tab-flight-tab-hp").click()
time.sleep(2)

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")

time.sleep(5)

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")
driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("02/28/2019")
driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("03/03/2019")
driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label").click()
time.sleep(10)

#Explicitly call here
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-0")))
element.click()

time.sleep(15)

driver.close()

