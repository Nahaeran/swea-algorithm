def check(i, j):
    a = arr[i]
    b = arr[j]
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    # 상하
    if dx == 0:
        if a[2] == 0 and b[2] == 1:
            result.append([dy, i, j])
    # 좌우
    elif dy == 0:
        if a[2] == 3 and b[2] == 2:
            result.append([dx, i, j])
    # 직각
    elif dx == dy:
        if a[2] == 0 and b[2] == 2 or a[2] == 3 and b[2] == 1:
            result.append([2 * dx, i, j])
    elif dx == -dy:
        if a[2] == 3 and b[2] == 0 or a[2] == 1 and b[2] == 2:
            result.append([2 * dx, i, j])


def emit(out):
    ans = 0
    v = [0] * N
    out.sort()
    for d, i, j in out:
        if v[i] == 0 and (v[j] == 0 or v[j] == d):
            v[i] = d
            ans += arr[i][3]
        if v[j] == 0 and (v[i] == 0 or v[i] == d):
            v[j] = d
            ans += arr[j][3]
    return ans


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    result = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            check(i, j)
    ans = 0

    print(f'#{tc} {emit(result)}')