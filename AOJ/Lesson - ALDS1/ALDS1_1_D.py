# 比較的可読性あるやつ
n = int(input())
R = [0 for i in range(n)]
for i in range(n):
    R[i] = int(input())
minvalue = 2000000000
maxprofit = -2000000000
for i in range(1,n):
    if R[i-1] < minvalue:
        minvalue = R[i-1]
    profitnow = R[i] - minvalue
    if profitnow > maxprofit:
        maxprofit = profitnow
print(maxprofit)

# 可読性犠牲にメモリ使用量少なくしたパターン
    n = int(input())
    minvalue = int(input())
    maxprofit = -2000000000
    for i in range(1,n):
        Ri = int(input())
        maxprofit = max(Ri - minvalue, maxprofit)
        minvalue = min(minvalue, Ri)
    print(maxprofit)