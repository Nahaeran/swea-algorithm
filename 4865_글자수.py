T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    counts = {}

    for e in str1:
        cnt = counts.setdefault(e, 0)

    keys = counts.keys()
    for s in str2:
        if s in keys:
            counts[s] += 1

    values = list(counts.values())
    max_value = values[0]
    for value in values:
        if max_value < value:
            max_value = value
    print(f'#{tc} {max_value}')