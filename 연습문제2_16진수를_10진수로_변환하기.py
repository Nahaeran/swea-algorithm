def change_to_bin(num):
    num_2 = ''
    for n in num:
        n_10 = int(n, 16)
        n_2 = str(bin(n_10))[2:]
        length = 4 - len(n_2)
        num_2 += '0' * length + n_2
    return num_2


T = int(input())

for tc in range(1, T + 1):
    num_16 = input()
    num_2 = change_to_bin(num_16)

    result = []
    for i in range(0, len(num_2), 7):
        if len(num_2) - i >= 7:
            result.append(int(num_2[i:i + 7], 2))
        else:
            result.append(int(num_2[i:], 2))
    print(f'#{tc}', *result)