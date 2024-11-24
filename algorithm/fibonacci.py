def fibonacci_calcolator(n):
    if n<0:
        return None
    if n<3:
        return 1
    
    n1=n2=1
    sum=0
    for i in range(3,n+1):
        sum=n1+n2
        n1,n2=n2,sum
    return sum

def fibonacci_recursion(n):
    if n<0:
        return None
    if n<3:
        return 1
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)

print(fibonacci_recursion(9))