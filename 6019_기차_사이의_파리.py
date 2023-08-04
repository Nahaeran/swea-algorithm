T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 간단
    # distance = D / (A + B) * F
    # print(f'#{tc} {distance}')
    t1 = D / (B + F)
    a1 = F * t1
    a_point1 = a1 * A / F
    b_point1 = D - B * t1
    r = (b_point1 - a_point1) / D
    inf_sum = a1 / (1 - r)
    print(f'#{tc} {inf_sum}')

# 실행속도 거의 1/7
# ans=[]
# T=int(input())
# for t in range(1,T+1):
#     d,a,b,f=map(int,input().split())
#     res=d/(a+b)*f
#     ans.append(f"#{t} {res}")
# for a in ans:
#     print(a)

