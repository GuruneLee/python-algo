# 14:45 x(내힘으로 못품)

# 2,3,5만을 소인수로 가진 합성수, 1은 못생긴 수
# n번째 못수는 뭘까

n = int(input())

# dp[i] : i번째 못생긴 수
# ti, thi, fi => 각각 2,3,5를 아직 곱하지 않은 최소 못생긴 수의 인덱스
# (모든 못생긴 수는 더 작은 못생긴수x2또는3또는5 이다 )
# dp[i] = min(
#     
# )
dp = [1]
ti, thi, fi = 0,0,0
for i in range(1, n):
    dp.append(min(dp[ti]*2, dp[thi]*3, dp[fi]*5))
    if dp[i]==dp[ti]*2:
        ti+=1
    if dp[i]==dp[thi]*3:
        thi+=1
    if dp[i]==dp[fi]*5:
        fi+=1
print(dp[-1])