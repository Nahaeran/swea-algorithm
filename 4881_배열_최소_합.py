def permutation(i, N, s):
    global min_result
    if i == N:
        result = 0
        for i in range(len(idx)):
            result += matrix[i][idx[i]]
            if result >= min_result:
                return
        min_result = result
    if s >= min_result:
        return
    else:
        for j in range(i, N):
            idx[i], idx[j] = idx[j], idx[i]
            permutation(i + 1, N, s+matrix[i][idx[i]])
            idx[i], idx[j] = idx[j], idx[i]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    idx = list(range(N))
    min_result = float('inf')
    permutation(0, N, 0)
    print(f'#{tc} {min_result}')