def lcs_memoization(X, Y, m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return ""
    if X[m - 1] == Y[n - 1]:
        memo[(m, n)] = lcs_memoization(X, Y, m - 1, n - 1, memo) + X[m - 1]
        return memo[(m, n)]
    else:
        left = lcs_memoization(X, Y, m - 1, n, memo)
        right = lcs_memoization(X, Y, m, n - 1, memo)
        memo[(m, n)] = left if len(left) > len(right) else right
        return memo[(m, n)]
def lcs_tabulation(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[""] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + X[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[m][n]
