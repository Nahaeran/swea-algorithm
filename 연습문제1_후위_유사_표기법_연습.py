def make_postfix(infix):
    stack = [0] * len(infix)
    top = -1
    postfix = ''

    for e in infix:
        if e not in '+-*/':
            postfix += e
        else:
            top += 1
            stack[top] = e

    while top != -1:
        postfix += stack[top]
        top -= 1

    return postfix


T = int(input())

for tc in range(1, T+1):
    infix = list(input())
    print(f'#{tc} {make_postfix(infix)}')