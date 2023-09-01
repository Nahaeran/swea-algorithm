def find_max(N):
    max_result = 0
    count = 1
    now = times[0]
    for t in range(N):
        if now[1] <= times[t][0]:
            count += 1
            now = times[t]
    if max_result < count:
        max_result = count
    return max_result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    times = [0] * N
    for i in range(N):
        s, e = map(int, input().split())
        times[i] = [s, e]

    times.sort(key = lambda x: x[1])

    print(f'#{tc} {find_max(N)}')