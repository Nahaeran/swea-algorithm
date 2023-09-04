from collections import deque

T = int(input())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]

    deq = deque()
    visited = [[-1] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                visited[i][j] = 0
                deq.append([i, j])

    while deq:
        t = deq.popleft()
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                visited[ni][nj] = visited[t[0]][t[1]] + 1
                deq.append([ni, nj])
    result = 0
    for i in range(N):
        for j in range(M):
            result += visited[i][j]

    print(f'#{tc} {result}')