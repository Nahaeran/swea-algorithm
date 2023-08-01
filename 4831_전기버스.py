T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    li = list(map(int, input().split()))

    now = 0
    idx = -1
    charge_num = 0
    while now + K < N:
        if now + K in li:
            now += K
            idx = li.index(now)
            charge_num += 1
        elif now+K > li[idx + 1]:
            idx += 1
            now = li[idx]
            charge_num += 1
        else:
            charge_num = 0
            break
    print(f'#{tc} {charge_num}')