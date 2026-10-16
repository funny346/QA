from random import shuffle, random

import pytest
from Calc_day2 import Calculator

@pytest.fixture
def calc():

    return Calculator()
@pytest.mark.parametrize("expression, expected_res",[
    ("1+1", "2"),
    ("0+2", "2"),
    ("99+101", "200"),
    ("1/1", "1.0"),
    ("0/2", "0.0"),
    ("90/0", "Ошибка"),
    ("1-1", "0"),
    ("0-2", "-2"),
    ("99-101", "-2"),
    ("1*1", "1"),
    ("0*2", "0"),
    ("99*101", "9999"),
])
def test_calc(calc, expression, expected_res):
    assert calc.calculate(expression) == expected_res

