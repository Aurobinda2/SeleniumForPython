import unittest
def setUpModule():
    print('Module Started ')
def tearDownModule():
    print('Module Ended')
class Test_unitTest_method(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Application started ")
    @classmethod
    def tearDownClass(cls):
        print('Application Closed ')
    @classmethod
    def setUp(cls):
        print('Log in to application...')
    @classmethod
    def tearDown(cls):
        print('Log out from the page ...')
    def test_search(self):
        print('Normal search started and successfull ...')

    def test_advanced_search(self):
        print('Advanced search started and successfull ...')

    def test_Prepaid(self):
        print('Preapaid started and successfull ...')

    def test_Post(self):
        print('PostPaid started and successfull ...')
if __name__ == "__main__":
    unittest.main()
