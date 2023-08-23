dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def stone_laying(x, y, color, N):
    board[x][y] = color
    for k in range(8):
        changes = []
        for s in range(1, N):
            nx = x + dx[k] * s
            ny = y + dy[k] * s
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == color:
                    while changes:
                        i, j = changes.pop()
                        board[i][j] = color
                    break
                elif board[nx][ny] == 0:
                    break
                else:
                    changes.append([nx, ny])
            else:
                break


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N//2 - 1][N//2] = board[N//2][N//2 - 1] = 1
    board[N//2 - 1][N//2 - 1] = board[N//2][N//2] = 2

    for _ in range(M):
        y, x, color = map(int, input().split())
        stone_laying(x-1, y-1, color, N)

    count1 = count2 = 0
    for i in range(N):
        count1 += board[i].count(1)
        count2 += board[i].count(2)

    print(f'#{tc} {count1} {count2}')
