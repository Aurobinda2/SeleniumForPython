import unittest
from selenium import webdriver
class checking(unittest.TestCase):
    def test_facebook(self):
        driver=webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get('https://www.facebook.com/')
        driver.find_element_by_id('email').send_keys('aurobindr.nayak3@gmial.com')
        driver.find_element_by_id('pass').send_keys('babulcool')
        driver.find_element_by_xpath("//*[@id='loginbutton']").click()
        title=driver.title
        print(title)
        self.assertEqual("(3) Facebook",title,"Page title is no same ")


if __name__=='__main__':
    unittest.main()
