for tc in range(1, 11):
    N = int(input())
    li = [list(input()) for i in range(8)]
    result = 0

    for i in range(8):
        for j in range(8 - N + 1):
            word = li[i][j:j+N]
            if word == word[::-1]:
                result += 1

    for j in range(8):
        for i in range(8 - N + 1):
            word = li[i][j]
            k = 1
            while k < N:
                word += li[i+k][j]
                k += 1
            if word == word[::-1]:
                result += 1
    print(f'#{tc} {result}')