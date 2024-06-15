
def test_area(my_rect):
    assert my_rect.area() == 10 * 20


def test_perimeter(my_rect):
    assert my_rect.perimeter() == (10 + 20) * 2


def test_equals_rect_and_rectAsSquare(my_rect, rect_as_square):
    assert my_rect != rect_as_square

