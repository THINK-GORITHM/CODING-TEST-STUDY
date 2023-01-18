N = int(input())
array = []
result = []
a = 1
b = True
for i in range(N):
    num = int(input())
    while num>= a:
        array.append(a)
        a+=1
        result.append("+")
    
    if(array[-1] == num): 
        array.pop()
        result.append("-")
    else: 
        print("NO")
        b = False
        break

if b:
    for i in result:
        print(i)
