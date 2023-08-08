def BruteForce(A, B):
    i = 0
    j = 0
    total = 0
    while i < len(B):
        if A[j] != B[i]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == len(A):
            total += 1
            j = 0
    return total

for _ in range(10):
    tc = int(input())
    A = input()
    B = input()
    result = BruteForce(A, B)
    print(f'#{tc} {result}')