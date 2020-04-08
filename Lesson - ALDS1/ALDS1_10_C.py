# 最長共通部分列 Longest Common Subsequence problem


def lcs(X, Y):
    m = len(X)
    n = len(Y)
    c = [[-1 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        c[i][0] = 0
    for j in range(n + 1):
        c[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    return c[m][n]


q = int(input())
for i in range(q):
    A = input()
    B = input()
    print(lcs(A, B))
