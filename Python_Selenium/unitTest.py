import unittest
from selenium import webdriver
class SearchEngineeTest(unittest.TestCase):
    def test(self):
        print('Test Case tasted fine....')

    def test_google_search(self):
        self.driver=webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.google.com/')
        print(self.driver.title)
        self.driver.close()

    def test_facebook_search(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.facebook.com')
        print(self.driver.title)
        self.driver.close()
if __name__== "__main__":
    unittest.main()
