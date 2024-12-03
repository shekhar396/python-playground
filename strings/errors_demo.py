first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")

def bad_fun(n):
    return 1 / n
 
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
 
print("THE END.")
 
    