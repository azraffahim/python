magicians=['olive','meem','sazid']

for magician in magicians:
    print(magician,end='\t')
    print('\n')

    for value in range(1,5):
       print(value)


numbers= list(range(1,10,2))
print(numbers)



digits={12,23,40,50,54,78,17,66,100}
print("The minimum numbers :{}".format(min(digits)))
print("The maxmum numbers :{}".format(max(digits)))
print("The sum numbers :{}".format(sum(digits)))

players=['ryan','torun','sourav','ashik','joy']

print(players[0:2])
print(players[0:1])
print(players[2:4])
# print(players[2:])
# print(players[-2])
# print(players[:])