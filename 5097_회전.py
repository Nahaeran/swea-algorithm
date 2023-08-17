T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    for _ in range(M):
        li.append(li.pop(0))
    print(f'#{tc} {li[0]}')