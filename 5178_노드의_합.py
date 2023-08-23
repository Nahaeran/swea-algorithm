T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        num, data = map(int, input().split())
        tree[num] = data

    for i in range(N - M, 0, -1):
        c1_idx = 2 * i
        c2_idx = 2 * i + 1
        if c1_idx <= N and c2_idx <= N:
            tree[i] = tree[c1_idx] + tree[c2_idx]
        else:
            tree[i] = tree[c1_idx]
    print(f'#{tc} {tree[L]}')