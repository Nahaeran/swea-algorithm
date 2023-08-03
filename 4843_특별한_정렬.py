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

def makeSpecialSort(arr):
    result = []
    for i in range(5):
        result.append(arr[-i-1])
        result.append(arr[i])
    return result

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    quickSort(li, 0, N-1)
    print(li)
    print(makeSpecialSort(li))