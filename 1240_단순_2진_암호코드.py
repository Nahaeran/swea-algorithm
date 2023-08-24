rule = {
    '0001101' : '0',
    '0011001' : '1',
    '0010011' : '2',
    '0111101' : '3',
    '0100011' : '4',
    '0110001' : '5',
    '0101111' : '6',
    '0111011' : '7',
    '0110111' : '8',
    '0001011' : '9'
}


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    codes = [input().strip('0') for _ in range(N)]
    for c in codes:
        if c != '':
            length = 56 - len(c)
            code = '0' * length + c
            break

    password = ''
    for i in range(0, 56, 7):
        code_bit = code[i:i + 7]
        password += rule[code_bit]

    num = 0
    sum_odd = 0
    sum_all = 0
    for i in range(8):
        if i % 2 == 0:
            sum_odd += int(password[i])
        else:
            num += int(password[i])
        sum_all += int(password[i])
    num += sum_odd * 3

    if num % 10 == 0:
        print(f'#{tc} {sum_all}')
    else:
        print(f'#{tc} 0')