T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    li90 = list(map(list, zip(*li[::-1])))
    li180 = list(map(list, zip(*li90[::-1])))
    li270 = list(map(list, zip(*li180[::-1])))
    
    print("#"+str(test_case))
    for i in range(n):
        result=""
        for j in range(n):
            result += str(li90[i][j])
        result += " "
        for j in range(n):
            result += str(li180[i][j])
        result += " "
        for j in range(n):
            result += str(li270[i][j])
        print(result)