def combination(n, r):
    global count
    if r == 0:
        if sum(tr) == K:
            count += 1
    elif n < r:
        return
    else:
        tr[r - 1] = ai[n - 1]
        combination(n - 1, r - 1)
        combination(n - 1, r)


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    ai = list(map(int, input().split()))

    count = 0
    for r in range(1, N):
        tr = [0] * r
        combination(N, r)

    print(f'#{tc} {count}')