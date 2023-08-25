for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    collision = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                di = i
                while di != N and table[di][j] != 2:
                    di += 1
                    if di != N and table[di][j] == 2:
                        collision += 1
                    elif di != N and table[di][j] == 1:
                        break

    print(f'#{tc} {collision}')