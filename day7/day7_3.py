from day7_1 import Meq
import unittest


class EqTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Meq(0, 0, 1), (0, 0, -1))

    def test_2(self):
        self.assertEqual(Meq(0, 0, 0), (0, 0, 0))
        
    def test_3(self):
        self.assertEqual(Meq(1, 2, 1), (-1, -1))
    
    def test_4(self):
        self.assertEqual(Meq(1, -2, 1), (1, 1))
        
    def test_5(self):
        self.assertEqual(Meq(1, 3, 4), (0, 0, -1))
        
    def test_6(self):
        self.assertEqual(Meq(1, 2, -8), (-4, 2))
        


unittest.main(exit=False)
