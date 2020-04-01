# Stack スタック
class Stack():
    def __init__(self, size):
        self.A = [None for i in range(size)]
        self.i = -1  #最後に追加された要素が入っているIndex。Aが空の場合、-1
        self.size = size
    
    def push(self, x):
        self.A[self.i+1] = x
        self.i += 1
    
    def pop(self):
        ret = self.A[self.i]
        self.A[self.i] = None
        self.i -= 1
        return ret
    
    def isEmpty(self):
        return self.i == -1
    
    def isFull(self):
        return self.i == size - 1

S = Stack(100)
for i in input().split():
    if i == '+':
        s1, s2= S.pop(), S.pop()
        S.push(s2 + s1)
    elif i == '-':
        s1, s2= S.pop(), S.pop()
        S.push(s2 - s1)
    elif i == '*':
        s1, s2= S.pop(), S.pop()
        S.push(s2 * s1)
    else:
        S.push(int(i))
print(S.pop())