# Linear search 線形探索
def linearSearch(A, k):
    for a in A:
        if a == k:
            return True
    return False

n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]
C = 0
for t in T:
    if linearSearch(S, t):
        C += 1
print(C)