# di = [1, 0, -1, 0]
# dj = [0, 1, 0, -1]
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     rooms = [list(map(int, input().split())) for _ in range(N)]
#
#     max_num_room = 1
#     room = 1000000
#     for i in range(N):
#         for j in range(N):
#             num_room = 1
#             ni = i
#             nj = j
#             visited = []
#             stack = []
#             while True:
#                 for k in range(4):
#                     if 0 <= ni + di[k] < N and 0 <= nj + dj[k] < N:
#                         if rooms[ni + di[k]][nj + dj[k]] - rooms[ni][nj] == 1 and [ni, nj] not in visited:
#                             stack.append([ni, nj])
#                             visited.append([ni, nj])
#                             ni += di[k]
#                             nj += dj[k]
#                             num_room += 1
#                             break
#                 else:
#                     if stack:
#                         ni, nj = stack.pop()
#                     else:
#                         break
#             if max_num_room <= num_room:
#                 if max_num_room == num_room and room < rooms[i][j]:
#                     pass
#                 else:
#                     room = rooms[i][j]
#                 max_num_room = num_room
#
#     print(f'#{tc} {room} {max_num_room}')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    num_list = [[0] for _ in range(N**2)]

    for i in range(N):
        for j in range(N):
            num_list[rooms[i][j] - 1] = [i, j]

    max_count = 0
    n_count = 1

    for k in range(N ** 2, 1, -1):
        i, j = num_list[k - 1]
        di, dj = num_list[k - 2]

        if abs(i - di) + abs(j - dj) == 1:
            n_count += 1
            if n_count >= max_count:
                ans = k - 1
                max_count = n_count
        else:
            n_count = 1

    print(f'#{tc} {ans} {max_count}')

