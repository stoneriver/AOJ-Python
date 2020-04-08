# フィボナッチ数列 Fibonacci number

DP = [-1 for i in range(45)]
DP[0] = 1
DP[1] = 1

def fib(i):
    if DP[i] != -1:
        return DP[i]
    else:
        DP[i] = fib(i-1) + fib(i-2)
        return DP[i]

n = int(input())
print(fib(n))