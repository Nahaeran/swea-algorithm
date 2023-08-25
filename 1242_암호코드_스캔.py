rule = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}


def remove_dup(arr):
    new = []
    for i in range(len(arr)):
        if arr[i] not in new:
            new.append(arr[i])
    return new


T = int(input().strip())

for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    input_codes = [input().strip().strip('0') for _ in range(N)]
    codes = []
    for c in input_codes:
        if c != '':
            codes.append(c)
    codes = remove_dup(codes)

    for i in range(len(codes)):
        temp = codes[i]
        for j in range(len(codes)):
            if len(temp) < len(codes[j]):
                codes[j] = codes[j].replace(temp, '').strip('0')
    for i in range(len(codes) - 1, -1, -1):
        temp = codes[i]
        for j in range(len(codes)):
            if len(temp) < len(codes[j]):
                codes[j] = codes[j].replace(temp, '').strip('0')
    codes = remove_dup(codes)
    for i in range(len(codes)):
        temp = codes[i]
        if temp[len(temp) // 2 - 2:len(temp) // 2 + 2] == '0000':
            temp1 = temp[:len(temp) // 2].strip('0')
            temp2 = temp[len(temp) // 2:].strip('0')
            codes.append(temp1)
            codes.append(temp2)
            codes.pop(i)
    codes = remove_dup(codes)

    code_10 = list(map(lambda x: int(x, 16), codes))
    code_2 = list(map(lambda x: str(bin(x))[2:], code_10))

    result = 0
    for code in code_2:
        last = len(code) - 1
        while code[last] == '0':
            last -= 1
        code = code[:last + 1]
        s = len(code) // 56
        r = len(code) % 56

        if r:
            s += 1
        length = 56 * s - len(code)
        code = '0' * length + code
        if s != 1:
            perfect_code = ''
            for i in range(0, len(code), s):
                perfect_code += code[i]
        else:
            perfect_code = code
        try:
            password = ''
            for i in range(0, 56, 7):
                code_bit = perfect_code[i:i + 7]
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
                result += sum_all
        except KeyError:
            pass
    print(f'#{tc} {result}')