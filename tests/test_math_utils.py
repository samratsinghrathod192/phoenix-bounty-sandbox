"""
REGRESSION TESTS FOR MATH UTILITY
"""
import pytest
from math_utils import calculate_safe_ratio

def test_standard_division():
    assert calculate_safe_ratio(10, 2) == 5.0

def test_zero_division_guard():
    assert calculate_safe_ratio(10, 0) == 0.0
    assert calculate_safe_ratio(10, 0, default=99.0) == 99.0
