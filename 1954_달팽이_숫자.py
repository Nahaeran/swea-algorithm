T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [[0] * N for _ in range(N)]

    di = []
    dj = []
    for n in range(N, 0, -1):
        for _ in range(n):
            di.append(0)
            dj.append(1 - 2 * ((N - n) % 2))
        for _ in range(n - 1):
            di.append(1 - 2 * ((N - n) % 2))
            dj.append(0)

    i = j = 0
    for e in range(1, N*N+1):
        result[i][j] = e
        if e != N*N:
            i += di[e]
            j += dj[e]
    print(f'#{tc}')
    for line in result:
        print(*line)
