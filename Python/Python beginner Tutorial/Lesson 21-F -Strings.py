'''
Lesson - 21
f-string
'''
s='python'
print(f'{s.title()}')

n1 = 1
n2 = 2
print(f'{n1} +{n2} +{n1 + n2}')

pi = 3.1449245
print(f'pi = {pi:.2f}')

print(f'n1 ={n1:010d}')# this ensures total width of 10 characters

print(f'{s.replace("p","p") }\n'\
      f'It\'s {s}')

print('''''(s.replace(('p','p'))
It's {s}''''')
