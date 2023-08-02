def add_canvas(arr, matrix):
    r1, c1, r2, c2 = arr[:4]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            matrix[i][j] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    canvas = [[0] * 10 for _ in range(10)]

    for area in li:
        add_canvas(area, canvas)

    result = 0
    for row in canvas:
        result += row.count(2)
    print(f'#{tc} {result}')