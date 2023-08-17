T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    pizzas = [0] * M
    for i in range(M):
        pizzas[i] = [i + 1, Ci[i]]

    in_fire = pizzas[:N]
    remain = pizzas[N:]

    while len(in_fire) > 1:
        front_pizza = in_fire.pop(0)
        front_pizza[1] //= 2
        if front_pizza[1] == 0:
            if remain:
                in_fire.append(remain.pop(0))
        else:
            in_fire.append(front_pizza)

    print(f'#{tc} {in_fire[0][0]}')