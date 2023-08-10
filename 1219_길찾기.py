def dfs(v):
    visited[v] = 1
    while not visited[99]:
        if visited[edge1[v]] == 0:
            stack.append(v)
            v = edge1[v]
            visited[v] = 1
        elif visited[edge2[v]] == 0:
            stack.append(v)
            v = edge2[v]
            visited[v] = 1
        else:
            if stack:
                v = stack.pop()
            else:
                return 0
    return 1

for tc in range(1, 11):
    tc, N = map(int, input().split())
    li = list(map(int, input().split()))

    edge1 = [0] * 100
    edge2 = [0] * 100

    for start_idx in range(0, len(li), 2):
        start_v = li[start_idx]
        end_v = li[start_idx + 1]
        if edge1[start_v] == 0:
            edge1[start_v] = end_v
        else:
            edge2[start_v] = end_v

    visited = [0] * 100
    stack = []

    result = dfs(0)
    print(f'#{tc} {result}')
