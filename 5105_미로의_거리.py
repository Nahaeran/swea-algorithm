di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(maze, v, N):
    visited = [ [0] * N for _ in range(N)]
    queue = [v]
    visited[v[0]][v[1]] = 1

    while queue:
        t = queue.pop(0)
        for i in range(4):
            ni = t[0] + di[i]
            nj = t[1] + dj[i]
            if 0 <= ni < N and 0 <= nj < N \
                and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = visited[t[0]][t[1]] + 1
                if maze[ni][nj] == 3:
                    return visited[ni][nj] - 2
    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    li = [list(map(int, input())) for _ in range(N)]

    start = 0
    for i in range(N):
        for j in range(N):
            if li[i][j] == 2:
                start = [i, j]
                break
        if start: break

    print(f'#{tc} {bfs(li, start, N)}')