from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
sys.path.append('E:/SeleniumForPython/Smoke_Test')


class test_Launch_Application(unittest.TestCase):

   def test_Launch_Application(self):
       driver = webdriver.Chrome(executable_path='E:/SeleniumForPython/Smoke_Test/Driver/chromedriver.exe')
       driver.get('http://www.gcrit.com/build3/admin/')
       driver.maximize_window()
       self.assertEqual('GCR Shop Admin Panel',driver.title,'Not able to open the correct page ')
       driver.implicitly_wait(5)
       driver.quit()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/SeleniumForPython/Smoke_Test/Reports',report_title='Launch Application'))

