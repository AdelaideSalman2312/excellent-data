import os
file = open('Lesson 02 - string.py','r')
content = file.read()
print(content)
file.close()

with open('Lesson 02- variable.py', 'r') as file:
    content = file.read()
    print(content)

with open('output.txt','w') as file:
        file.write('first line\n')
        file.write('second line\n')

with open('output txt ,r') as file:
     print(file.read())
      
with open('output.txt','r') :     
      file.write('Second line')
      
with open('output.txt','r')as file:
      print(file.read())

      os.remove('output.txt')



