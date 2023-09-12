T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    hi = list(map(int, input().split()))

    result = B
    for i in range(1<<N):
        temp = -B
        for j in range(N):
            if i & 1<<j:
                temp += hi[j]
        if temp >= 0 and result > temp:
            result = temp

    print(f'#{tc} {result}')