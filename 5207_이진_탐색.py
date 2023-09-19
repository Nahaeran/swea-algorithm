def binary_search(arr, p):
    left, right = 0, len(arr) - 1
    before = 'none'

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == p:
            return 1
        elif arr[mid] > p:
            right = mid - 1
            if before == 'left':
                return 0
            before = 'left'
        else:
            left = mid + 1
            if before == 'right':
                return 0
            before = 'right'

    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    ai.sort()
    result = 0

    for b in bi:
        if binary_search(ai, b):
            result += 1

    print(f'#{tc} {result}')