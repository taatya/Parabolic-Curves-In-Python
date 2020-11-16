# Imports
import turtle
from utilities import draw_curves, Point, getCoordsForXAxis, getCoordsForYAxis

print("starting parabola drawing")


#  Variables
origin = Point(0,0)
yMax = Point(origin.x, 480)
xMax = Point(480, origin.y)
NegativeXMax = Point(-480, 0)
NegativeYMax = Point(0, -480)

# Parts
try:
    parts = float(input('Please enter how many parts you would like ( the number of dots): '))
    parts += 1
except ValueError:
    print('You did not type a number! Please re-start the program, and do it right this time')
    quit()

# Steps
steps = (yMax.y - origin.y) / parts

# Calculating coordinates
yList = getCoordsForYAxis(origin, yMax, steps, 0)
xList = getCoordsForXAxis(origin, xMax, steps, 0)
NegativeXList = getCoordsForXAxis(NegativeXMax, origin, steps, 0)
NegativeYList = getCoordsForYAxis(NegativeYMax, origin, steps, 0)
yList.reverse()
NegativeXList.reverse()
print(NegativeXList)
print(yList)


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
pen.speed(10)
pen.color('green')
pen.hideturtle()


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
