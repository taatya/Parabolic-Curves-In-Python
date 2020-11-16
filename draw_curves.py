# Imports
import turtle

# Defines a coordinate
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)


# Helping to make the curves
def draw_curves(pen, firstList, secondList):
    i = 0
    LenOfList = len(firstList)
    while i < LenOfList:
        pen.penup()
        pen.goto(firstList[i].x, firstList[i].y)
        pen.pendown()
        pen.goto(secondList[i].x, secondList[i].y)
        i += 1

def getCoordsForXAxis(left, right, steps, y):
    xList = []
    x = left.x
    while x <= right.x:
        xPoint = Point(x, y)
        xList.append(xPoint)
        x += steps
    return xList

def getCoordsForYAxis(bottom, top, steps, x):
    yList = []
    y = bottom.y
    while y <= top.y:
        yPoint = Point(x, y)
        yList.append(yPoint)
        y += steps
    return yList