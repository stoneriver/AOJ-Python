# シェルソート Shell sort
# アルゴリズム自体は良いんだけどWAが出る。多分Gの表示を制限していないから。わからんのでしばらくしたら解答する。

m = 2
G = [4, 1]
cnt = 0

def insertionSort(A, n, g):
    cnti = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnti = cnti + 1
        A[j+g] = v
    return cnti

def shellSort(A, n):
    cnts = 0
    for g in G:
        cnts += insertionSort(A, n, g)
    return cnts

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
cnt = shellSort(A, n)
print(m)

for i in range(m-1):
    print(G[i], end=" ")
print(G[m-1])
print(cnt)
for Ai in A:
    print(Ai)
