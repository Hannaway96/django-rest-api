"""
Sample Tests
"""

from django.test import SimpleTestCase
from app.calculator import Calculator


class TestCalculator(SimpleTestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.calculator = Calculator()

    def test_add_positive(self):
        x, y = 2, 3
        answer = self.calculator.add(x, y)
        self.assertEqual(answer, 5)

    def test_add_negative(self):
        x, y = 2, 3
        answer = self.calculator.add(x, y)
        self.assertNotEqual(answer, 9)

    def test_subtract_positive(self):
        x, y = 5, 3
        answer = self.calculator.subtract(x, y)
        self.assertEqual(answer, 2)

    def test_subtract_negative(self):
        x, y = 5, 3
        answer = self.calculator.subtract(x, y)
        self.assertNotEqual(answer, 9)
