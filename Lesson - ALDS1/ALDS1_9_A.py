# 完全二分木  Complete binary tree

H = int(input())
T = [-1] + [int(i) for i in input().split()]

for i in range(1, H+1):
    print("node ", i, ": ", sep="", end="")
    print("key = ", T[i], ", ", sep="", end="")
    if i != 1:
        print("parent key = ", T[i // 2], ", ", sep="", end="")
    if 2 * i <= H:
        print("left key = ", T[2 * i], ", ", sep="", end="")
    if 2 * i + 1 <= H:
        print("right key = ", T[2 * i + 1], ", ", sep="", end="")
    print()
