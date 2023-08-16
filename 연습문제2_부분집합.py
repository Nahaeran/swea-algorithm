def f(i, N, s, t):
    global cnt
    if s == t:
        cnt += 1
        return
    elif i == N:
        return
    elif s > t:
        return
    else:
        bit[i] = 1
        f(i + 1, N, s + A[i], t)
        bit[i] = 0
        f(i + 1, N, s, t)
        return


cnt = 0
A = list(map(int, input().split()))
bit = [0] * 10
f(0, 10, 0, 10)
print(f'#1 {cnt}')