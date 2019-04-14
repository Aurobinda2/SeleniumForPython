import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append('E:/Smoke_Test')
from PageObject import Initiate_Page
import unittest

class test_verify_eleme(unittest.TestCase):
    url = 'https://www.gcreddy.com/project1/admin'
    driver = webdriver.Chrome(executable_path='E:/Smoke_Test/Driver/chromedriver.exe')
    @classmethod
    def setUpClass(cls):
        p=Initiate_Page.Initaite(cls.driver)
        p.set_url(cls.url)

    def test_check_username(self):
         username=self.driver.find_element_by_xpath("//*[@id='contentText']/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td")
         self.assertEqual(True,username.is_displayed(),"Unable to find 'User Name' field in login page ")
    def test_check_password(self):
        password = self.driver.find_element_by_xpath("//*[@id='contentText']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td")
        self.assertEqual(True, password.is_displayed(), "Unable to find 'Password' field in login page")
    def test_check_login_button(self):
        login_button = self.driver.find_element_by_class_name('ui-button-text')
        self.assertEqual(True, login_button.is_displayed(), "Unable to find 'Login Button' in login page")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
veryfy_testelement=unittest.TestLoader().loadTestsFromTestCase(test_verify_eleme)
test_suit=unittest.TestSuite(veryfy_testelement)


runner=HtmlTestRunner.HTMLTestRunner(output='E:/SeleniumForPython/Smoke_Test/Reports')
runner.run(test_suit)
#if __name__=='__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/Smoke_Test/Reports'))


