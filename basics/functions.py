def introduction(first_name, last_name=''):
    print("Hello, my name is", first_name, last_name)
 
# introduction("Skywalker", "Luke")
# introduction("Quick", "Jesse")
# introduction(first_name="Kent")

def add(a,b,c):
    d = 'print(a+b+c)'
    eval(d)

def is_year_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
def days_in_month(year, month):
    if month  in [1,3,5,7,8,10,12]:
        return 31
    elif month ==2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else:
        return 30
def tuple_test():
    global xyz
    xyz=123
    t1=(1,)
    t2=(1,2,3,4.0)
    t3=t1+t2
    print(t1,' ',t2,' ',t3)
tuple_test()

print(xyz)

