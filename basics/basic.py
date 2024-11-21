class MyMath:
    @staticmethod
    def inputMath():
        a=float(input("Enter a floating number.: "))
        b=float(input("Enter a floating number.: "))
        print("sum: ",a+b, "sub: ",a-b, "mult: ",a*b, "div: ",round(a/b,2))

    @staticmethod
    def basicOperators():
        x=float(input("Enter number: "))
        y=(1/(x+(1/(x+1/(x+1/x)))))
        print(y)

    @staticmethod
    def timeCalculation():
        o=int(input("Enter Hour: "))
        m=int(input("Enter Min: "))
        d=int(input("Enter Duration: "))

        totalMin=m+d
        additionalHours=int(totalMin/60)
        restMin=totalMin%60
        expectedHours=(o+additionalHours)%24

        print(expectedHours,':',restMin)

    @staticmethod
    def test():
        a=3
        b=5
        a=a+b
        b=a-b
        a=a-b
        print(a,b)



    

MyMath.test()