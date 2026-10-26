"List is a collection which is ordered and changeable (modifiable) and it allows duplicate members and different data types."

friends =['Angela','Hassan','Husna','Rehan','Husna']
print(friends)
lst = [12.30 , 'Melbourne ', 'Kigali',True, 12 ,16 , 4,{'Nairobi','Dar es Salaam'}]
print(lst)

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
spam[1]
spam[2]
spam[3]
#spam[4]Python will give you an IndexError error message if you use an index 
#that exceeds the number of values in your list value. Indices can only be integer values not float values 
'Hello, ' + spam[0]
'The ' + spam[1] + ' ate the ' + spam[0] + '.'
# Negative Indices 
spam [-1]
spam [-3]

'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'

#Getting a List from Another List with Slices

"Just as an index can get a single value from a list, a slice can get several values from a list, in the form of a new list. "

" A slice is typed between square brackets, like an index, but it has two integers separated by a colon"
" spam[2] is a list with an index (one integer). spam[1:4] is a list with a slice (two integers)"
# In a slice , , the first integer is the index where the slice starts. The second integer is the index where the slice ends.
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
['cat', 'bat', 'rat', 'elephant']
spam[1:3]
['bat', 'rat']
spam[0:-1]
['cat', 'bat', 'rat' ]
spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2]

['cat', 'bat']
spam[1:]
['bat', 'rat', 'elephant']
spam[:]
['cat', 'bat', 'rat', 'elephant']

#Getting a List's Length with the len() function 
len(spam)

#Changing Values in a List with Indexes

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam
spam[2] = spam[1]
spam

#List Concatenation and Replication

"Lists can be concatenated and replicated just like strings. The + operator combines two lists to create a new list value and the * operator can be used with a list and an integer value to replicate the list."

[1, 2, 3] + ['A', 'B', 'C']

spam1 = ['Tortoise', 'Turtle', 'Sea Horse', 'Octopus']
spam2= spam1 + spam 
print (spam2)

#Removing Values from Lists with del Statements

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print (spam)

# The del statement can also be used on a simple variable to delete it, as if it were an “unassignment” statement.

# Working with Lists 

catName1 = 'Zophie'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady Macbeth'
catName5 = 'Fat-tail'
catName6 = 'Miss Cleo'
"This is the part you were told you need to prioritize clean code : It turns out that this is a bad way to write code.-  For one thing, if the number of cats changes, your program will never be able to store more cats than you have variables. These types of programs also have a lot of duplicate or nearly identical code in them."

# Showing how can cause duplicates
print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' + 
catName5 + ' ' + catName6 )

# Instead of using multiple, repetitive variables, you can use a single variable that contains a list value

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + 
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)


#Using for Loops with Lists

for i in range(4):
    print(i)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders'] 
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#The in and not Operator

'howdy' in ['hello', 'hi', 'howdy', 'heyas']


spam3 = ['hello', 'hi', 'howdy', 'heyas'] 

'cat' in spam3

'howdy' not in spam3
'cat' not in spam3

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')


cat = ['fat', 'gray', 'loud']
size, color, disposition = cat


#Using the enumerate() Function with List

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
     
 print('Index ' + str(index) + ' in supplies is: ' + item)

 #Using the random.choice() and random.shuffle() Functions with Lists

 import random
pets = ['Dog', 'Cat', 'Moose']
random.choice(pets)

import random
friends =['Angela','Hassan','Husna','Rehan','Husna']
random.shuffle(friends)

# Augmented Assignment Operators 

spam = 'Hello,'
spam += ' world!'
spam

bacon = ['Zophie']
bacon *= 3
bacon



