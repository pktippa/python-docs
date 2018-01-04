# To run the test case run as $ python -m pyteset pytest_code.py
import pytest
from topackage.actualcode import boarding # Inorder to import a file we can just convert the folder to package by adding empty __init__.py
def test_boarding_1():
    result=boarding(3)
    assert result==1
                
def test_boarding_2():
    result=boarding(28)
    assert result==2

# Parameterized pytest cases.
# Instead of writing multiple test cases for same functionality we can write
# one pytest test case with a list of tuples.

values = [(0,-1),(1,1),(25,1),(100,2),(199,3),(201,-1)]

@pytest.mark.parametrize("seat_number,expected_value",values)
def test_borading(seat_number, expected_value):
    result = boarding(seat_number)
    assert result == expected_value
