T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0
    # stack = [0] * max(N, M)
    # top = -1

    for i in range(N):
        row_sum = 0
        for j in range(M):
            if li[i][j]:
                row_sum += 1
                if max_len < row_sum:
                    max_len = row_sum
            else:
                row_sum = 0

    for j in range(M):
        col_sum = 0
        for i in range(N):
            if li[i][j]:
                col_sum += 1
                if max_len < col_sum:
                    max_len = col_sum
            else:
                col_sum = 0

    print(f'#{tc} {max_len}')