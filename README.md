# Test Driven Development

### What is TDD?

Test Driven Development (TDD), is a software development process which relies on incremental individual software requirements to be turned into test cases before software is fully developed.

TDD runs in a *RED*, *GREEN*, *BLUE* cycle (think uncle bob's dev hats).

![TDD](https://user-images.githubusercontent.com/47668244/183911093-4fbdbb4d-4a82-43f1-a31f-ecb4087ee930.png)

- In the *RED* stage code is written which has yet to be tested.
- In the *GREEN* stage the code is tested, and iterated upon until it passes the (particular software requirement) test case.
- Finally in the *BLUE* stage the code is refactored. Edited wihout changing functionality or success case for the tests, so that it completes as few computation, carries out in as few lines as possible, and follows appropriate naming conventions (etc).

These three stages of the cycle are continued over and over throughout the development.

### Benefits
This allows for fewer bugs and errors arising. which in term means less time is being spent of fixing such bugs, compared to other programming methodologies. Produces overall a higher test coverage and therefore to a better quality of the final product.


## Pytest
An installable package used to run unit tests on pycharm. Once installed and code is implemented to actually test it, you can call it using:

easy to write small test, yet good for testing complex written code.

open source
run test in parallel
- install pytest `pip install -U pytest`
- run `python -n pytest -v`

Python code:
```Python Code
class Calc():

    def percentage(self, val1, val2):
        return str((val1 / val2) * 100) + "%"

    def divide(self, val1, val2):
        return val1 / val2

    def multiply(self, val1, val2):
        return val1 * val2

    def calc_DoB(self, year, age):
        return year - age

    def cm_m(self, cm):
        return cm/100
```

Pytests:
```commandline
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
```