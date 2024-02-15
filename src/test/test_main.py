import pytest
from src.main import decimal_a_romano

def test_decimal_a_romano():
    assert decimal_a_romano(1) == "I"
