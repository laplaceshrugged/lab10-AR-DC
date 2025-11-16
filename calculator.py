"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError()
    return math.sqrt(a)
def hypotenuse(a, b): 
    return math.hypot(a, b)
def mul(a, b):
    return a * b
def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError:
        print("Can't divide by zero")
def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def logarithm(a, b):
    try:
        return math.log(b,a)
    except ValueError:
        raise ValueError()
def exp(a, b):
    return pow(a,b)
