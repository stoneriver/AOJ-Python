# Dictionary ハッシュ
class Dictionary():

    def __init__(self, size):
        self.dict = [False for i in range(size)]
    
    def insert(self, dataindex):
        self.dict[dataindex] = True
    
    def find(self, dataindex):
        return self.dict[dataindex]


def getIndexOf(data):
    index = 0;
    for i in range(0, len(data)):
        if data[-1 - i] == 'A':
            index += 4 ** i * 1
        elif data[-1 - i] == 'C':
            index += 4 ** i * 2
        elif data[-1 - i] == 'G':
            index += 4 ** i * 3
        elif data[-1 - i] == 'T':
            index += 4 ** i * 4
    return index
        

n = int(input())
Dict = Dictionary(4 ** 12)
for i in range(n):
    cmd, str = input().split()
    if cmd == "insert":
        Dict.insert(getIndexOf(str))
    elif cmd == "find":
        if Dict.find(getIndexOf(str)):
            print("yes")
        else:
            print("no")