T = int(input())


def quickSort(arr, L, R):
    left = L
    right = R
    pivot = arr[(left + right) // 2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    if L < right:
        quickSort(arr, L, right)
    if left < R:
        quickSort(arr, left, R)


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    li = []
    for line in arr:
        li.extend(line)
    quickSort(li, 0, N * N - 1)

    di = []
    dj = []
    for n in range(N, 0, -1):
        for _ in range(n):
            di.append(0)
            dj.append(1 - 2 * ((N - n) % 2))
        for _ in range(n - 1):
            di.append(1 - 2 * ((N - n) % 2))
            dj.append(0)

    i = j = 0
    for e in range(1, N * N + 1):
        arr[i][j] = li[e - 1]
        if e != N * N:
            i += di[e]
            j += dj[e]
    print(f'# {tc}')
    for line in arr:
        print(*line)