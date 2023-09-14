def sort(low, high):
    if high - low < 2:
        return
    mid = (low + high) // 2
    sort(low, mid)
    sort(mid, high)
    merge(low, mid, high)


def merge(low, mid, high):
    global result
    temp = []
    l, h = low, mid

    if arr[mid - 1] > arr[high - 1]:
        result += 1

    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[h])
            h += 1

    while l < mid:
        temp.append(arr[l])
        l += 1

    while h < high:
        temp.append(arr[h])
        h += 1

    for i in range(low, high):
        arr[i] = temp[i - low]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    sort(0, N)
    print(f'#{tc} {arr[N//2]} {result}')