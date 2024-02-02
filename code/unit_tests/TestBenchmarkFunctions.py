import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Individual import Individual
from BenchmarkFunctions import OneMax, LeadingOnes, JumpK

class TestBenchmarkFunctions(unittest.TestCase):
    def setUp(self):
        self.test = Individual(64)

    def test_OneMax_1(self):
        for i in range(1, 11):
            self.test.set(5*i)
        t = OneMax(self.test)
        self.assertEqual(t, 10)

    def test_OneMax_2(self):
        for i in range(1, 21):
            self.test.set(3*i)
        t = OneMax(self.test)
        self.assertEqual(t, 20)

    def test_LeadingOnes_1(self):
        for i in range(11):
            self.test.set(i)
        t = LeadingOnes(self.test)
        self.assertEqual(t, 11)

    def test_LeadingOnes_2(self):
        for i in range(64):
            self.test.set(i)
        self.test.reset(30)
        t = LeadingOnes(self.test)
        self.assertEqual(t, 30)

    def test_JumpK_1(self):
        for i in range(64):
            self.test.set(i)
        t = JumpK(self.test, 6)
        self.assertEqual(t, 70)  # k + 64

    def test_JumpK_2(self):
        for i in range(41):
            self.test.set(i)
        t = JumpK(self.test, 24)
        self.assertEqual(t, 23)  # returns n - OneMax(test)

if __name__ == '__main__':
    unittest.main()
