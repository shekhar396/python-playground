import math

x = float(input("Enter a number: "))
assert x>=0.0,"X must be 0 or positive"

x = math.sqrt(x)

print(x)

def divide(a, b):
    assert b != 0, "Denominator must not be zero"
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # AssertionError: Denominator must not be zero

def foo(x):
    assert x
    return 1/x
print(foo(0))