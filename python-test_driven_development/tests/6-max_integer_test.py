#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for testing the max_integer function."""

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(
            max_integer([]),
            "Le résultat devrait être None pour une liste vide"
        )

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(
            max_integer([5]),
            5,
            """Le plus grand élément dans une liste de un élément
            devrait être cet élément"""
        )

    def test_multiple_elements_positive(self):
        """Test with a list of multiple positive elements."""
        self.assertEqual(
            max_integer([1, 2, 3, 4, 5]),
            5,
            "Le plus grand élément dans la liste devrait être 5"
        )

    def test_multiple_elements_negative(self):
        """Test with a list of multiple negative elements."""
        self.assertEqual(
            max_integer([-1, -2, -3, -4, -5]),
            -1,
            "Le plus grand élément dans la liste devrait être -1"
        )

    def test_mixed_elements(self):
        """Test with a list of mixed negative and positive elements."""
        self.assertEqual(
            max_integer([1, -2, 3, -4, 5]),
            5,
            "Le plus grand élément dans la liste devrait être 5"
        )

    def test_repeated_elements(self):
        """Test with a list of repeated elements."""
        self.assertEqual(
            max_integer([3, 3, 3, 3]),
            3,
            "Le plus grand élément dans la liste devrait être 3"
        )

    def test_invalid_elements(self):
        """Test with a list containing invalid element types."""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3.5])

    def test_floats(self):
        """Test with a list containing float numbers."""
        self.assertEqual(
            max_integer([1.5, 2.5, 3.5, 4.5]),
            4.5,
            "Le plus grand élément dans la liste devrait être 4.5"
        )

    def test_max_in_the_middle(self):
        """Test with the maximum element in the middle of the list."""
        self.assertEqual(
            max_integer([1, 5, 3]),
            5
        )


if __name__ == "__main__":
    unittest.main()
