#!/usr/bin/env python

"""
Author: Kamil Niklasinski
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

import math
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, contains 3 legs definition and decimal
    places precision for calculation of area.
    """

    decimal_places = 2

    def __init__(self, base_leg, left_leg, right_leg):
        """
        Create the triangle by givn three legs of a triangle.
        """
        self.base_leg = base_leg
        self.left_leg = left_leg
        self.right_leg = right_leg

    def area(self):
        """
        Compute the area using the formula (base_leg * height)/2
        """
        return round(
            math.sqrt(
                self.perimeter()
                * (self.perimeter() - self.base_leg)
                * (self.perimeter() - self.left_leg)
                * (self.perimeter() - self.right_leg)
            ),
            self.decimal_places,
        )

    def perimeter(self):
        """
        Compute the perimeter using all three legs of the triangle.
        """
        return self.base_leg + self.left_leg + self.right_leg

    def valid_legs(self):
        """
        Validates if sum of left_leg and right_leg is less or equal base_leg of
        the triangle. If this condition is met, then given leg lenghts are not
        correct and shape is not triangle.
        """
        if (self.left_leg + self.right_leg) <= self.base_leg:
            return False
        return True
