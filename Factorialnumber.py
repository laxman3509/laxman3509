import sys
sys.path.append("D:\Programs\Afpp")

import Factorial_Number

import unittest


class Test_Fact(unittest.TestCase):
     def testcase_1(self):
         self.assertEqual(Factorial_Number.factorial(4),24)

if __name__=="__main__":
    unittest.main()
