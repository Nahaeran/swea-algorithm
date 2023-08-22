def preorder(node):
    global V
    if 0 < node <= V:
        print(node, end=" ")
        if node != V:
            preorder(c1[node])
            preorder(c2[node])


V = int(input())
input_list = list(map(int, input().split()))

c1 = [0] * V
c2 = [0] * V

for i in range(0, len(input_list), 2):
    p, c = input_list[i], input_list[i + 1]
    if not c1[p]:
        c1[p] = c
    else:
        c2[p] = c

preorder(1)