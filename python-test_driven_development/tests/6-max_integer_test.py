#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    # Test avec une liste vide
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Le résultat devrait être None pour une liste vide")

    # Test avec une liste contenant un seul élément
    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5, "Le plus grand élément dans une liste de un élément devrait être cet élément")

    # Test avec une liste contenant plusieurs éléments positifs
    def test_multiple_elements_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5, "Le plus grand élément dans la liste devrait être 5")

    # Test avec une liste contenant des nombres négatifs
    def test_multiple_elements_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1, "Le plus grand élément dans la liste devrait être -1")

    # Test avec une liste contenant des éléments mixtes (négatifs et positifs)
    def test_mixed_elements(self):
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5, "Le plus grand élément dans la liste devrait être 5")

    # Test avec une liste contenant des éléments répétés
    def test_repeated_elements(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3, "Le plus grand élément dans la liste devrait être 3")

    # Test avec une liste contenant des éléments de types différents
    def test_invalid_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3.5])

    # Test avec une liste contenant des nombres flottants
    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5, "Le plus grand élément dans la liste devrait être 4.5")

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)
if __name__ == "__main__":
    unittest.main()
