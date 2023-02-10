# 문제풀이 흐름 정리 (평석이의 재수강 탈출기,,,ㅎㅋㅎ)
# 단어 개수 N 입력받고, N만큼의 단어를 한 줄씩 입력받음
# 
# "좋은 단어" --> 단어 위로 그은 아치형 곡선이 전혀 겹치지 않고, 모든 글자가 짝을 이룰 수 있는 단어 
# "좋은 단어"가 될 수 없는 경우
#   - 한 쌍의 문자 사이에 다른 문자가 껴있는 경우
#   - 같은 종류 문자가 홀수개 있는 경우(모두 짝을 이룰 수 없음)
#
# 어쩄든 모든 문자열의 경우를 하나하나 뜯어봐야 하는 것 같음
# VPS(괄호 문제)와 유사한 로직으로 풀이 가능
# 최대 100개의 단어에 대해, 최대 1,000,000길이인 문자열 내의 문자를 뜯어보기?
#    * 시간 복잡도 --> 이중 for문 (100 * 1,000,000 = 100,000,000 (1억 = 1초 가능))

result = 0
inputStr = []

for _ in range(int(input())):
  inputStr = list(input())
  temp = []
  for i in range(len(inputStr)):
    # temp 배열 길이가 0인 경우 무조건 요소 추가
    if len(temp) == 0:
      temp.append(inputStr[i])
      continue

    # temp가 비어있지 않은 경우, temp의 가장 마지막 요소와 inputStr의 i번째 글자를 비교
    if (len(temp) > 0) & (temp[len(temp) - 1] == inputStr[i]): 
      temp.pop()
    else:
      temp.append(inputStr[i])
  
  # temp가 빈 배열 -> 모든 글자가 짝을 이루었음을 의미
  if len(temp) == 0:
    result += 1

print(result)


