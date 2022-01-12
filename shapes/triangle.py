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
    Represents a Triangle shape, and contains 3 legs definition.
    """

    decimal_places = 2

    def __init__(self, leg1, leg2, leg3):
        """
        Create the triangle by storing base and height.
        leg1: base leg
        leg2: left leg
        leg3: right leg
        """
        self.leg1 = leg1
        self.leg2 = leg2
        self.leg3 = leg3

    def area(self):
        """
        Compute the area using the formula (base * height)/2
        """
        return round(
            math.sqrt(
                self.perimeter()
                * (self.perimeter() - self.leg1)
                * (self.perimeter() - self.leg2)
                * (self.perimeter() - self.leg3)
            ),
            self.decimal_places,
        )

    def perimeter(self):
        """
        Compute the perimeter using all three legs of the triangle.
        """
        return round(self.leg1 + self.leg2 + self.leg3)

    def valid_legs(self):
        """
        Validates if sum of left and right leg is less or equal base leg of the
        triangle. If this condition is met, then given leg lenghts are not
        correct and shape is not triangle.
        """
        if (self.leg2 + self.leg3) <= self.leg1:
            return False
        return True
