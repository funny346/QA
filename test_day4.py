

import pytest

from Calculator.day4 import clean_city_name, extract_weather_info, analyze_history



def test_clean_city_name_positive():
    assert clean_city_name(" БрЕсТ") == "Брест"

def test_clean_city_name_negative():
    assert clean_city_name(" 12312dsadas") == "Invalid name"

def test_extract_weather_info():
    example = {
        "name": "Лондон",
        "main": {"temp": 15.4},
        "weather": [{"description": "небольшой дождь"}]}
    res = extract_weather_info(example)

    assert res["name"] == "Лондон"
    assert res["temp"] == 15.4
    assert res["description"] == "небольшой дождь"

def test_analyze_history_positive():
    example = [10.0, 15.5, 8.2, 14.3]
    res = analyze_history(example)

    assert res["min"] == 8.2
    assert res["max"] == 15.5
    assert res["avg"] == 12.0

def test_analyze_history_negative():
    example = []
    res = analyze_history(example)

    assert res["min"] == None
    assert res["max"] == None
    assert res["avg"] == None