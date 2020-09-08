import unittest

from multiply import *

class TestMultiply(unittest.TestCase):
    def test1(self):
        result = multiply(10,20,30)
        self.assertEqual(result, 6000)

    def test2(self):
    	result = multiply(10,20,30)
    	self.assertTrue(result == 5000)

    def test3(self):
    	result = multiply(10,20,30)
    	self.assertFalse(result == 5000)

    def test4(self):
    	result = multiply(10,20,30)
    	self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()


#https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual