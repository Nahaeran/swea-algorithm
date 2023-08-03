T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    result = 0
    for i in range(N):
        for j in range(M):
            temp = li[i][j]
            for k in range(4):
                for s in range(1, li[i][j]+1):
                    ni = i + di[k] * s
                    nj = j + dj[k] * s
                    if 0 <= ni < N and 0 <= nj < M:
                        temp += li[ni][nj]
            if result < temp:
                result = temp
    print(f'#{tc} {result}')