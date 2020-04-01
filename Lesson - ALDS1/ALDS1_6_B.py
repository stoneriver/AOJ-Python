# Partition パーティション


def partition(A, p, r):
    i = p - 1
    x = A[r]
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            t = A[j]
            A[j] = A[i]
            A[i] = t
    A[r] = A[i + 1]
    A[i + 1] = x
    return i + 1


n = int(input())
A = [int(i) for i in input().split()]
par = partition(A, 0, n - 1)
for i in range(0, par):
    print(A[i], end=" ")
print("[", A[par], "]", sep="", end=" ")
for i in range(par + 1, n - 1):
    print(A[i], end=" ")
print(A[n - 1])
