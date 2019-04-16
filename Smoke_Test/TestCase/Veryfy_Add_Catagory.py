from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
sys.path.append('E:/SeleniumForPython/Smoke_Test')
from PageObject import Home_Page


class Verify_AddCategory_In_Admin_Login(unittest.TestCase):
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

    def test_Add_Category(self):
        self.driver.find_element_by_link_text('Categories/Products').click()
        NewCategory=self.driver.find_element_by_id('tdb1').click()
        text=self.driver.find_element_by_class_name('infoBoxHeading').text
        self.assertEqual('New Category', text, 'Add Category option present in Admin Page')

    driver.implicitly_wait(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/SeleniumForPython/Smoke_Test/Reports',
                                                           report_title='NewCategory Option in Admin Home Page '))



