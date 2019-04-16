from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
sys.path.append('E:/SeleniumForPython/Smoke_Test')

class test_VeryfyElememt(unittest.TestCase):

    driver = webdriver.Chrome(executable_path='E:/SeleniumForPython/Smoke_Test/Driver/chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.driver.get('http://www.gcrit.com/build3/admin/')
        cls.driver.maximize_window()


    def test_Veryfy_Username(self):
       username=self.driver.find_element_by_xpath("//*[@id='contentText']/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td")
       self.assertEqual(True,username.is_displayed(),'Username field not visible')

    def test_Veryfy_Password(self):
        password =self.driver.find_element_by_xpath("//*[@id='contentText']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td")
        self.assertEqual(True,password.is_displayed(),'Password field not visible')

    def test_Veryfy_loginButton(self):
        login_Button=self.driver.find_element_by_class_name('ui-button-text')
        self.assertEqual(True,login_Button.is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.quit()
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/SeleniumForPython/Smoke_Test/Reports',report_title='Verify Element On Admin Page'))


