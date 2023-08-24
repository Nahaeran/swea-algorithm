T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    maked = 0
    decimal = ''
    temp = -1
    while maked != N:
        if N - maked >= 2 ** temp:
            maked += 2 ** temp
            decimal += '1'
        else:
            decimal += '0'
        temp -= 1

        if temp < -13:
            decimal = 'overflow'
            break
    print(f'#{tc} {decimal}')