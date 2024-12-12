class Classy:
    def other(self):
        print("other")
    
    def method(self):
        self.other()
    
    def __hidden(self):
        print("Hidden")

obj=Classy()
obj.method()
try:
    obj.__hidden()
    # obj._Classy__hidden()
except:
    print("Failed")

print(obj.__dict__)
print(Classy.__dict__)
print(Classy.__name__)
print(type(obj).__name__)
print(Classy.__module__)
print(obj.__module__)