from collections import deque

for tc in range(1, 11):
    N, s = map(int, input().split())
    input_list = list(map(int, input().split()))
    adj_list = [set() for _ in range(101)]
    max_num = max(input_list)

    for i in range(0, N, 2):
        f, t = input_list[i], input_list[i + 1]
        adj_list[f].add(t)

    queue = deque()
    queue.append(s)
    visited = [0] * (max_num + 1)
    visited[s] = 1

    while queue:
        p = queue.popleft()
        for n in adj_list[p]:
            if not visited[n]:
                queue.append(n)
                visited[n] = visited[p] + 1

    print(f'#{tc} {max_num - visited[::-1].index(max(visited))}')