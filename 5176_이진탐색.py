def inorder(idx):
    if 0 < idx <= N:
        inorder(idx * 2)
        tree[idx] = li.pop(0)
        inorder(idx * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    li = list(range(1, N + 1))

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
