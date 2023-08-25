rule = {
    '001101' : 0,
    '010011' : 1,
    '111011' : 2,
    '110001' : 3,
    '100011' : 4,
    '110111' : 5,
    '001011' : 6,
    '111101' : 7,
    '011001' : 8,
    '101111' : 9
}


def change_to_bin(num):
    num_2 = ''
    for n in num:
        n_10 = int(n, 16)
        n_2 = str(bin(n_10))[2:]
        length = 4 - len(n_2)
        num_2 += '0' * length + n_2
    return num_2


T = int(input().strip())

for tc in range(1, T + 1):
    num_16 = input().strip()
    num_2 = change_to_bin(num_16)

    for i in range(len(num_2) - 1, -1, -1):
        if num_2[i] == '1':
            idx = i
            break

    result = []
    while idx >= 5:
        temp = num_2[idx - 5:idx + 1]
        result.append(rule[temp])
        idx -= 6

    print(f'#{tc}', *result[::-1])