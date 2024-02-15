import pytest
from src.main import decimal_a_romano

def test_lowest_number_conversion():
    assert decimal_a_romano(1) == "I"


_