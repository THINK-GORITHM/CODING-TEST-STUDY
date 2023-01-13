dt = {}

for _ in range(int(input())):
    name = input()
    count = 0
    if dt.get(name) == None:
        dt[name] = 1
    else:
        dt[name] += 1

max = 0
max_book = ""
for key in dt:
    if dt[key] > max:
        max = dt[key]
        max_book = key
    elif dt[key] == max:
        if max_book > key:
            max_book = key

print(max_book)