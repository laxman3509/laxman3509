import sys
sys.path.append("D:\Programs\Afpp")

import Pallindrome_Number

import unittest
class Test_pallin(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Pallindrome_Number.pallindrome(121),"the number is pallindrome")
    def testcase_2(self):
        self.assertEqual(Pallindrome_Number.pallindrome(-4),"negative numbers")
    def testcase_3(self):
        self.assertEqual(Pallindrome_Number.pallindrome(12),"the number is not pallindrome")

if __name__=="__main__":
    unittest.main()
