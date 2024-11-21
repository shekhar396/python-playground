class Problems:
    def uniqueListMaker(self,myList):
        uniqueList=[]
        for x in myList:
            if x not in uniqueList:
                uniqueList.append(x)
        return uniqueList

    @staticmethod
    def primeNumberGeneretor(n):
        for x in range(2,n):
            isPrime=True
            for i in range(2,(x//2)+1):
                if x%i==0:
                    isPrime=False
                    break
            
            if(isPrime):
                print(x)

    @staticmethod
    def reverseNumber(n):
        reversed_number=0
        while n!=0:
            reversed_number=reversed_number*10+n%10
            n //= 10
        return reversed_number

    
    @staticmethod
    def reversString(s):
        return s[::-1]
    
    @staticmethod
    def isPalindromString(s):
        return s==s[::-1]

    @staticmethod
    def hightCounter(n):
        i=1
        c=1
        h=0
        while i<=n:
            h=c
            c+=1
            i+=c
        print('Height: ',h)
    
    @staticmethod
    def  intriguingHypothesis(c0):
        steps=0
        while True:
            steps+=1
            if(c0%2==0):
                c0=c0//2
            else:
                c0=3*c0+1
            print(c0)
            if c0==1:
                break
        print('Steps: ',steps)
    
    @staticmethod
    def emailName(str):
        name=''
        for c in str:
            if c=='@':
                break
            name+=c
        print(name)


        


    
    def strTest():
       i=15
       print(i>>3)

                    

# problems_obj=Problems()
# res=problems_obj.uniqueListMaker([1,1,3,1,2,5,3,6,2])
# print(res)

Problems.strTest()