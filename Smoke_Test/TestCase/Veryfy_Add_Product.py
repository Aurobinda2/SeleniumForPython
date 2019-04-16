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

    def test_Add_Product(self):
        self.driver.find_element_by_link_text('Categories/Products').click()
        self.driver.find_element_by_id('tdb2').click()
        Add_Product=self.driver.find_element_by_class_name("pageHeading")
        print(Add_Product.text)
        self.assertEqual('''New Product in "Top"''',Add_Product.text,'Add Product option not visible')
    driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/SeleniumForPython/Smoke_Test/Reports',
                                                           report_title='Add(Insert) Production Option in Admin Home Page '))



