inputString = input()

inputString = inputString.replace('XXXX', 'AAAA')
inputString = inputString.replace('XX', 'BB')

if 'X' in inputString: print(-1)
else:print(inputString)
