import unittest
from day6_7 import MyTeam
from day6_3 import Dog
from time import perf_counter


class TestTeam(unittest.TestCase):

    def setUp(self) -> None:
        self.m = MyTeam("Mike Waldberg", "Louise Mitchell")
        self.m.addDog(Dog("Charlie", 6))
        self.m.addDog(Dog("Marlie", 9))
        self.m.addDog(Dog("Marlie", 8))
        self.m.addDog(Dog("Keren", 3))
        self.n = MyTeam("Sarah Bernar", "Jessica Jhones")
        self.n.addDog(Dog("Roger", 6))
        self.n.addDog(Dog("Mike", 2))
        self.n.addDog(Dog("Cobo", 6))
        self.n.addDog(Dog("Taro", 2))

    def test_1(self):
        self.assertTrue(True)

    def test_2(self):
        self.m.removeDogFromTeam("Marlie")
        self.assertEqual(len(self.m.dogs), 2)

    def test_3(self):
        self.m.removeDogFromTeam("Marlie")
        testlist = [x for x in self.m.dogs if x.name == "Marlie"]
        self.assertEqual(len(testlist), 0)

    def test_4(self):
        self.m.mixTeam(self.n, 2)
        self.assertEqual(len(self.m.dogs), 6)

    def test_5(self):
        start_time = perf_counter()
        self.m.removeDogFromTeam("Marlie")
        end_time = perf_counter()
        dif = end_time - start_time
        self.assertTrue(dif < 0.0002)


unittest.main(exit=False)
