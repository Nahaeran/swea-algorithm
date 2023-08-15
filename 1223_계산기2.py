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


def cal_postfix(postfix):
    stack = []

    for e in postfix:
        if e.isdigit():
            stack.append(e)
        else:
            if e == '+':
                e1 = int(stack.pop())
                e2 = int(stack.pop())
                stack.append(e1 + e2)
            elif e == '*':
                e1 = int(stack.pop())
                e2 = int(stack.pop())
                stack.append(e1 * e2)
    return stack.pop()


for tc in range(1, 11):
    N = int(input())
    infix = list(input())
    postfix = make_postfix(infix)
    result = cal_postfix(postfix)
    print(f'#{tc} {result}')