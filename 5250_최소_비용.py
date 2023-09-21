import heapq

T = int(input())
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
INF = float('inf')

for tc in range(1, T + 1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]

    hq = []
    heapq.heappush(hq, (0, 0, 0))
    dist[0][0] = 0

    while hq:
        h, i, j = heapq.heappop(hq)
        if dist[i][j] < h:
            continue
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                gap = max(height[ni][nj] - height[i][j], 0)
                if h + gap + 1 < dist[ni][nj]:
                    dist[ni][nj] = h + gap + 1
                    heapq.heappush(hq, (dist[ni][nj], ni, nj))

    print(f'#{tc} {dist[N - 1][N - 1]}')
