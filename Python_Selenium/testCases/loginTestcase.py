import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append('E:/Python_Selenium')
from pageObject import loginPage
class test_Login(unittest.TestCase):
    url='https://opensource-demo.orangehrmlive.com/'
    driver=webdriver.Chrome(executable_path="E:/Python_Selenium/driver/chromedriver.exe")
    username='Admin'
    password='admin123'
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
    def test_set(self):
        l=loginPage.LoginTest(self.driver)
        l.set_UserName(self.username)
        l.set_Password(self.password)
        l.login_action()
        self.driver.implicitly_wait(5)
        print(self.driver.title)
        self.assertEqual('OrangeHRM',self.driver.title,'Title not matching')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/Python_Selenium/htmlReport'))




