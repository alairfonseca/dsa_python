"""
Write a Python program that can simulate a simple calculator,
using the console as the exclusive input and output device.
That is, each input to the calculator, be it a number, like
12.34 or 1034, or an operator, like + or =, can be done on a
separate line. After each such input, you should output to the
Python console what would be displayed on your calculator.
"""
import sys
from os import system

OPERATORS = "+=*/"


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    if operator == '-':
        return a + b
    if operator == '*':
        return a * b
    if operator == '/':
        return a / b


def validate_operator(operator):
    return operator.strip('\n') in OPERATORS


def validate_operand(operand):
    try:
        float(operand)
        return True
    except ValueError:
        return False


def calculator():
    a = None
    b = None
    operator = None

    for line in sys.stdin:
        if (a is None):
            if validate_operand(line):
                a = float(line.strip('\n'))
                system('clear')
                print(a)
        elif (operator is None) & (a is not None):
            if validate_operator(line):
                operator = line.strip('\n')
                system('clear')
                print(a, operator)
            else:
                a = None
        elif (b is None) & (operator is not None):
            if validate_operand(line):
                b = float(line.strip('\n'))
                system('clear')
                print(a, operator, b)
                print(calculate(a, b, operator))
                a = None
                b = None
                operator = None
            else:
                a = None
                operator = None


if __name__ == "__main__":
    calculator()
