def quick_sort(low, high):
    if high <= low:
        return
    mid = partition(low, high)
    quick_sort(low, mid - 1)
    quick_sort(mid, high)


def partition(low, high):
    pivot = arr[(low + high) // 2]
    l, r = low, high

    while l <= r:
        while arr[l] < pivot:
            l += 1
        while arr[r] > pivot:
            r -= 1
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1
    return l


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print(f'#{tc} {arr[N//2]}')
