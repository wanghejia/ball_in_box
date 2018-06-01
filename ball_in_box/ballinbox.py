import math
import random
import validate as vl

__all__ = ['ball_in_box']

def get_r(x,y,blockers,circles):
    r = 1 - x
    if r>(1 - y):
        r = 1 - y
    if r>(x + 1):
        r = x + 1
    if r>(y + 1):
        r = y + 1
    for blocker in blockers:
        x1 = blocker[0]
        y1 = blocker[1]
        r1 = ((x1-x)**2+(y1-y)**2)**0.5
        if r>r1:
            r = r1
    for circle in circles:
        x2 = circle[0]
        y2 = circle[1]
        r2 = circle[2]
        r3 = ((x2-x)**2+(y2-y)**2)**0.5 - r2
        if r>r3:
            r = r3
    circles2 = circles + [(x,y,0)]
    return r

def judge(x,y,circles):
    for circle in circles:
        x1 = circle[0]
        y1 = circle[1]
        r = circle[2]
        rr = ((x1-x)**2+(y1-y)**2)**0.5
        if rr<r:
            return False
    return True


def ball_in_box(m, blockers):
    circles = []
    i = 0
    while i<m:
        x = random.random()*2 - 1
        y = random.random()*2 - 1
        while not judge(x,y,circles):
            x = random.random()*2 - 1
            y = random.random()*2 - 1
        r = get_r(x,y,blockers,circles)
        circles.append((x,y,r))
        i += 1
    return circles
