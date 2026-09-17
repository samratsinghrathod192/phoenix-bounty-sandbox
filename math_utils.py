"""
MATH UTILITY MODULE (SAFE RATIO COMPUTATION)
"""
def calculate_safe_ratio(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safely divides numerator by denominator with ZeroDivisionError guard."""
    if denominator == 0:
        return default
    return float(numerator) / float(denominator)
