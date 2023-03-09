from simple_math import *
import pytest


@pytest.mark.parametrize('a, b, expected', [
    (0, 0, 0),
    (2, 2, 4),
    (1, 3, 4),
])
def test_add(a, b, expected):
    assert simple_add(a, b) == expected


@pytest.mark.parametrize('a, b, expected', [
    (1, 0, 1),
    (2, 2, 0),
    (1, 3, -2),
])
def test_sub(a, b, expected):
    assert simple_sub(a, b) == expected



@pytest.mark.parametrize('a, b, expected', [
    (1, 0, 0),
    (2, 2, 4),
    (2, 3, 6),
])
def test_mult(a, b, expected):
    assert simple_mult(a, b) == expected


@pytest.mark.parametrize('a, b, expected', [
    (1, 1, 1),
    (4, 2, 2),
    (12, 3, 4),
])
def test_div(a, b, expected):
    assert simple_div(a, b) == expected

@pytest.mark.parametrize('x, a0, a1, expected', [
    (1, 1, 1, 2),
    (4, 2, 2, 10),
    (2, 3, 4, 11),
])
def test_poly1(x, a0, a1, expected):
    assert poly_first(x,a0,a1) == expected

@pytest.mark.parametrize('x, a0, a1, a2, expected', [
    (1, 1, 1, 1, 3),
    (4, 2, 2, 10, 170),
    (2, 3, 4, 11, 55),
])
def test_poly2(x, a0, a1,a2, expected):
    assert poly_second(x,a0,a1,a2) == expected