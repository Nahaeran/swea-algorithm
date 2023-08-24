T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bits = ''
    result = []
    for _ in range(N):
        bit = input()
        bits += bit
    for i in range(0, len(bits), 7):
        bit = bits[i:i + 7]
        result.append(int(bit, 2))
    print(f'#{tc}', *result)