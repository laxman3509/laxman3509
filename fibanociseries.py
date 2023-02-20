import sys
sys.path.append("D:\Programs\Afpp")
import fibanocci_series

import unittest
class Test_fib(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(fibanocci_series.fibanocciseries(5),[0,1,1,2,3])

if __name__=="__main__":
    unittest.main()
