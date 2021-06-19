# Imports
import turtle
from utilities import draw_left_curves, draw_right_curves, Point, getCoordsForXAxis, getCoordsForYAxis, pen_speed

print("starting parabola drawing")


# Screen Size
screen_size = 1000.0
width = screen_size
height = screen_size
padding = 40.0
paddedWidth = width - padding
paddedHeight = height - padding

# Points
origin = Point(0, 0)
yMax = Point(origin.x, paddedHeight / 2)
xMax = Point(paddedWidth/ 2, origin.y)
negativeXMax = Point((paddedWidth/ 2) * (-1), origin.y)
negativeYMax = Point(origin.x, (paddedHeight/ 2) * (-1))
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

# Calculating coordinates
yList = getCoordsForYAxis(origin, yMax, steps, 0)
xList = getCoordsForXAxis(origin, xMax, steps, 0)
negativeXList = getCoordsForXAxis(negativeXMax, origin, steps, 0)
negativeYList = getCoordsForYAxis(negativeYMax, origin, steps, 0)
yList.reverse()
negativeXList.reverse()


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
pen.goto(negativeXMax.x, origin.y)

pen.penup()
pen.goto(origin.x, origin.y)
pen.pendown()
pen.goto(origin.x, negativeYMax.y)


# Making the curves
draw_left_curves(pen, xList, yList)
draw_right_curves(pen, xList, negativeYList)
draw_left_curves(pen, negativeXList, negativeYList)
draw_right_curves(pen, negativeXList, yList)

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
