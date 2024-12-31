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