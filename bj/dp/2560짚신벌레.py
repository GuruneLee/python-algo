a,b,d,n = list(map(int, input().split()))

dp = [1] # i번째 날에 새로 태어난 벌레의 수
sex = 0 # 생식 가능 벌레 수
re = 1 # 현재 벌레 수
# dp를 계산하며 생식가능한 벌레의 수와 현재 벌레의 수를 함께 구해 나간다
# https://nnnlog.tistory.com/66 
for i in range(1,n+1):
    if i>=b:
        sex -= dp[i-b]
    if i>=a:
        sex += dp[i-a]
    dp.append(sex%1000)
    re += dp[i]
    if i>= d:
        re -= dp[i-d]
print(re%1000)