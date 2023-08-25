T = int(input())

for tc in range(1, T + 1):
    letters = [input() for _ in range(5)]
    max_length = max(map(len, letters))

    for i in range(5):
        if len(letters[i]) < max_length:
            add = max_length - len(letters[i])
            letters[i] = letters[i] + '+' * add

    result = ''
    for j in range(max_length):
        for i in range(5):
            if letters[i][j] != '+':
                result += letters[i][j]

    print(f'#{tc} {result}')