# Imports
import turtle

# Screen Size
screen_size = 1000.0
width = screen_size
height = screen_size
padding = 40.0
paddedWidth = width - padding
paddedHeight = height - padding

colors = ["grey", "green", "red", "blue", "pink"]


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

# Points
origin = Point(0, 0)
yMax = Point(0, paddedHeight / 2)
xMax = Point(paddedWidth/ 2, 0)
negativeXMax = Point((paddedWidth/ 2) * (-1), 0)
negativeYMax = Point(0, (paddedHeight/ 2) * (-1))
topLeft = Point(negativeXMax.x, yMax.y)
topRight = Point(xMax.x, yMax.y)
bottomLeft = Point(negativeXMax.x, negativeYMax.y)
bottomRight = Point(xMax.x, negativeYMax.y)

def setup_iteration(parts):
    # # Steps
    steps = (yMax.y - origin.y) / parts

    # Lists of Coordinates
    topLeftYList = getCoordsForYAxis(Point(negativeXMax.x, origin.y), topLeft, steps, negativeXMax.x)
    topLeftXList = getCoordsForXAxis(topLeft, Point(origin.x, yMax.y), steps, yMax.y)
    bottomLeftXList = getCoordsForXAxis(bottomLeft, Point(origin.x, negativeYMax.y), steps, negativeYMax.y)
    bottomLeftYList = getCoordsForYAxis(bottomLeft, Point(negativeXMax.x, origin.y), steps, negativeXMax.x)
    bottomLeftYList.reverse()
    topRightYList = getCoordsForYAxis(Point(xMax.x, origin.y), topRight, steps, xMax.x)
    topRightXList = getCoordsForXAxis(Point(origin.x, yMax.y), topRight, steps, yMax.y)
    topRightYList.reverse()
    bottomRightXList = getCoordsForXAxis(Point(origin.x, negativeYMax.y), bottomRight, steps, negativeYMax.y)
    bottomRightYList = getCoordsForYAxis(bottomRight, Point(xMax.x, origin.y), steps, xMax.x)

    # Drawing curves
    draw_left_curves(pen, topLeftYList, topLeftXList)
    draw_right_curves(pen, topRightYList, topRightXList)
    draw_left_curves(pen, bottomLeftYList, bottomLeftXList)
    draw_right_curves  (pen, bottomRightYList, bottomRightXList)

def setup_screen():
    # Drawing base
    pen.penup()
    pen.goto(topLeft.x, topLeft.y)
    pen.pendown()
    pen.goto(bottomLeft.x, bottomLeft.y)
    pen.goto(bottomRight.x, bottomRight.y)
    pen.goto(topRight.x, topRight.y)
    pen.goto(topLeft.x, topLeft.y)
    pen.penup()


# Quit function
running = True
def quit():
    global running
    running = False

# Setting up the screen
wn = turtle.Screen()
wn.setup(width=width, height=height)
wn.tracer(1)
wn.bgcolor('black')
wn.title('Parabolic Curves')

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.hideturtle()



try:
    maxParts = float(input('Please enter how many iterations you would like: '))
    maxParts += 1
except ValueError:
    print('You did not type a number! Please re-start the program, and do it right this time')
    quit()

parts = 0
setup_screen()
while(parts < maxParts):
    
    setup_iteration(parts)
    # wn.clear()
    # wn.tracer(1)
    # wn.bgcolor('black')
    parts += 1

    wn.listen()
    wn.onkeypress(quit, 'q')
    wn.onkeypress(quit, 'Q')


while running:
    wn.update()