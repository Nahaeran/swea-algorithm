def find_subset_sum_zero(arr, n):
    for i in range(1, 1 << n):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset_sum += arr[j]
        if subset_sum == 0:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    N = len(li)
    result = find_subset_sum_zero(li, N)
    print(f'#{tc} {result}')