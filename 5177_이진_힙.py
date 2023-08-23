def enq(heap, e):
    global last
    last += 1
    idx = last
    heap[idx] = e
    while e < heap[idx // 2]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        idx //= 2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    li = list(map(int, input().split()))

    min_heap = [0] * (N + 1)
    last = 0

    for e in li:
        enq(min_heap, e)

    result = 0
    while last != 0:
        last //= 2
        result += min_heap[last]

    print(f'#{tc} {result}')