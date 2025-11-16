"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError:
        print("Can't divide by zero")

def log(a, b):
    try:
        if a < 0 or b < 0:
            raise ValueError
        return math.log(a, b)
    except ValueError:
        print("Can't accept numbers less than or equal to 0")

def exp(a, b):
    return pow(a,b)
