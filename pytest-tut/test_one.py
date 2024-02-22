# test_one.py
import pytest
import math

def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80

def get_average(li):
    if not li:
            return float('NaN')
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average_normal_use_case():
    assert math.isclose(get_average([1,2,3,4]), 2.5)

# test_exception.py
def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]

def test_palindrome():
    with pytest.raises(TypeError):
        palindrome(44)