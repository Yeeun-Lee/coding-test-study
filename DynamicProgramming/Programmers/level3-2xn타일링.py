def solution(n):
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        # 1000000007로 계속 나눠줘야 런타임 에러가 나지 않는다.
        dp[i] = (dp[i-1]+dp[i-2])%1000000007
    return dp[n]

result = solution(int(input()))
print(result)
