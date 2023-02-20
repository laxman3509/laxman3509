import sys
sys.path.append("D:\Programs\Afpp")
import pallindrome_string
import unittest
class Test_pallin(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(pallindrome_string.pallindrome("racecar"),"it is pallindrome")
    def testcase_2(self):
        self.assertEqual(pallindrome_string.pallindrome("lagnar"),"it is not pallindrome")
    def testcase_3(self):
        self.assertEqual(pallindrome_string.pallindrome(""),0)

if __name__=="__main__":
    unittest.main()
