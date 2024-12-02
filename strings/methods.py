the_string = "Hello World"
print(ord(min(the_string)))
print(max(the_string))
print(the_string.index('o'))
print(list(the_string))
print(the_string.count('o'))
print(the_string.capitalize())
print('[' + 'alpha'.center(10) + ']')
print('[' + 'alpha'.center(20,'*') + ']')

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)