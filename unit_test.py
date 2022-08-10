from tdd import Calc
import pytest
import unittest

class CalcTest(unittest.TestCase):
    calc_obj = Calc()

    def test_percentage(self): # unit test to test the percentage function of the Calc class
        self.assertEqual(self.calc_obj.percentage(20, 40), "50.0%") # PASS
        self.assertEqual(self.calc_obj.percentage(40, 110), "36.36363636363637%") # PASS
        self.assertEqual(self.calc_obj.percentage(16, 5012), "45.0%") # FAIL

    def test_multiply(self): # unit test which tests the multiply function of the Calc class
        self.assertEqual(self.calc_obj.multiply(23, 41), "50.0%") # PASS
        self.assertEqual(self.calc_obj.multiply(40, 110), "36.36363636363637%") # PASS
        self.assertEqual(self.calc_obj.multiply(16, 5012), "45.0%") # FAIL

    def tes_DoB(self):
        self.assertEqual(self.calc_obj.calc_DoB(3000, 100),2900)
        self.assertEqual(self.calc_obj.calc_DoB(2022, 5012), 3012)
        self.assertEqual(self.calc_obj.calc_DoB(2000, -1990), 3990) # technically a fail, date of birth can't be negative