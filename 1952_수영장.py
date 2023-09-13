def swim(month, cost):
    global result
    if month >= 12:
        if result > cost:
            result = cost
    else:
        swim(month + 1, cost + plans[month] * d)
        swim(month + 1, cost + m)
        swim(month + 3, cost + q)


T = int(input())

for tc in range(1, T + 1):
    d, m, q, y = map(int, input().split())
    plans = list(map(int, input().split()))

    result = y
    swim(0, 0)

    print(f'#{tc} {result}')