# from sys import path
'''we've used the relative name of the folder - this will work if you start the main.py file directly from its home folder, and won't work if the current directory doesn't fit the relative path; you can always use an absolute path, like this:
path.append('C:\\Users\\user\\py\\modules')'''
# path.append('..∖∖modules')
 
# import module
 
zeroes = [i for i in range(5) if i % 2 != 0]
print(zeroes)
# ones = [1 for i in range(5)]
# print(module.suml(zeroes))
# print(module.prodl(ones))