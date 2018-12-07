from __future__ import division

from math import sqrt


def dist(x1, y1, x2, y2):
    return sqrt(sq(x2 - x1) + sq(y2 - y1))


def sq(x1):
    return x1 * x1


x = 0
y = 0
circle = 0
total = 0
width = 1000
pi = 0

if __name__ == '__main__':

    while y <= width:
        x += 1
        if x >= width:
            x = 0
            y += 1

        d = dist(x, y, width / 2, width / 2)
        if d < width / 2:
            circle += 1

        total += 1
        pi = 4 * (circle / total)

    print(pi)
