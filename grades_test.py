import pytest
from test import calculate_average_test_scores, get_letter_grade  

def test_calculate_average_test_scores():
    file_path = 'grades.csv'
    expected_average = 75.0  
    actual_average = calculate_average_test_scores(file_path)
    assert actual_average == pytest.approx(expected_average, 0.01), f"Expected {expected_average}, but got {actual_average}"

def test_get_letter_grade():
    assert get_letter_grade(95) == 'A'
    assert get_letter_grade(85) == 'B'
    assert get_letter_grade(75) == 'C'
    assert get_letter_grade(65) == 'D'
    assert get_letter_grade(55) == 'F'

if __name__ == "__main__":
    pytest.main()