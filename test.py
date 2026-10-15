import pytest
from l3_tasks_1_project_day1 import CalculatorEngine

def test_addition():
    """Тест проверяет обычное сложение"""
    calc = CalculatorEngine()
    result = calc.Calc(2, 3, "+")

    assert result == 5
    assert calc.show_history() == [5]  # Проверяем, что в истории сохранился результат

def test_division_by_zero():
    """Тест проверяет защиту от деления на ноль"""
    calc = CalculatorEngine()
    result = calc.Calc(5, 0, "/")
    assert result == "Делить на ноль нельзя"
    # При делении на ноль история не должна пополняться (ведь вычисления не произошло)
    assert len(calc.show_history()) == 0

def test_clear_history():
    """Тест проверяет очистку истории"""
    calc = CalculatorEngine()
    calc.Calc(2, 2, "+")  # Добавит 4 в историю
    calc.clear_history()  # Очищаем
    assert calc.show_history() == []  # История должна стать пустой
