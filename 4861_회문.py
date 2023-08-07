T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    li = [list(input()) for _ in range(N)]
    result = ""

    for i in range(N):
        for j in range(N - M + 1):
            if M % 2 == 0 and li[i][j:j + M // 2] == li[i][j + M:j + M // 2 - 1: -1]:
                result = "".join(li[i][j:j + M])
            elif li[i][j:j + M // 2] == li[i][j + M:j + M // 2: -1]:
                result = "".join(li[i][j:j + M])

    if result == "":
        li90 = list(map(list, zip(*li)))
        for i in range(N):
            for j in range(N - M + 1):
                if li90[i][j:j + M // 2] == li90[i][j + M:j + M // 2 - 1: -1]:
                    result = "".join(li90[i][j:j + M])
    print(f'#{tc} {result}')