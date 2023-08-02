T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    result = 0
    for i in range(N):
        temp = 0
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    temp += abs(li[ni][nj] - li[i][j])
        result += temp
    print(f'#{tc} {result}')