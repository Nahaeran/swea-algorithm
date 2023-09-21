import heapq

T = int(input())
INF = float('inf')

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))

    hq = []
    visited = [0] * (V + 1)
    heapq.heappush(hq, (0, 0))
    result = 0

    while hq:
        w, now = heapq.heappop(hq)
        if visited[now]:
            continue
        visited[now] = 1
        result += w

        for next in graph[now]:
            if visited[next[0]]:
                continue
            heapq.heappush(hq, (next[1], next[0]))

    print(f'#{tc} {result}')

