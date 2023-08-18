V, E = map(int, input().split())
input_edge = list(map(int, input().split()))
edges = [[] for _ in range(V + 1)]
for i in range(0, 2*E, 2):
    s, e = input_edge[i], input_edge[i + 1]
    edges[s].append(e)
    edges[e].append(s)

visited = [0] * (V + 1)
queue = [0] * (V + 1)
front = rear = -1

rear += 1
queue[rear] = 1
visited[1] = 1
while front != rear:
    front += 1
    t = queue[front]
    for adj_v in edges[t]:
        if visited[adj_v] == 0:
            rear += 1
            queue[rear] = adj_v
            visited[adj_v] = 1

print('#1', *queue[:V])