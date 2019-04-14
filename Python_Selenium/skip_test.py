import unittest
import datetime
class Test_unitTest__skip_method(unittest.TestCase):
    #@unittest.SkipTest #Skip method using decorator
    def test_search(self):
        print('Normal search started and successfull ...')

    def test_advanced_search(self):
        print('Advanced search started and successfull ...')

    @unittest.skip("Prepaid not required ..Hence skip the method ") #skip the method with reason
    def test_Prepaid(self):
        print('Preapaid started and successfull ...')

    @unittest.skipIf(datetime.datetime.now().month!=2,'Month is not feb ..Hence skip the method ')
    def test_Post(self):
        print('PostPaid started and successfull ...')

    def test_loginbymain(self):
        print ('log in by gmail ')

    def test_loginbytwiter(self):
        print('login by twiter')

if __name__ == "__main__":
    unittest.main()
