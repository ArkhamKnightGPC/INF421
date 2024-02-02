import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Individual import Individual

class TestIndividual(unittest.TestCase):

    def test_flip_bit_in_first_block(self):
        test = Individual(5)
        test.flip(3)
        t = test.get(3)
        self.assertEqual(t, 1)

    def test_flip_bit_in_middle_block(self):
        test = Individual(50)
        test.flip(42)
        t1 = test.get(42)
        test.flip(42)
        t2 = test.get(42)
        self.assertEqual(t1, 1)
        self.assertEqual(t2, 0)

    def test_flip_bit_in_last_block(self):
        test = Individual(100)
        test.flip(90)
        t = test.get(90)
        self.assertEqual(t, 1)

    def test_set_and_reset_several_bits(self):
        test = Individual(120)
        test.set(3)
        test.set(41)
        test.set(94)
        test.set(100)
        test.set(111)
        test.reset(41)
        test.reset(100)

        t1 = test.get(3)
        t2 = test.get(41)
        t3 = test.get(94)
        t4 = test.get(100)
        t5 = test.get(111)
        self.assertEqual(t1, 1)
        self.assertEqual(t2, 0)
        self.assertEqual(t3, 1)
        self.assertEqual(t4, 0)
        self.assertEqual(t5, 1)

    def test_count_1(self):
        test = Individual(155)
        test.set(3)
        test.set(41)
        test.set(94)
        test.set(100)
        test.set(111)
        test.set(150)

        t = test.count()
        self.assertEqual(t, 6)

    def test_count_2(self):
        test = Individual(155)
        test.set(33)
        test.set(94)
        test.set(142)
        test.set(153)

        t = test.count()
        self.assertEqual(t, 4)

if __name__ == '__main__':
    unittest.main()
