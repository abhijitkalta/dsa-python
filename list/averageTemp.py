d1 = int(input('How many days temp? '))
temp = []
for i in range(d1):
    n = int(input('Enter day ' + str(i+1) + ' high temp:'))
    temp.append(n)

sum = 0
length = len(temp)
for i in temp:
    sum += i

average = sum/length
print('Average = {}'.format(average))

days = 0
for i in temp:
    if i > average:
        days +=1

print('{} days above average'.format(days))
