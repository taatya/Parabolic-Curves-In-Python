# Imports
import turtle

pen_speed = 10.0


# Defines a coordinate
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)


def draw_left_curves(pen, firstList, secondList):
    i = 0
    LenOfList = len(firstList)
    while i < LenOfList:
        pen.penup()
        if i != len(firstList) - 1 and len(secondList) -1:
            pen.goto(firstList[i+1].x, firstList[i].y)
            pen.pendown()
            pen.goto(secondList[i+1].x, secondList[i].y)
        else:
            pen.goto(firstList[i].x, firstList[i].y)
            pen.pendown()
            pen.goto(secondList[i].x, secondList[i].y)
        i += 1
def draw_right_curves(pen, firstList, secondList):
    i = 0
    LenOfList = len(firstList)
    while i < LenOfList:
        pen.penup()
        if i != len(firstList) - 1 and len(secondList) -1:
            pen.goto(firstList[i].x, firstList[i+1].y)
            pen.pendown()
            pen.goto(secondList[i].x, secondList[i+1].y)
        else:
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