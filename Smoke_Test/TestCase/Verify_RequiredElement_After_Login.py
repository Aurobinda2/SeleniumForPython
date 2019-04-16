from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
sys.path.append('E:/SeleniumForPython/Smoke_Test')
from PageObject import Home_Page


class Verify_Element_After_Admin_Login(unittest.TestCase):
    driver = webdriver.Chrome(executable_path='E:/SeleniumForPython/Smoke_Test/Driver/chromedriver.exe')
    p=Home_Page.Home_Page(driver)
    username='admin'
    password='admin@123'

    @classmethod
    def setUpClass(cls):
        cls.driver.get('http://www.gcrit.com/build3/admin/')
        cls.driver.maximize_window()
        cls.p.send_username(cls.username)
        cls.p.send_password(cls.password)
        cls.p.click_login_button()

    def test_checking_catalog(self):
        catalog=self.driver.find_element_by_link_text('Catalog')
        self.assertEqual(True,catalog.is_displayed(),'Catalog option not visible after login to Admin page')
    def test_checking_Customers(self):
        Customers=self.driver.find_element_by_link_text('Customers')
        self.assertEqual(True,Customers.is_displayed(),'Customers option is not visible after login to admin page')
    def test_checking_Localization(self):
        Localization=self.driver.find_element_by_link_text('Localization')
        self.assertEqual(True,Localization.is_displayed(),'Localization option not visible after login to Admin page')
    def test_checking_Reports(self):
        Reports=self.driver.find_element_by_link_text('Reports')
        self.assertEqual(True,Reports.is_displayed(),'Reports option is not visible after login to admin page')

    driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/SeleniumForPython/Smoke_Test/Reports',
                                                           report_title='Verify Element After Login to Admin Page '))




