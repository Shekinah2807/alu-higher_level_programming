#!/usr/bin/python3
"""Defines unittests for models/square.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base_and_rectangle(self):
        self.assertIsInstance(Square(10), Base)
        self.assertIsInstance(Square(10), Rectangle)

    def test_args(self):
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertEqual(s2.id, s3.id - 1)
        self.assertEqual(4, s4.id)

    def test_invalid_types(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_invalid_values(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


class TestSquare_methods(unittest.TestCase):
    """Unittests for testing str, update, and to_dictionary of Square."""

    def test_str(self):
        s = Square(5, 1, 2, 4)
        self.assertEqual("[Square] (4) 1/2 - 5", str(s))

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))
        s.update(89, 1, 2, 3)
        self.assertEqual("[Square] (89) 2/3 - 1", str(s))

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual("[Square] (89) 2/3 - 1", str(s))

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 9)
        correct = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())


class TestSquare_save_and_load(unittest.TestCase):
    """Unittests for testing save_to_file and load_from_file of Square."""

    @classmethod
    def tearDown(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_one_square(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        Square.save_to_file([s1])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))


if __name__ == "__main__":
    unittest.main()
