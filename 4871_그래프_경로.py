def dfs(v, end):
    top = 0
    stack[top] = v
    visited[v] = 1

    while top != -1:
        for i in range(1, V+1):
            if adj[v][i] == 1 and i == end:
                return 1
            elif adj[v][i] == 1 and visited[i] == 0:
                v = i
                visited[v] = 1

                top += 1
                stack[top] = v
                break
        else:
            top -= 1
            v = stack[top]
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj[v1][v2] = 1

    S, G = map(int, input().split())

    stack = [0] * (V+1)
    visited = [0] * (V+1)

    print(f'#{tc} {dfs(S, G)}')