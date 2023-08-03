T = int(input())
def binarySearchCounting(N, key):
    start = 1
    end = N
    count = 0
    while start <= end:
        mid = (start + end) // 2
        count += 1
        if mid == key:
            return count
        elif mid > key:
            end = mid - 1
        else:
            start = mid + 1

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    count_a = binarySearchCounting(P, Pa)
    count_b = binarySearchCounting(P, Pb)
    if count_a < count_b:
        vic = 'A'
    elif count_a > count_b:
        vic = 'B'
    else:
        vic = 0

    print(f'#{tc} {vic}')
