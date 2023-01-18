num = 9
array = []
for i in range(num):
    array.append(int(input()))

a = 0
b = 0
for i in range(num-1):
  for j in range(i+1, num):
    if sum(array)-(array[i]+array[j])==100:
      a=array[i]
      b=array[j]


array.remove(a)
array.remove(b)
array.sort()

for i in range(len(array)):
    print(array[i]) 