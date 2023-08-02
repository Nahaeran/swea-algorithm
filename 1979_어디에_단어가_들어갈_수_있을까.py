T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        row = 0
        col = 0
        for j in range(N):
            if li[i][j]:
                row += 1
            else:
                row = 0
            if li[j][i]:
                col += 1
            else:
                col = 0
            try:
                if row == K and li[i][j + 1] == 0:
                    result += 1
                if col == K and li[j + 1][i] == 0:
                    result += 1
            except:
                if row == K:
                    result += 1
                if col == K:
                    result += 1
    print(f'#{tc} {result}')