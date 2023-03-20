from day7_1 import Meq
import unittest

class TestFromListSource(unittest.TestCase):
    
    def setUp(self) -> None:
        self.questions = [[1,1,1], [1,0,1], [0,1,1], [1,-2,1], [1,2,-8]]
        self.answers = [(0,0,-1), (0,0,-1), (-1), (1,1), (-4,2)]
        
    def test_from_lists(self):
        for i in range(0, len(self.questions)):
            with self.subTest():
                self.assertEqual(Meq(self.questions[i][0],self.questions[i][1],self.questions[i][2]), self.answers[i])


unittest.main(exit=False)
