def make_subset(r, c, cnt, total, benefit):
    if total > C: return
    if cnt == M:
        if max_map[r][c - M] < benefit: max_map[r][c - M] = benefit
        return
    make_subset(r, c + 1, cnt + 1, total + honey_map[r][c], benefit + honey_map[r][c] ** 2)
    make_subset(r, c + 1, cnt + 1, total, benefit)


def get_max_benefit():
    res_max = 0
    t_max_map = [col for row in max_map for col in row]
    for i in range(N ** 2):
        for j in range(i + M, N ** 2):
            res_max = max(res_max, t_max_map[i] + t_max_map[j])

    return res_max


TC = int(input())
for tc in range(1, TC + 1):
    N, M, C = map(int, input().split())
    honey_map = [list(map(int, input().split())) for _ in range(N)]
    max_map = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N - M + 1):
            make_subset(r, c, 0, 0, 0)
    print(f"#{tc} {get_max_benefit()}")
