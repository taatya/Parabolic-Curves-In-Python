# Imports
import turtle
from utu2 import screen_size, width, height, padding, paddedWidth, paddedHeight, origin, yMax, xMax, negativeXMax, negativeYMax, topLeft, topRight, bottomLeft, bottomRight, Point, getCoordsForYAxis, getCoordsForXAxis, draw_right_curves, draw_left_curves

print("starting parabola drawing")



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
draw_left_curves(pen, yList, xList)
# draw_left_curves(pen, yList, negativeXList)
# draw_left_curves(pen, negativeYList, negativeXList)
# draw_left_curves(pen, negativeYList, xList)

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
