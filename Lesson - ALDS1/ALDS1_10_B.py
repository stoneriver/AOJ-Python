# 連鎖行列積 Matrix chain multiplication

n = int(input())
p = [-1 for i in range(n + 1)]
M = [[-1 for i in range(n + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    l, m = (int(i) for i in input().split())
    p[i - 1] = l
    p[i] = m

for i in range(1, n + 1):
    M[i][i] = 0

for l in range(2, n + 1):
    for i in range(1, n - l + 2):
        j = i + l - 1
        M[i][j] = 2000000000
        for k in range(i, j):
            M[i][j] = min(M[i][j], M[i][k] + M[k + 1][j] + p[i - 1] * p[k] * p[j])

print(M[1][n])
