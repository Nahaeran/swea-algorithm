def find_cost(total, p):
    global result
    if result <= total:
        return
    if p == N:
        result = min(result, total)
        return
    for j in range(N):
        if used[j]:
            continue
        used[j] = 1
        find_cost(total + Vij[p][j], p + 1)
        used[j] = 0
    return total


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Vij = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    result = 100 * N
    find_cost(0, 0)
    print(f'#{tc} {result}')