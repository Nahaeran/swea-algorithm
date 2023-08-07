T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    if len(str1) > len(str2):
        long = str1
        short = str2
    else:
        long = str2
        short = str1

    result = 0
    for i in range(len(long) - len(short) + 1):
        if long[i:i+len(short)] == short:
            result = 1

    print(f'#{tc} {result}')