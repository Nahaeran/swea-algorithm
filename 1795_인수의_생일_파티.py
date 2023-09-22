import heapq
INF = float('inf')


def dijkstra(start, end):
    hq = []
    dist = [INF] * (N + 1)
    heapq.heappush(hq, (0, start))
    dist[start] = 0

    while hq:
        w, now = heapq.heappop(hq)
        if dist[now] < w:
            continue
        for next in adj_list[now]:
            if next[1] + w >= dist[next[0]]:
                continue
            dist[next[0]] = next[1] + w
            heapq.heappush(hq, (dist[next[0]], next[0]))
    if end == -1:
        return dist
    else:
        return dist[X]


T = int(input())

for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        f, t, w = map(int, input().split())
        adj_list[f].append((t, w))

    fromInsu_dist = dijkstra(X, -1)
    result = 0
    for i in range(1, N + 1):
        temp = fromInsu_dist[i] + dijkstra(i, X)
        result = max(result, temp)

    print(f'#{tc} {result}')