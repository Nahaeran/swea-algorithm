# di = [0, 1]
# dj = [1, 0]
#
#
# def permutation(i, n):
#     if i == n:
#         if p not in all_com:
#             all_com.append(list(p))
#     else:
#         for j in range(n):
#             if not used[j]:
#                 p[i] = arr[j]
#                 used[j] = 1
#                 permutation(i + 1, n)
#                 used[j] = 0
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#
#     arr = [0, 1] * (N - 1)
#     p = [0] * (2 * (N - 1))
#     used = [0] * (2 * (N - 1))
#     all_com = []
#     permutation(0, 2 * (N - 1))
#
#     result = 10000
#     for com in all_com:
#         ni = nj = 0
#         temp = matrix[0][0]
#         for i in range(len(com)):
#             ni += di[com[i]]
#             nj += dj[com[i]]
#             temp += matrix[ni][nj]
#         if result > temp:
#             result = temp
#     print(f'#{tc} {result}')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        matrix[0][i] += matrix[0][i - 1]
        matrix[i][0] += matrix[i - 1][0]

    for i in range(1, N):
        for j in range(1, N):
            l = matrix[i][j - 1]
            t = matrix[i - 1][j]
            matrix[i][j] += min(l, t)

    print(f'#{tc} {matrix[N-1][N-1]}')

