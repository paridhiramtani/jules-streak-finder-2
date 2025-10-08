import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test with a list containing only non-positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_single_streak():
    """Test with a single streak of positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks_longest_last():
    """Test with multiple streaks, where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3

def test_multiple_streaks_longest_first():
    """Test with multiple streaks, where the longest streak is at the beginning."""
    assert longest_positive_streak([1, 2, 3, 0, 5, 6]) == 3

def test_example_case():
    """Test the example from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_same_positive_number():
    """Test with a streak of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_zeros_and_negatives_breaking_streaks():
    """Test that both zeros and negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -1, 5]) == 2