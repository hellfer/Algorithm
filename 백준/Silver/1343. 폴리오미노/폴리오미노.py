board = input().split('.')
filled_board = []

for i in board:
    if len(i) % 2 != 0:
        print(-1)
        break
    else:
        filled_board.append('AAAA' * (len(i) // 4) + 'BB' * ((len(i) % 4) // 2))

else:
    print('.'.join(filled_board))
