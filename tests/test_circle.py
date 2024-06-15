import math

import source.shapes as shapes
import pytest


class TestCircle:

    def setup_method(self, method):
        print(f"settings up: {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"teardown: {method}")

    def test_area(self):
        expected = math.pi * self.circle.radius ** 2
        actual = self.circle.area()
        assert expected == actual

    def test_perimeter(self):
        expected = math.pi * self.circle.radius * 2
        actual = self.circle.perimeter()
        assert expected == actual

