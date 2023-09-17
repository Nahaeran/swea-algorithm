from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = M - N

    queue = deque()
    queue.append(N)
    num_list = [0] * (M + 11)
    num_list[N] = 1

    while queue:
        p = queue.popleft()
        num = num_list[p]
        if p == M:
            result = num - 1
            break
        for k in (p + 1, p - 1, p * 2, p - 10):
            if -10 < k < M + 11 and not num_list[k]:
                num_list[k] = num + 1
                queue.append(k)

    print(f'#{tc} {result}')