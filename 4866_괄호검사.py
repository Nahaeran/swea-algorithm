def parentheses_test(string):
    stack = []

    for s in string:
        if s == '(' or s == '{':
            stack.append(s)
        elif s == ')':
            if stack[-1] != '(':
                return 0
            stack.pop()
        elif s == '}':
            if stack[-1] != '{':
                return 0
            stack.pop()

    if stack:
        return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    str1 = input()

    result = parentheses_test(str1)
    print(f'#{tc} {result}')
