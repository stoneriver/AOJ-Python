# Rooted tree 根付き木の表現


class Node():

    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1


def setdt(id, p, Dp, Tp, T):
    Dp[id] = p  # 自身のdepthの処理
    if T[id].right != -1:
        setdt(T[id].right, p, Dp, Tp, T)  # 兄弟のdepthの処理
    if T[id].left != -1:
        setdt(T[id].left, p + 1, Dp, Tp, T)  # 子のdepthの処理
        Tp[id] = "internal node"  # 自身のtypeの処理、子がいる場合
                                    # rootもここでinternal nodeと判定されるので関数の再帰が終わったあとに別に処理
    else:
        Tp[id] = "leaf"  # 自身のtypeの処理、子がいない場合


n = int(input())
T = [Node() for i in range(n)]
Dp = [-1 for i in range(n)]
Tp = ["" for i in range(n)]
rootid = -1

for i in range(n):
    data = [int(j) for j in input().split()]
    id, k, cids = data[0], data[1], data[2:]
    if k > 0:  # 子を持つ場合
        T[id].left = cids[0]  # 自身のleftの処理
        for j in range(k):
            T[cids[j]].parent = id  # 子らのparentの処理
        for j in range(k - 1):
            T[cids[j]].right = cids[j + 1]  # 子らのrightの処理

for i in range(n):
    if T[i].parent == -1:
        rootid = i  # rootとなるNodeの検索（ここからdepthとtypeの設定を行う）
        break

setdt(rootid, 0, Dp, Tp, T)
Tp[rootid] = "root"

for id in range(n):
    parent = T[id].parent
    type = Tp[id]
    depth = Dp[id]
    children = []
    nextchild = T[id].left
    while nextchild != -1:
        children += [nextchild]
        nextchild = T[nextchild].right
    print("node ", id, ": parent = ", parent, ", depth = ", depth, ", ", type, ", ", children, sep="")

