def get_element_pascal(n, r):
    global canvas
    if n == r or r == 0:
        e = 1
    else:
        e = canvas[n - 1][r - 1] + canvas[n - 1][r]
    return e


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    canvas = [[] for _ in range(N)]
    canvas[0].append(1)

    for n in range(1, N):
        for r in range(n+1):
            canvas[n].append(get_element_pascal(n, r))

    print(f'#{tc}')
    for line in canvas:
        print(*line)