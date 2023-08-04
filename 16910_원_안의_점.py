T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_sq = N ** 2

    result = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i**2 + j**2 <= N_sq:
                result += 1
    result *= 4
    result += (2*N+1) * 2 - 1
    print(f'#{tc} {result}')
