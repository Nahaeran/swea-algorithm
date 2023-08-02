T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                for s in range(M):
                	temp += li[i + k][j + s]
            if result < temp:
                result = temp
    print(f'#{tc} {result}')