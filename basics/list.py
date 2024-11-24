import random
class List:
    @staticmethod
    def test():
        lst=[1,2,3,4,5]
        del lst[1]
        print(len(lst))
        print(lst)
        print(lst[-3])

    @staticmethod
    def hatProblem():
        hat_list=[1,2,3,4,5]
        hat_list[2]=int(input("Enter Number: "))
        del hat_list[-1]
        print(len(hat_list))
        print(hat_list)
    
    @staticmethod
    def listOperation():
        lst=[1,2,3,4,5]
        lst.append(10)
        print(lst)
        lst.insert(0,1000)
        print(lst)

        total=0

        for i in range(len(lst)):
            total+=lst[i]
        print(total)

    def assignment_and_reference_demo():
        a=10
        b=a
        a=15
        print(b)

        lst1=[15,20]
        lst2=lst1
        lst1=[30,40]
        lst1[0]=300
        print(lst2)

        list_1 = [1,2]
        list_2 = list_1
        list_1[0] = 2
        print(list_2)

        list_a=[1]
        list_b=list_a[:]
        list_a[0]=100
        print(list_b)

    def list_slice():
        my_list=[10,12,15,20,25]
        new_list=my_list[1:3]
        print(25 in new_list)

    def find_largest():
        lst=[10,15,390,400,2,100,99,43]
        largest=lst[0]
        for i in range(1,len(lst)):
            if lst[i]>largest:
                largest=lst[i]
        print(largest)

    def list_comprehension():
        squares = [x ** 2 for x in range(10)]

        test=[x for x in range(2,20,2)]
        print(test)
        print(squares)
    
    def two_d_array():
        EMPTY = 0
        board=[[EMPTY for i in range(8)] for j in range(8)]
        print(board)
    
    def avg_temp():
        temp=[[i for i in range(24)] for j in range(31)]

        total=0.0
        for day in temp:
            total+=day[11]
        
        print(total/31)
    
    def highest_tem():
        temp=[[random.randint(-11, 34) for i in range(24)] for j in range(31)]
        print(temp)

        highest=-100
        for day in temp:
            for hours in day:
                if hours>highest:
                    highest=hours
        print('highest: ',highest)

    
    def hotel_booking():
        rooms=[[[random.choice([True,False]) for i in range(5)] for j in range(4)] for k in range(3)]
        # rooms = [[[random.choice([True, False]) for j in range(4)] for i in range(5)] for k in range(3)]
        a = 1
        b = 0
        c = a ^ b 
        

        print(c)
    
    
# List.hotel_booking()