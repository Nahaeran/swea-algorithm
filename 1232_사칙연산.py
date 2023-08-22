def postorder(n):
    global N
    if 0 < n <= N:
        postorder(c1[n])
        postorder(c2[n])
        postfix.append(data[n])


def calculate(post):
    stack = [post.pop(0)]
    while post:
        tmp = post.pop(0)
        if type(tmp) == int:
            stack.append(tmp)
        elif tmp == '+':
            e1 = stack.pop()
            e2 = stack.pop()
            stack.append(e1 + e2)
        elif tmp == '-':
            e2 = stack.pop()
            e1 = stack.pop()
            stack.append(e1 - e2)
        elif tmp == '*':
            e1 = stack.pop()
            e2 = stack.pop()
            stack.append(e1 * e2)
        else:
            e2 = stack.pop()
            e1 = stack.pop()
            stack.append(e1 // e2)
    return stack[0]


for tc in range(1, 11):
    N = int(input())

    data = [0] * (N + 1)
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    postfix = []

    for _ in range(N):
        temp = list(input().split())
        num = int(temp[0])
        if len(temp) == 4:
            data[num] = temp[1]
            c1[num] = int(temp[2])
            c2[num] = int(temp[3])
        else:
            data[num] = int(temp[1])

    postorder(1)
    print(f'#{tc} {calculate(postfix)}')