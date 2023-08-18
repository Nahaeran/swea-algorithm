def bfs(adj_l, S):
    visited = [0] * 101
    queue = [S]
    visited[S] = 1

    while queue:
        t = queue.pop(0)

        for v in adj_l[t]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = visited[t] + 1

    max_t = max(visited)
    for n in range(101):
        if visited[n] == max_t:
            max_n = n

    return max_n


for tc in range(1, 11):
    N, S = map(int, input().split())
    input_edges = list(map(int, input().split()))
    edges = [set() for _ in range(101)]

    for i in range(0, N, 2):
        f, t = input_edges[i], input_edges[i + 1]
        edges[f].add(t)

    print(f'#{tc} {bfs(edges, S)}')
