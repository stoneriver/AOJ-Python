q = int(input())
A = []
for i in range(q):
    query = [int(i) for i in input().split()]
    if query[0] == 0 and query[1] == 0:
        # A.insert(0, query[2])
        A = [query[2]] + A
    elif query[0] == 0 and query[1] == 1:
        # 
        A = A + [query[2]]
    elif query[0] == 1:
        print(A[query[1]])
    elif query[0] == 2 and query[1] == 0:
        # A.pop(0)
        A = A[1:len(A)]
    elif query[0] == 2 and query[1] == 1:
        # A.pop(len(A)-1)
        A = A[0:len(A)-1]