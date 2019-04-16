from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
sys.path.append('E:/SeleniumForPython/Smoke_Test')
from PageObject import Home_Page


class Verify_AddManufactureOption_in_AdminPage(unittest.TestCase):
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

    def test_Add_Manufacture(self):
        self.driver.find_element_by_link_text('Manufacturers').click()
        self.driver.find_element_by_id('tdb1').click()
        New_Manufacture_option=self.driver.find_element_by_class_name("infoBoxHeading")
        self.assertEqual('New Manufacturer',New_Manufacture_option.text,'Add Manufacture option not visible')
    driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/SeleniumForPython/Smoke_Test/Reports',
                                                           report_title='Add(Insert) Manufacture Option in Admin Home Page '))



