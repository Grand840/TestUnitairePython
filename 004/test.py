from unittest import TestCase

from main import addition, divide

class TestCalculatrice(TestCase):
    def test_adding_two_numbers(self):
        self.assertEqual(addition(5, 10), 15)

    def test_adding_two_letters(self):
        self.assertEqual(addition("a", "b"), "ab")

    def test_adding_two_booleans(self):
        self.assertEqual(addition(True, False), 1)
        self.assertEqual(addition(True, True), 2)
        self.assertEqual(addition(False, False), 0)

    def test_adding_two_none(self):
        with self.assertRaises(TypeError):
            addition(None, None)

    def test_divide_with_two_numbers(self):
        self.assertEqual(divide(10, 5), 2)


