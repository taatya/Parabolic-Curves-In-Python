# Imports
import turtle
from utilities import draw_left_curves, draw_right_curves, Point, getCoordsForXAxis, getCoordsForYAxis, pen_speed


# Screen Size
screen_size = 1000.0
width = screen_size
height = screen_size
padding = 40.0
paddedWidth = width - padding
paddedHeight = height - padding

# Points
origin = Point(((screen_size - padding) / 2) * (-1),((screen_size - padding) / 2) * (-1))
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
except:
    print('You did not type a number! Please re-start the program, and do it right this time')
    quit()

# Steps
steps = (yMax.y - origin.y) / parts

yList = getCoordsForYAxis(origin, Point(origin.x, yMax.y), steps, origin.x)
xList = getCoordsForXAxis(origin, Point(xMax.x, origin.x), steps, origin.y)
yList.reverse()


# Setting up the screen
wn = turtle.Screen()
wn.setup(width=width, height=height)
wn.tracer(1)
wn.bgcolor('black')
wn.title('Parabolic Curves (curve)')

# Pen
pen = turtle.Turtle()
pen.speed(pen_speed)
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
draw_left_curves(pen, yList, xList)

# Quitting the program
running = True

def quit():
    global running
    running = False

# Taking in key presses/ inputs
wn.listen()
wn.onkeypress(quit, 'q')
wn.onkeypress(quit, 'Q')

print("Working On It.")

# Main Loop
while running:
    wn.update()