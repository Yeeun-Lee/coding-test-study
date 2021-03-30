"""
https://programmers.co.kr/learn/courses/30/lessons/43105
"""
def solution(triangle):
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0] = triangle[0]
    dp[1] = [a + dp[0][0] for a in triangle[1]]
    for k in range(1, len(triangle) - 1):
        for j in range(k + 1):
            dp[k + 1][j] = max(dp[k + 1][j], dp[k][j] + triangle[k + 1][j])
            dp[k + 1][j + 1] = max(dp[k + 1][j + 1], dp[k][j] + triangle[k + 1][j + 1])

    return max(dp[-1])