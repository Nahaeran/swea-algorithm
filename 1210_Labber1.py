for tc in range(1, 11):
    tc = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]

    row = 99
    col = li[99].index(2)
    while row != 0:
        if col != 0 and li[row][col-1] and before != 'r':
            col -= 1
            before = 'l'
        elif col != 99 and li[row][col+1] and before != 'l':
            col += 1
            before = 'r'
        else:
            row -= 1
            before = 'b'
    print(f'#{tc} {col}')