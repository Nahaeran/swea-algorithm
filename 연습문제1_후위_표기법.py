op = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}


def make_postfix(infix):
    stack = []
    postfix = ''

    for e in infix:
        if e.isdigit():
            postfix += e
        else:
            if stack and op[e] <= op[stack[-1]]:
                postfix += stack.pop()
            stack.append(e)
    while stack:
        postfix += stack.pop()

    return postfix


T = int(input())

for tc in range(1, T+1):
    infix = list(input())
    print(f'#{tc} {make_postfix(infix)}')