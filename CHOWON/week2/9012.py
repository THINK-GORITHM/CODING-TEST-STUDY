for i in range(int(input())):
    vpsList = list(input())
    result = []
    for p in range(0,len(vpsList)):
        if vpsList[p] == '(':
            result.append('(')
        elif vpsList[p] == ')':
            if len(result) == 0:
                result.append(')')
                break
            else:
                result.pop()
    
    if len(result) == 0:
        print("YES")
    else:
        print("NO")