def find_prime_factor(dividend, divisor):
    factor = 0
    while dividend % divisor == 0:
        dividend //= divisor
        factor += 1
    return factor


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    a = find_prime_factor(N, 2)
    b = find_prime_factor(N, 3)
    c = find_prime_factor(N, 5)
    d = find_prime_factor(N, 7)
    e = find_prime_factor(N, 11)

    print(f'#{tc}', a, b, c, d, e)