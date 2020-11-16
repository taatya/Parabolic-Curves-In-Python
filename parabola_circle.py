# Imports
from draw_curves import draw_curves, Point, getCoordsForXAxis, getCoordsForYAxis
import turtle

# Screen Size
width = 1000
height = 1000
padding = 40
paddedWidth = width - padding
paddedHeight = height - padding

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
draw_curves(pen, topLeftYList, topLeftXList)
draw_curves(pen, bottomLeftYList, bottomLeftXList)
draw_curves(pen, topRightYList, topRightXList)
draw_curves(pen, bottomRightYList, bottomRightXList)

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