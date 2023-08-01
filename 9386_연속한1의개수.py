T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    count = max_cnt = 0
    for e in arr:
        if e:
            count += 1
        else:
            count = 0
        if count > max_cnt:
            max_cnt = count
    print(f'#{tc} {max_cnt}')