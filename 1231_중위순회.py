def inorder(idx):
    global N
    if 0 < idx <= N:
        inorder(2 * idx)
        result.append(tree[idx])
        inorder(2 * idx + 1)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)

    for _ in range(N):
        temp = list(input().split())
        if len(temp) == 4:
            num, data, left, right = temp
        elif len(temp) == 3:
            num, data, left = temp
        else:
            num, data = temp
        num = int(num)
        tree[num] = data

    result = []
    inorder(1)
    print(f'#{tc} {"".join(result)}')


