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

print(fibonacci_calcolator(9))