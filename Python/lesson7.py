dict ={'Ali':18,'Rahim':20,'Ryan':22}

print(dict['Rahim'])

boys ={'Ali':18,'Rahim':20,'Ryan':22}
girls = {'Ab':18,'bc':20,'nn':22}

studentx=boys.copy()
studenty=girls.copy()

dict.update({'kamal':40})
print(dict)


print('del by key')

#del dict['Ali']
#print(dict)

#print(type(studentx))
#print(dir(dict))

print("Students Name: %s" % dict.items())
'''

print('only keys: ')
for val in dict.values():
    print(val)

'''
students = list(dict.keys())
students.sort()
print('Sorted keys:' + str(students))

print('KEY 1 :'+ students[1])