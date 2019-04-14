import unittest
#assertEqual
#assertNotEqual

class Assert_class(unittest.TestCase):

    #def test_assertEqual(self):
        #name=input("Enter your name:")
        #self.assertEqual(4,len(name),'You name should be 4 character length')
    def test_assertNotEqual(self):
        age=eval(input("Enter your age:"))
        self.assertNotEqual(27,age,'This is your marriage year ..Not hire you ')
if __name__ == "__main__":
    unittest.main()