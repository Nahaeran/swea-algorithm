T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()

    for i in range(N):
        bread = (times[i] // M) * K
        if bread < i + 1:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')