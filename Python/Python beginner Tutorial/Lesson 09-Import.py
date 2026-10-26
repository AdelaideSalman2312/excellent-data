'''
Lesson 09-Import
import from os
os random datetime mathmtics'''
import os
from random import randint
from datetime import datetime as dt


cwd = os.getcwd()
print(cwd)
files=os.listdir()
print(files)
os.system('cls||clear')

for i in range (10):
    print(randint(1,10))

time = dt(2025,6,1,2,3,4)
print(time)


