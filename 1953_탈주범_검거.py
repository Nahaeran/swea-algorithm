from collections import deque

possible_dict = {
    1 : [[1, 2, 4, 7], [1, 3, 6, 7], [1, 2, 5, 6], [1, 3, 4, 5]],
    2 : [[1, 2, 4, 7], [], [1, 2, 5, 6], []],
    3 : [[], [1, 3, 6, 7], [], [1, 3, 4, 5]],
    4 : [[], [1, 3, 6, 7], [1, 2, 5, 6], []],
    5 : [[1, 2, 4, 7], [1, 3, 6, 7], [], []],
    6 : [[1, 2, 4, 7], [], [], [1, 3, 4, 5]],
    7 : [[], [], [1, 2, 5, 6], [1, 3, 4, 5]]
}

T = int(input())
# 하 우 상 좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    count = 1
    time = L - 1
    deq = deque()
    deq.append([R, C, time])
    visited[R][C] = 1

    while deq:
        t = deq.popleft()
        if t[2] == 0:
            break
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and tunnel[ni][nj] in possible_dict[tunnel[t[0]][t[1]]][k]:
                visited[ni][nj] = 1
                deq.append([ni, nj, t[2] - 1])
                count += 1

    print(f'#{tc} {count}')