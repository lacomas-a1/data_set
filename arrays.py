#array-is a special value that can hold more than one value at a time.
data = [1.6, 3.4, 5.5, 9.4]
N =len(data)
print(N)
print(data[2])
data[2]=7.3
print(data[2])

for x in data:
    print(x)

data.append(11.4)
N=len (data)
print(N)

for x in data:
    print(x)