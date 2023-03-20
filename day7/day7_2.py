import unittest
from fortest import get_formatted_name


class NamesTestClass(unittest.TestCase):

    def test_first_last_1(self):
        testname = get_formatted_name("charlIe", "chAplin")
        self.assertEqual(testname, "Charlie Chaplin")

    def test_first_last_2(self):
        testname = get_formatted_name("charlIe1", "chAplin1")
        self.assertEqual(testname, "Charlie Chaplin")

    def test_first_last_3(self):
        testname = get_formatted_name("ch34arlIe1", "ch23()%%Aplin1")
        self.assertEqual(testname, "Charlie Chaplin")


unittest.main(exit=False)
