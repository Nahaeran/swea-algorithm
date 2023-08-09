def parentheses_test(string):
    stack = []

    try:
        for s in string:
            if s == '(':
                stack.append(s)
            elif s == ')':
                if stack[-1] != '(':
                    return -1
                stack.pop()

        if stack:
            return -1
        return 1
    except:
        return -1


T = int(input())
for tc in range(1, T+1):
    str1 = input()

    result = parentheses_test(str1)
    print(f'#{tc} {result}')