# 優先順位キュー Priority queue


def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def insert(A, key):
    A += [-1]
    heapIncreaseKey(A, len(A) - 1, key)


def heapIncreaseKey(A, i, key):
    if key < A[i]:
        return
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]:
        tmp = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = tmp
        i = parent(i)


def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    largest = i
    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        maxHeapify(A, largest)


def extract(A):
    max = A[1]
    A[1] = A[len(A) - 1]
    A.pop(len(A) - 1);
    maxHeapify(A, 1)
    return max


A = [-1]
while True:
    cmd = input().split()
    if cmd[0] == "insert":
        insert(A, int(cmd[1]))
    elif cmd[0] == "extract":
        print(extract(A))
    elif cmd[0] == "end":
        break

