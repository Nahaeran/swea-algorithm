import heapq
T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(E)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    INF = float('inf')
    dist = [INF] * (N + 1)

    hq = []
    heapq.heappush(hq, (0, 0))
    dist[0] = 0

    while hq:
        w, now = heapq.heappop(hq)

        if dist[now] < w:
            continue

        for next in graph[now]:
            new_cost = w + next[1]

            if dist[next[0]] <= new_cost:
                continue

            dist[next[0]] = new_cost
            heapq.heappush(hq, (new_cost, next[0]))

    print(f'#{tc} {dist[-1]}')