import heapq

T = int(input())
INF = float('inf')
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    hq = []
    dist = [[INF] * N for _ in range(N)]
    heapq.heappush(hq, (0, 0, 0))
    dist[0][0] = 0
    while hq:
        cost, i, j = heapq.heappop(hq)
        if dist[i][j] < cost:
            continue
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                new_cost = cost + board[ni][nj]
                if dist[ni][nj] > new_cost:
                    dist[ni][nj] = new_cost
                    heapq.heappush(hq, (new_cost, ni, nj))
    print(f'#{tc} {dist[N - 1][N - 1]}')