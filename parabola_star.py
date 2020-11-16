# Imports
import turtle
from draw_curves import draw_curves

print("starting parabola drawing")

# Defines a coordinate
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)

#  Variables
origin = Point(0,0)
yMax = Point(origin.x, 480)
xMax = Point(480, origin.y)
NegativeXMax = Point(-480, 0)
NegativeYMax = Point(0, -480)
try:
    parts = float(input('Please enter how many parts you would like ( the number of dots): '))
    parts += 1
except ValueError:
    print('You did not type a number! Please re-start the program, and do it right this time')
    quit()
parts += 1
yList = []
xList = []
NegativeXList = []
NegativeYList = []
# Steps
steps = (yMax.y - origin.y) / parts

# Setting up the screen
width = 1000
height = 1000
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

# Calculating y coordinates
y = 0
while y <= yMax.y:
    yPoint = Point(origin.x, y)
    yList.append(yPoint)
    y += steps

# Calculating x coordinates
x = 0
while x <= xMax.x:
    xPoint = Point(x, origin.y)
    xList.append(xPoint)
    x += steps

# Calculating negative x coordinates
NegativeX = 0
while NegativeX >= NegativeXMax.x:
    NegativeXPoint = Point(NegativeX, origin.y)
    NegativeXList.append(NegativeXPoint)
    NegativeX -= steps

# Calculating negative x coordinates
NegativeY = 0
while NegativeY >= NegativeYMax.y:
    NegativeYPoint = Point(origin.x, NegativeY)
    NegativeYList.append(NegativeYPoint)
    NegativeY -= steps


# Drawing the base
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.goto(origin.x, yMax.y)

pen.penup()
pen.goto(origin.x, origin.y)
pen.pendown()
pen.goto(xMax.x, origin.y)

pen.penup()
pen.goto(origin.x, origin.y)
pen.pendown()
pen.goto(NegativeXMax.x, origin.y)

pen.penup()
pen.goto(origin.x, origin.y)
pen.pendown()
pen.goto(origin.x, NegativeYMax.y)

yList.reverse()
NegativeYList.reverse()
LenOfList = len(yList)



# Making the curves
draw_curves(pen, xList, yList)
draw_curves(pen, NegativeXList, yList)
draw_curves(pen, NegativeXList, NegativeYList)
draw_curves(pen, xList, NegativeYList)

# Quitting the program
running = True

def quit():
    global running
    running = False

# Taking in key presses/ inputs
wn.listen()
wn.onkeypress(quit, 'q')
wn.onkeypress(quit, 'Q')

# Main Loop
while running:
    wn.update()