T = int(input())
for tc in range(1, T+1):
    string = input()

    stack = []
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)

    print(f'#{tc} {len(stack)}')