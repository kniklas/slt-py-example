"""
Author: Kamil Niklasiński
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase

from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.leg1leg1leg1 = Triangle(1, 1, 1)  # triangle with valid legs
        self.leg2leg1leg1 = Triangle(2, 1, 1)  # triangle with invalid legs

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.leg1leg1leg1.area(), 4.9)

    def test_valid_legs(self):
        """
        Verify if triangle legs length is correctly validated.
        """
        self.assertFalse(self.leg2leg1leg1.valid_legs())
        self.assertTrue(self.leg1leg1leg1.valid_legs())

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.leg1leg1leg1.perimeter(), 3)
