# Imports
import turtle
from utilities import draw_curves, Point, getCoordsForXAxis, getCoordsForYAxis


#  Variables
maxQuantity = 480
origin = Point(0, 0)
yMax = Point(origin.x, maxQuantity)
xMax = Point(maxQuantity, origin.y)

# Parts
try:
    parts = float(input('Please enter how many parts you would like ( the number of dots): '))
    parts += 1
except:
    print('You did not type a number! Please re-start the program, and do it right this time')
    quit()

# Steps
steps = (yMax.y - origin.y) / parts

yList = getCoordsForYAxis(origin, Point(origin.x, yMax.y), steps, 0)
xList = getCoordsForXAxis(origin, Point(xMax.x, origin.x), steps, 0)
yList.reverse()


# Setting up the screen
wn = turtle.Screen()
wn.setup(width=1000, height=1000)
wn.tracer(1)
wn.bgcolor('black')
wn.title('Parabolic Curves (curve)')

# Pen
pen = turtle.Turtle()
pen.speed(10)
pen.color('green')
pen.hideturtle()

# Drawing the base
pen.penup()
pen.goto(origin.x, origin.y)
pen.pendown()
pen.goto(origin.x, yMax.y)

pen.penup()
pen.goto(origin.x, origin.y)
pen.pendown()
pen.goto(xMax.x, origin.y)

# Making the curve
draw_curves(pen, yList, xList)

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