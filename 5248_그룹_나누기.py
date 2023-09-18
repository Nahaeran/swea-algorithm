def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        p[y] = x
    else:
        p[x] = y


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    p = list(range(N + 1))

    for k in range(0, M * 2, 2):
        x = number[k]
        y = number[k + 1]
        union(x, y)
    # result = 0
    # temp = []
    # for i in range(1, N + 1):
    #     if find_set(i) not in temp:
    #         temp.append(find_set(i))
    #         result += 1
    # print(f'#{tc} {result}')
    p = list(map(find_set, p))
    p = set(p) - {0}

    print(f'#{tc} {len(p)}')
