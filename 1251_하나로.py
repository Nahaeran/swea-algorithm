import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x_points = list(map(int, input().split()))
    y_points = list(map(int, input().split()))
    E = float(input())

    edges = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            dist = (abs(x_points[i] - x_points[j]) ** 2 + \
                    abs(y_points[i] - y_points[j]) ** 2) ** 0.5
            edges[i].append((j, dist))
            edges[j].append((i, dist))
    hq = []
    visited = [0] * N
    heapq.heappush(hq, (0, 0))
    result = 0

    while hq:
        cost, t = heapq.heappop(hq)
        if visited[t]:
            continue
        visited[t] = 1
        result += cost ** 2
        for edge in edges[t]:
            if visited[edge[0]]:
                continue
            visited[edge[0]]
            heapq.heappush(hq, (edge[1], edge[0]))

    print(f'#{tc} {int(round(result * E))}')

