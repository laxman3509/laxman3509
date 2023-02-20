import sys
sys.path.append("D:\Programs\Afpp")
import Prime_Number

import unittest


class Test_prime(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Prime_Number.prime(5),"yes it is prime")
    #def testcase_2(self):
        #self.assertEqual(Prime_Number.prime(1),"neither prime nor composite")
    #def testcase_3(self):
        #self.assertEqual(Prime_Number.prime(-3),"negative numbers are not prime")

if __name__=="__main__":
    unittest.main()
