import pytest

from source.shapes import Square


@pytest.mark.parametrize("side_len, expected_area", [(5, 25), (8, 64), (9, 81)])
def test_multiple_square_area(side_len, expected_area):
    assert Square(side_len).area() == expected_area

