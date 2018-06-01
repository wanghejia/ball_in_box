import math

def validate(circles, blockers):
    # Is circle in the box?
    for circle in circles:
        xmr = circle[0] - circle[2]
        xpr = circle[0] + circle[2]
        ymr = circle[1] - circle[2]
        ypr = circle[1] + circle[2]
        if xpr>1:
            print 1
            return False
        if xmr<-1:
            print 2
            return False
        if ypr>1:
            print 3
            return False
        if ymr<-1:
            print 4
            return False
    # Is circle good for blockers?
    if blockers is not None and len(blockers) > 0:
        for circle in circles:
            for block in blockers:
                x = circle[0]
                y = circle[1]
                r = circle[2]
                bx = block[0]
                by = block[1]
                if math.sqrt((x - bx)**2 + (y - by)**2) < r:
                    print 5
                    return False

    # Is circle good for each other?
    i = len(circles)
    p = 0
    while p<i-2:
        p1 = p + 1
        while p1<i-1:
            circle1 = circles[p]
            circle2 = circles[p1]
            x1 = circle1[0]
            y1 = circle1[1]
            r1 = circle1[2]
            x2 = circle2[0]
            y2 = circle2[1]
            r2 = circle2[2]
            rr = r1 + r2
            d = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if d < rr:
                return False
            p1 += 1
        p += 1

    # all good
    return True
