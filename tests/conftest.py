from source.shapes import Rectangle
import pytest


@pytest.fixture
def my_rect():
    return Rectangle(10, 20)


@pytest.fixture
def rect_as_square():
    return Rectangle(5, 5)