def preorder_count(node):
    global result
    if 0 < node <= E + 2:
        result += 1
        if node != E + 2:
            preorder_count(c1[node])
            preorder_count(c2[node])


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    input_list = list(map(int, input().split()))

    c1 = [0] * (E + 2)
    c2 = [0] * (E + 2)

    for i in range(0, 2 * E, 2):
        p, c = input_list[i], input_list[i + 1]
        if not c1[p]:
            c1[p] = c
        else:
            c2[p] = c

    result = 0
    preorder_count(N)
    print(f'#{tc} {result}')