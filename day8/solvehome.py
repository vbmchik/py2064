from pif import Pythagoras
import unittest


class TestFromListSource(unittest.TestCase):

    def setUp(self) -> None:
        self.questions = [[3, 4, 5], [1, 0, 1],
                          [5, 13, 12], [8,17,15], [1, 2, 0]]
        
        self.answers = [True, True, True, True, False]

    def test_from_lists(self):
        for i in range(0, len(self.questions)):
            with self.subTest():
                self.assertEqual(Pythagoras(
                    self.questions[i][0], self.questions[i][1], self.questions[i][2]), self.answers[i])


unittest.main(exit=False)
