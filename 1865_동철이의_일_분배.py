def work(total, p):
    global result
    if total <= result:
        return
    if p == N:
        result = max(result, total)
        return
    for j in range(N):
        if used_w[j] or not Pi[p][j]:
            continue
        used_w[j] = 1
        total *= Pi[p][j] / 100
        work(total, p + 1)
        used_w[j] = 0
        total /= Pi[p][j] / 100
    return total


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Pi = [list(map(int, input().split())) for _ in range(N)]
    used_w = [0] * N
    result = 0
    work(100, 0)
    print(f'#{tc} {result:.6f}')



