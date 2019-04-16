from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
sys.path.append('E:/SeleniumForPython/Smoke_Test')
from PageObject import Home_Page

class Verify_Admin_Login(unittest.TestCase):
    driver = webdriver.Chrome(executable_path='E:/SeleniumForPython/Smoke_Test/Driver/chromedriver.exe')
    p=Home_Page.Home_Page(driver)
    username='admin'
    password='admin@123'

    @classmethod
    def setUpClass(cls):
        cls.driver.get('http://www.gcrit.com/build3/admin/')
        cls.driver.maximize_window()

    def test_Admin_Login(self):
        self.p.send_username(self.username)
        self.p.send_password(self.password)
        self.p.click_login_button()
        self.assertEqual('GCR Shop',self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/SeleniumForPython/Smoke_Test/Reports',report_title='Verify Login On Admin Page'))

