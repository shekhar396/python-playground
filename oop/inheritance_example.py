class Super:
    def __init__(self,name):
        self.__name=name
    
    def __str__(self):
        return self.__name

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj=Sub("Andy")

print(obj)