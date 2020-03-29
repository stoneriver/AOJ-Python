# 全探索 Exhaustive search
# 多分動的計画法使ったら早く計算できると思う（こなみ）

def solve(i, m):
    if m == 0:
        return True
    elif i >= n:
        return False
    else:
        return solve(i + 1, m) or solve(i + 1, m - A[i])


n = int(input())
A = [int(i) for i in input().split()]
q = int(input())
for m in (int(i) for i in input().split()):
    if solve(0, m):
        print("yes")
    else:
        print("no")