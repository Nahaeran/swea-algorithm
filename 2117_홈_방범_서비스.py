T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    num_all_house = sum([line.count(1) for line in board])

    result = 0
    while result != num_all_house:
        for i in range(N):
            for j in range(N):
                for k in range(1, N + 2):
                    cost = k * k + (k - 1) * (k - 1)
                    num_house = 0

                    for di in range(-k + 1, k):
                        for dj in range(- k + 1, k):
                            distance = abs(di) + abs(dj)
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < N and 0 <= nj < N and distance < k:
                                if board[ni][nj] == 1:
                                    num_house += 1

                    if cost <= num_house * M and result < num_house:
                        result = num_house
        else:
            break
    print(f'#{tc} {result}')