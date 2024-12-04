def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print("An Error")

print("The End")


def bad_fun2(n):
    try:
        return n/0
    except:
        print("I did it again!")
        raise

try:
    bad_fun2(0)
except ArithmeticError:
    print("I See")

print("The End")

