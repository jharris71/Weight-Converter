import pytest
from project import calculate_grams,calculate_ounces,calculate_pounds 

def test_grams():
    assert calculate_grams(2) == 2000

def test_ounces():
    assert calculate_ounces(2) == 70.548

def test_pounds():
    assert calculate_pounds(2) == 4.40924


def test_zero():
    assert calculate_grams(0) == 0

def test_grams_decimal():
    assert calculate_grams(0.001) == 1

def test_grams_large():
    assert calculate_grams(100000) == 100000000

def test_zero_ounces():
    assert calculate_ounces(0) == 0

def test_ounces_decimal():
    assert calculate_ounces(0.001) == 0.035274

def test_ounces_large():
    assert calculate_ounces(100000) == 3527400

def test_zero_pounds():
    assert calculate_pounds(0) == 0

def test_pounds_decimal():
    assert calculate_pounds(0.001) == 0.00220462

def test_pounds_large():
    assert calculate_pounds(100000) == pytest.approx(220462)


