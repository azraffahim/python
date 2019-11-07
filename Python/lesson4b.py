""" List
====================
"""
mototrcycles=['honda','yamaha','suzuki']


print(mototrcycles)
print(mototrcycles[1])

mototrcycles[0]='hero'
print(mototrcycles)



fruits=[]

fruits.append('Orange')
fruits.append('Mango')
fruits.append('Banana')
print(fruits)

fruits.insert(1,'Apple')
print(fruits)
print('after sorting:')
fruits.sort()
print(fruits)
print('After reverse')
#fruits.sort(reverse=True)

fruits.reverse()
print(fruits)

print('After Removing')

fruits.remove('Apple')
print(fruits)