T = int(input())
start_list = [0] * 100000
last_list = [0] * 100000
for tc in range(1, T + 1):
    L = int(input())
    N = int(input())

    for i in range(N):
        start_list[i], last_list[i] = map(int, input().split())

    result = 0
    start = 1
    end = L

    while start <= end:
        mid = (start + end) // 2

        first = last = 0
        peak_time = 0
        total_time = 0

        while True:
            if peak_time + (last_list[last] - start_list[last]) >= mid:
                if total_time + (mid - peak_time) <= L:
                    is_mid_min = True
                    break
                else:
                    peak_time -= last_list[first] - start_list[first]
                    total_time -= start_list[first + 1] - start_list[first]
                    first += 1
            else:
                if last == N - 1:
                    is_mid_min = False
                    break
                peak_time += last_list[last] - start_list[last]
                total_time += start_list[last + 1] - start_list[last]
                last += 1

        if is_mid_min:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(f'#{tc} {result}')
