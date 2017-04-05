# To run the test case run as $ python -m pyteset pytest_code.py
import pytest
from topackage.actualcode import boarding # Inorder to import a file we can just convert the folder to package by adding empty __init__.py
def test_boarding_1():
        result=boarding(3)
        assert result==1
                
def test_boarding_2():
        result=boarding(28)
        assert result==2