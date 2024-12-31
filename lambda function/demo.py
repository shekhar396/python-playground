two=lambda: 2
sqr=lambda x:x*x
pwr=lambda x,y: x**y
print(two())
print(sqr(two()))
print(pwr(2,3))

def print_function(args,fun):
    for x in args:
        print(fun(x))

def poly(x):
    return 2*x**2-4*x+2
print_function([x for x in range(-2,3)],poly)
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
print("---------Map----------")
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
print("---------Filter----------")
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
    