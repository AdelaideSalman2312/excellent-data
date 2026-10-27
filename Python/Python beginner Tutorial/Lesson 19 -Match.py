'''
Lesson 19 - match
match
'''
command = input('Choose a greeting')
match command:
    case '1' :
        print('Hi')
    case '2' :
        print('Hello')
    case _:
        print('Invalid choice')

item = 2
match item:
    case int(x) if x > 0:
        print('Item is a positive number')
    case str(x):
        print('item is a string ',x)
    case list(x):
        print('item is a list') 
