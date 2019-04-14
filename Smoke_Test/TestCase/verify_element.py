import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append('E:/Smoke_Test')
from PageObject import Initiate_Page
import unittest

class test_verify_eleme(unittest.TestCase):
    url = 'https://www.gcreddy.com/project1/admin'
    driver = webdriver.Chrome(executable_path='E:/Smoke_Test/Driver/chromedriver.exe')
    def test_element(self):
        p=Initiate_Page.Initaite(self.driver)
        p.set_url(self.url)
        username=self.driver.find_element_by_xpath("//*[@id='contentText']/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td")
        password=self.driver.find_element_by_xpath("//*[@id='contentText']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td")
        self.assertEqual('True1',username.is_displayed())
        self.assertEqual(True, password.is_displayed())
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/Smoke_Test/Reports'))


