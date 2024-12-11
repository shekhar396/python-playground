class ExampleClass:
    def __init__(self,val):
        if val % 2 !=0:
            self.a=1
        else:
            self.b=1
        
obj=ExampleClass(11)

try:
    print(obj.a)
    print(obj.b)
except AttributeError:
    print("Not Found")

print(hasattr(obj,'a'))
print(hasattr(obj,'b'))
print(hasattr(ExampleClass,'b'))

