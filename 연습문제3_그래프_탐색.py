def dfs(v):
    global top
    visited[v] = 1
    top += 1
    stack[top] = v
    path = [v]

    while top != -1:
        for i in range(V+1):
            if adj[v][i] == 1 and visited[i] == 0:
                v = i
                visited[v] = 1
                path.append(v)

                top += 1
                stack[top] = v
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break
    return path


V, E = map(int, input().split())
input_li = list(map(int, input().split()))

visited = [0] * (V+1)
stack = [0] * V
top = -1

adj = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(0, len(input_li), 2):
    v1, v2 = input_li[i:i + 2]
    adj[v1][v2], adj[v2][v1] = 1, 1

result = map(str, dfs(1))
print(f'#1 {"-".join(result)}')