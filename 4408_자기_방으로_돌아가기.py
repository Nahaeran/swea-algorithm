T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [(0, 0)] * N
    for n in range(N):
        s, e = map(int, input().split())
        start = (s - 1) // 2
        end = (e - 1) // 2
        if start > end:
            start, end = end, start
        arr[n] = (start, end)
    paths = [[(-1, -1)]]
    arr.sort()
    for i in range(N):
        now = arr[i]
        for path in paths:
            if path[-1][1] < now[0]:
                path.append(now)
                break
        else:
            paths.append([now])
    print(f"#{tc} {len(paths)}")