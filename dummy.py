dp = [-1, 1,1,1,2,2,3,4,5,7,9]

for i in range(11, 101):
    dp.append(dp[i-1]+dp[i-5])

for _ in range(int(input())):
    print(dp[int(input())])
