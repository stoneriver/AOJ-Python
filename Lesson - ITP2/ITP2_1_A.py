q = int(input())
A = []
for i in range(q):
    query = [int(i) for i in input().split()]
    if query[0] == 0:
        A.append(query[1])
    elif query[0] == 1:
        print(A[query[1]])
    elif query[0] == 2:
        A.pop(len(A)-1)
