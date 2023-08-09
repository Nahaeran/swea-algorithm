# for tc in range(1, 11):
#     N, string = input().split()
#
#     stack = []
#     for i in range(int(N)):
#         if stack and stack[-1] == string[i]:
#             stack.pop()
#         else:
#             stack.append(string[i])
#     print(f'#{tc} {"".join(stack)}')
def push(item, size):
    global top
    top += 1
    if top == size:
        print('stack overflow!!')
    else:
        stack[top] = item


def pop():
    global top
    if top == -1:
        print('stack underflow!!')
        return 0
    else:
        top -= 1
        return stack[top + 1]


for tc in range(1, 11):
    N, string = input().split()

    stack = [0] * int(N)
    top = -1
    for s in string:
        if stack and stack[top] == s:
            pop()
        else:
            push(s, int(N))
    print(f'#{tc} {"".join(stack[:top + 1])}')