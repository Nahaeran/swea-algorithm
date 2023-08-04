T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(Q)]
    boxes = [0] * N

    for i in range(Q):
        for j in range(li[i][0]-1, li[i][1]):
            boxes[j] = i+1
    print(f'#{tc}', *boxes)