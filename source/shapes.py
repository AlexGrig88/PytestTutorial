import math


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.length == other.length

    def __ne__(self, other):
        return not self.__eq__(other)

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2


class Square(Rectangle):
    def __init__(self, side_len):
        super().__init__(side_len, side_len)
        self.side_len = side_len

