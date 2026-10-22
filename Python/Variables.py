# Variables in Python -A variable is like a box in the computer’s memory where you can store a 
#single value. If you want to use the result of an evaluated expression later 
#in your program, you can save it inside a variable

#Assignment Statements
#You’ll store values in variables with an assignment statement. An assignment 
#statement consists of a variable name, an equal sign (called the assignment 
#operator), and the value to be stored. If you enter the assignment state
#ment love = 42, then a variable named love will have the integer value 42 
#stored in it.

love = 42 
print(love)
love = 140
print (love)

#A variable is initialized (or created) the first time a value is stored in it 
#After that, you can use it in expressions with other variables and values . 
#When a variable is assigned a new value , the old value is forgotten, which 
#is why love evaluated to 42 instead of 140 

#For the clean code's sake name the variable - as if describing the data it contains eg-heightMen - contains data for me's heights .
# Rules for naming variables - sikiliza vizuri sana It can be only one word with no spaces.	It can use only letters, numbers, and the underscore (_) character.	It can’t begin with a number.
print('Hello, Doctor Lillian')
print('What Unit are you taking me through?')
Unit = input()
print('I am happy to meet you , I am taking you through' + Unit)
print('Length of the Unit name is :') 
print(len(Unit))
print('How long is your teaching experience?')
TE = input()
print('My teaching experience is '+TE + 'years')