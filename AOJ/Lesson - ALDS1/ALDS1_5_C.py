# コッホ曲線 Koch curve

import math

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x) + " " + str(self.y)


def Koch(p1, p2, n):
    if n == 0:
        print(p1)
    else:
        s = Point(p1.x * 2 / 3 + p2.x * 1 / 3, p1.y * 2 / 3 + p2.y * 1 / 3)
        u = Point(p1.x / 2 + p2.x / 2 + p1.y * r3 / 6 - p2.y * r3 / 6, p1.y / 2 + p2.y / 2 + p2.x * r3 / 6 - p1.x * r3 / 6)
        t = Point(p1.x * 1 / 3 + p2.x * 2 / 3, p1.y * 1 / 3 + p2.y * 2 / 3)
        Koch(p1, s, n - 1)
        Koch(s, u, n - 1)
        Koch(u, t, n - 1)
        Koch(t, p2, n - 1)


r3 = math.sqrt(3)
start = Point(0, 0)
goal = Point(100, 0)
n = int(input())
Koch(start, goal, n)
print(goal)
