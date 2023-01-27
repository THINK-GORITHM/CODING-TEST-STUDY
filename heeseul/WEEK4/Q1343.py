board = input()  # 보드판
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')
if 'X' in board:
    print(-1)
else: print(board)
