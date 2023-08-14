def calculate(arr):
    stack = [0] * len(arr)
    top = -1

    for e in arr:
        if e == '.':
            if top == 0:
                return stack[top]
            else:
                return 'error'
        elif type(e) == int:
            top += 1
            stack[top] = e
        else:
            e2 = stack[top]
            top -= 1
            e1 = stack[top]
            top -= 1
            if e == '+':
                top += 1
                stack[top] = e1 + e2
            elif e == '-':
                top += 1
                stack[top] = e1 - e2
            elif e == '*':
                top += 1
                stack[top] = e1 * e2
            elif e == '/':
                top += 1
                stack[top] = e1 // e2


T = int(input())

for tc in range(1, T+1):
    postfix = list(input().split())
    for i in range(len(postfix)):
        try:
            postfix[i] = int(postfix[i])
        except:
            pass

    print(f'#{tc} {calculate(postfix)}')

