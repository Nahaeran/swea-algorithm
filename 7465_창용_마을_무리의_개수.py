def find_set(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y: return
    p[max(x, y)] = min(x, y)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p = list(range(N + 1))
    for _ in range(M):
        f, t = map(int, input().split())
        union(f, t)
    p = list(map(find_set, p))
    print(f'#{tc} {len(set(p) - {0})}')