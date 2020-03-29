# Doubly linked list連結リスト
# AOJではTLEで不正解になった。そんなにひどくオーバーしてるわけ無いと思うけどな…
# C/C++で書き直したらワンチ使えるかもしれないのでこのまま放置。今はPythonを使いたいのだ。

from _ast import If


class Node():

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def getData(self):
        return self.data

    def getPrev(self):
        return self.prev
    
    def getNext(self):
        return self.next
    
    def setPrev(self, newprev):
        self.prev = newprev
    
    def setNext(self, newnext):
        self.next = newnext
    
    def deleteSelf(self):
        self.next.setPrev(self.prev)
        self.prev.setNext(self.next)
        del(self)
    
    def __repr__(self):
        if self.data == None:
            return "NIL NODE"
        else:
            return self.data


class List():

    def __init__(self):
        self.nil = Node(None, None, None)
        self.nil.setNext(self.nil)
        self.nil.setPrev(self.nil)
    
    def getFirst(self):
        return self.nil.getPrev()
    
    def getLast(self):
        return self.nil.getNext()
    
    def insert(self, x):
        new = Node(x, self.getFirst(), self.nil)
        self.getFirst().setNext(new)
        self.nil.setPrev(new)
    
    def delete(self, x):
        scan = self.nil.getPrev()
        while True:
            if scan.getData() == x:
                scan.deleteSelf()
                break
            scan = scan.getPrev()
            if scan == self.nil:
                break

    def deleteFirst(self):
        self.nil.getPrev().deleteSelf()

    def deleteLast(self):
        self.nil.getNext().deleteSelf()


n = int(input())
L = List()
for i in range(n):
    cmd = (input().split())
    if cmd[0] == "insert":
        L.insert(cmd[1])
    elif cmd[0] == "delete":
        L.delete(cmd[1])
    elif cmd[0] == "deleteFirst":
        L.deleteFirst()
    elif cmd[0] == "deleteLast":
        L.deleteLast()
scan = L.nil
while True:
    scan = scan.getPrev()
    if scan.getPrev() == L.nil:
        print(scan.getData())
        break
    else:
        print(scan.getData(), end=" ")
