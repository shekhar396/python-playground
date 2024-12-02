def mysplit(str):
    if str == '' or str.isspace():
        return [ ]
    lst=[]
    str_build=''
    for c in str:
        if not c.isspace():
            str_build+=c
        if str_build !='' and c.isspace():
            lst.append(str_build)
            str_build=''
    lst.append(str_build)
    return lst

    

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print('---------------------------')
print("To be or not to be, that is the question".split())
print("To be or not to be,that is the question".split())
print("   ".split())
print(" abc ".split())
print("".split())
