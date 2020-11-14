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

#  Variables
origin = Point(0,0)
yMax = Point(0, 480)
xMax = Point(480, 0)
parts = float(input('Please enter how many parts you would like ( the number of dots): '))
if parts == str:
    running = False
    print('You did not type a number! Please re-start the program, and do it right this time')
parts += 1
yList = []
xList = []
zList = []
# Steps
steps = (yMax.y - origin.y) / parts

# Setting up the screen
wn = turtle.Screen()
wn.setup(width=1000, height=1000)
wn.tracer(1)
wn.bgcolor('black')
wn.title('Parabolic Curves')

# Pen
pen = turtle.Turtle()
pen.speed(10)
pen.color("white")
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


# Drawing the base
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.goto(0, yMax.y)

pen.penup()
pen.goto(origin.x, origin.y)
pen.pendown()
pen.goto(xMax.x, origin.y)

# Making the curve
yList.reverse()
i = 0
LenOfList = len(yList)
while i < LenOfList:
    pen.penup()
    pen.goto(xList[i].x, xList[i].y)
    pen.pendown()
    pen.goto(yList[i].x, yList[i].y)
    i += 1

# Quitting the program
running = True

def quit():
    global running
    running = False

# Taking in key presses/ inputs
wn.listen()
wn.onkeypress(quit, 'q')

# Main Loop
while running:
    wn.update()