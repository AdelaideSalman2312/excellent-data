lessons={'Lesson 01':'String','Lesson 02':'String' }
print(type(lessons),lessons)
print(lessons['Lesson 01']) 
print(lessons.values())
print(lessons.keys())
lessons['Lesson 03'] = 'Integer'
print(lessons)

for key in lessons:
    print('key =',key,'value =',lessons[key])

del lessons['Lessons 03']
for i in range(len(lessons)):
    print(list(lessons.values())(i))