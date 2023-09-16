di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def grid(cur_i, cur_j, cur_str, cnt):
    if cnt == 7:
        set_seven.add(cur_str)
        return
    for k in range(4):
        ni = cur_i + di[k]
        nj = cur_j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            grid(ni, nj, cur_str + board[ni][nj], cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    board = [list( input().split()) for _ in range(4)]
    set_seven = set()
    for i in range(4):
        for j in range(4):
            grid(i, j, board[i][j], 1)
    print(f'#{tc} {len(set_seven)}')