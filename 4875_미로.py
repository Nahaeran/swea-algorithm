di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]


def is_path_in_maze(arr, start, end, N):
    stack = []
    visited = [start]

    curr = start
    while curr != end:
        for k in range(4):
            ni = curr[0] + di[k]
            nj = curr[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 3:
                    return 1
                elif not arr[ni][nj] and [ni, nj] not in visited:
                    stack.append(curr)
                    curr = [ni, nj]
                    visited.append(curr)
                    break
        else:
            if stack:
                curr = stack.pop()
            else:
                break
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if li[i][j] == 2:
                start_idx = [i, j]
            elif li[i][j] == 3:
                end_idx = [i, j]

    print(f'#{tc} {is_path_in_maze(li, start_idx, end_idx, N)}')