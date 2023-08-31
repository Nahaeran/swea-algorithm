def permutation(i, n):
    if i == n:
        temp = [1]
        temp += p
        temp += [1]
        all_com.append(temp)
    else:
        for j in range(n):
            if not used[j]:
                p[i] = arr[j]
                used[j] = 1
                permutation(i + 1, n)
                used[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(2, N + 1))
    all_com = []

    p = [0] * (N - 1)
    used = [0] * (N - 1)
    permutation(0, N - 1)

    result = 10000
    for com in all_com:
        temp = 0
        for i in range(len(com) - 1):
            ni = com[i] - 1
            nj = com[i + 1] - 1
            temp += matrix[ni][nj]
        if result > temp:
            result = temp

    print(f'#{tc} {result}')