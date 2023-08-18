di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def find_path_with_bfs(maze, v):
    visited = [[0] * 100 for _ in range(100)]
    queue = [v]
    visited[v[0]][v[1]] = 1
    while queue:
        t = queue.pop(0)
        for i in range(4):
            ni = t[0] + di[i]
            nj = t[1] + dj[i]
            if 0 <= ni < 100 and 0 <= nj < 100 \
                    and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if maze[ni][nj] == 3:
                    return 1
                queue.append([ni, nj])
                visited[ni][nj] = 1
    return 0


for tc in range(1, 11):
    tc = int(input())
    li = [list(map(int, input())) for _ in range(100)]
    start = 0

    for i in range(100):
        for j in range(100):
            if li[i][j] == 2:
                start = [i, j]
                break
        if start: break
    print(f'#{tc} {find_path_with_bfs(li, start)}')