def lcs_length_no_minus(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):  # от 0 до m-1
        for j in range(n):  # от 0 до n-1
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[m][n]

print(lcs_length_no_minus("HHASJDAJSDJASJDA", "AKSDASDASKDASJFAHFKDF"))


