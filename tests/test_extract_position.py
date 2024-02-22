import pytest
from extract_position import extract_position

def test_extract_position_with_none_input():
    line = None
    assert extract_position(line) is None

def test_extract_position_with_debug_input():
    line = "|debug| lorem ipsum dolor sit amet."
    assert extract_position(line) is None

def test_extract_position_with_error_input():
    line = "|error| unable to perform the operation."
    assert extract_position(line) is None

def test_extract_position_without_x():
    line = "|update| the object's location in the system is y:42.0."
    assert extract_position(line) is None

def test_extract_position_with_valid_input():
    line = '|update| the object is currently located at x:42.0'
    assert extract_position(line) == '42.0'