import pytest
import source.my_functions as my_func


def test_add():
    expected = 5
    actual = my_func.add(1, 4)
    assert actual == expected


def test_add_strings():
    expected = "I love Python and C#"
    actual = my_func.add("I love Python ", "and C#")
    assert actual == expected


def test_divide():
    expected = 2
    actual = my_func.divide(10, 5)
    assert actual == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_func.divide(10, 0)

