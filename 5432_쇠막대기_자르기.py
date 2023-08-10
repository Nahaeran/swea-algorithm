T = int(input())

for tc in range(1, T+1):
    parenthesis = input()
    result = 0

    floor = 0
    laser = 0
    for i in range(len(parenthesis) - 1):
        if parenthesis[i] == '(':
            if parenthesis[i + 1] == '(':
                floor += 1
            else:
                laser = 1
            if laser:
                result += floor
                laser = 0
        else:
            if parenthesis[i + 1] == ')':
                floor -= 1
                result += 1

    print(f'#{tc} {result}')