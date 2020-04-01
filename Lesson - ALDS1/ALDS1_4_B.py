# Binary search 二分検索
def binarySearch(A, n, k):
    left = 0
    right = n
    while left < right:
        mid = int((left + right) / 2)
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            right = mid + 1
        elif A[mid] < k:
            left = mid
    return -1


n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]
C = 0
for t in T:
    if binarySearch(S, n, t) != -1:
        C += 1
print(C)
