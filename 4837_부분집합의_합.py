T = int(input())
ARR = list(range(1, 13))

for tc in range(1, T+1):
    N, K = map(int, input().split())

    result = 0
    for i in range(1, 1 << 12):
        subset_len = 0
        subset_sum = 0
        for j in range(12):
            if i & (1 << j):
                subset_len += 1
                print(ARR, j)
                subset_sum += ARR[j]
        if subset_len == N and subset_sum == K:
            result += 1

    print(f'#{tc} {result}')
