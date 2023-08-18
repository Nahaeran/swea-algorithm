def bfs(adj_l, S, G, N):
    visited = [0] * (N + 1)
    queue = [S]
    visited[S] = 1

    while queue:
        t = queue.pop(0)

        for adj_v in adj_l[t]:
            if visited[adj_v] == 0:
                queue.append(adj_v)
                visited[adj_v] = visited[t] + 1
                if adj_v == G:
                    return visited[adj_v] - 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V + 1)]

    for _ in range(E):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(edges, S, G, V)}')
