def bus(i, total):
    global result
    if result <= total:
        return
    if i >= N - 1:
        result = min(result, total)
        return
    for idx in range(Mi[i]):
        bus(i + idx + 1, total + 1)
    return total


T = int(input())

for tc in range(1, T + 1):
    N, *Mi = list(map(int, input().split()))
    result = N - 1
    bus(0, -1)

    print(f'#{tc} {result}')