def dic_test():
    school_class={}
    while True:
        name = input("Enter Name: ")
        if name=='':
            break

        score=int(input("enter socre"))

        if name in school_class:
            school_class[name] +=(score,)
        else:
            school_class[name]=(score,)

    for name in sorted(school_class.keys()):
        print(school_class[name],end='\n -------------------')
        for score in school_class[name]:
            print(name," ",score)

def dic_test_2():
    #Expected output 
    # a
    # b
    # c
    dictionary = {}
    my_list = ['a', 'b', 'c', 'd']
    
    for i in range(len(my_list) - 1):
        dictionary[my_list[i]] = (my_list[i], )


    
    for i in sorted(dictionary.keys()):
        k = dictionary[i]
        # Insert your code here.
        print(k[0])



d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
d3.update(d1)
d3.update(d2)
d3.update(d3)

print(d3)

