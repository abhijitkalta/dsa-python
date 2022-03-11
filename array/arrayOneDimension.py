import array as arr

#Create an array and traverse
ar1 = arr.array('i', [1, 2, 5, 8, 11])
for i in ar1:
    print(i)

#Access individual elements through indexes
print(ar1[2])

#Append value to array
ar1.append(25)
print(ar1)

#Insert value in an array using insert
ar1.insert(1, 10)
print(ar1)

#Extend array
ar1.extend([3, 4])
print(ar1)

#Add items from list using fromList()
l1 = [1, 34]
ar1.fromlist(l1)
print(ar1)

#Remove elements
ar1.remove(8)
print(ar1)

#Pop index 5 ->
print(ar1.pop(5))
print(ar1)

#Fetch through index
k = ar1.index(3)
print(k)

#Reverse
ar1.reverse()
print(ar1)

#Buffer info
print(ar1.buffer_info())

#Number of occurences
print(ar1.count(1))

#convert array to string
print(','.join(str(x) for x in ar1))
print(ar1)

#convert array to list
l1 = ar1.tolist()
print(l1)
print(ar1)

#Append string to char array
chr1 = arr.array('u', ['a', 'b'])
chr1.append('H')
print(chr1)

#Slice elements
print(ar1[2: 6])
