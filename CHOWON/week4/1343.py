# 문제풀이 흐름 정리
# 보드판 입력받고, '.'을 기준으로 보드판 나누기
# 나눠진 보드판을 돌면서 AAAA와 BB로 덮일지 체크
# 4나 2로 나눈 나머지가 0이 아닌 일부 보드판이 있다면 -1 출력 후 종료
# BB가 길이 2로, 그에 대한 배수가 AAAA의 길이가 되므로 그리디 가능
# 
# 뭔데 반례 다 맞게 나오는데 왜 틀렸는데 왜요 왜


board = input()
separatedBoard = board.split('.')

failFlag = False
emptyCount = 0
result = ""
for b in separatedBoard:
    if len(b) == 0:
        emptyCount += 1
    if len(result) > 0:
        result += "."
    if (len(b) % 4) == 0 :
        for i in range(int(len(b)/4)):
            result += "AAAA"
    elif (len(b) % 4) == 2 :
        for i in range(int(len(b)/4)):
            result += "AAAA"
        result += "BB"
    elif (len(b) % 2) == 0 :
        for i in range(int(len(b)/2)):
            result += "BB"
    else:
        failFlag = True
        break

if failFlag:
    print(-1)
else:
    if len(result) == 0:
        for i in range(emptyCount - 1):
            result += "."   # .만으로 이루어진 입력이 보드로 주어졌을 경우를 대비
    print(result)