    # Imports
import turtle
import utilities
from utilities import screen_size, width, height, padding, paddedWidth, paddedHeight, origin, yMax, xMax, negativeXMax, negativeYMax, topLeft, topRight, bottomLeft, bottomRight, Point, getCoordsForYAxis, getCoordsForXAxis, draw_right_curves, draw_left_curves


# Helping to make the curves

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


# Parts
try:
    parts = float(input('Please enter how many parts you would like ( the number of dots): '))
    parts += 1
except ValueError:
    print('You did not type a number! Please re-start the program, and do it right this time')
    quit()

# Steps
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

# Setting up the screen
wn = turtle.Screen()
wn.setup(width=width, height=height)
wn.tracer(1)
wn.bgcolor('black')
wn.title('Parabolic Curves')

# Pen
pen = turtle.Turtle()
pen.speed(10)
pen.color('green')
pen.hideturtle()

# Drawing base
pen.penup()
pen.goto(topLeft.x, topLeft.y)
pen.pendown()
pen.goto(bottomLeft.x, bottomLeft.y)
pen.goto(bottomRight.x, bottomRight.y)
pen.goto(topRight.x, topRight.y)
pen.goto(topLeft.x, topLeft.y)
pen.penup()

# Drawing curves
draw_left_curves(pen, topLeftYList, topLeftXList)
draw_left_curves(pen, bottomLeftYList, bottomLeftXList)
draw_right_curves(pen, topRightYList, topRightXList)
draw_right_curves  (pen, bottomRightYList, bottomRightXList )

# Quit function
running = True
def quit():
    global running
    running = False

wn.listen()
wn.onkeypress(quit, 'q')
wn.onkeypress(quit, 'Q')

while running:
    wn.update()