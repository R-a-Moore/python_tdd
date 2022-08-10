from tdd import Calc
import pytest
import unittest

class CalcTest(unittest.TestCase):
    calc_obj = Calc()

    def test_percentage(self):
        self.assertEqual(self.calc_obj.percentage(20, 40), "50.0%") # PASS
        self.assertEqual(self.calc_obj.percentage(40, 110), "36.36363636363637%") # PASS
        self.assertEqual(self.calc_obj.percentage(16, 5012), "45.0%") # FAIL
