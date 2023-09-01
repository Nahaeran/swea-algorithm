T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort(reverse=True)

    result = j = 0
    for i in range(N):
        if wi[i] <= ti[j]:
            result += wi[i]
            j += 1
        if j == M:
            break

    print(f'#{tc} {result}')