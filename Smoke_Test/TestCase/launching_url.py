from selenium import webdriver
import HtmlTestRunner
from PageObject import Initiate_Page
import unittest
#from selenium.common.exceptions import TimeoutException

class test_launching_url(unittest.TestCase):
    url = 'https://www.gcreddy.com/project1/admin'
    driver = webdriver.Chrome(executable_path='E:/Smoke_Test/Driver/chromedriver.exe')
    def test_url(self):
        p=Initiate_Page.Initaite(self.driver)
        title=p.set_url(self.url)
        self.assertEqual('GCR Shop Admin Panel',title,'title not matched')

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/Smoke_Test/Reports'))


