def my_fnc(my_list, type):
    result = my_list[0]
    idx_result = 0
    for idx, e in enumerate(my_list):
        if type == "max":
            if result < e:
                idx_result = idx
                result = e
        elif type == "min":
            if result > e:
                idx_result = idx
                result = e
    return idx_result

for tc in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))
    gap = 0

    max_idx = my_fnc(li, "max")
    min_idx= my_fnc(li, "min")
    for _ in range(N):
        li[max_idx] -= 1
        li[min_idx] += 1
        max_idx = my_fnc(li, "max")
        min_idx = my_fnc(li, "min")

    gap = li[max_idx] - li[min_idx]

    print(f'#{tc} {gap}')