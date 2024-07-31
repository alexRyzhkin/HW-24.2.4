import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 5, 1) == 6

    def test_subtraction(self):
        assert self.calc.subtraction(self, 4, 1) == 3

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 5) == 10

    def test_division(self):
        assert self.calc.division(self, 8, 4) == 2