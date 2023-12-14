import turtle

pen_speed = 10.0


# Defines a coordinate
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)


# Screen Size
screen_size = 1000.0
width = screen_size
height = screen_size
padding = 40.0
paddedWidth = width - padding
paddedHeight = height - padding


points = int(input("Enter how many points you want: "))
input_angle = (int(input("Enter the angle you want: ")))
angle = 90-input_angle

# Setting up the screen
wn = turtle.Screen()
wn.setup(width=width, height=height)
wn.tracer(0)
wn.bgcolor('black')
wn.title('Parabolic Curves')


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.hideturtle()
pen.turtlesize(2)
pen.penup()
pen.setheading(90)


# Points
origin = Point(0, 0)
aMax = Point(origin.x, paddedHeight / 2)
pen.setheading(90 + angle)
pen.forward(paddedHeight / 2)
bMax = Point(pen.xcor, pen.ycor)
pen.setheading(90)
pen.goto(origin.x, origin.y)

steps = (aMax.y) / points

# Quit function
running = True
def quit():
    global running
    running = False

def getCoordsA(bottom, top, steps, x):
    aList = []
    y = bottom.y
    while y <= top.y:
        aPoint = Point(x, y)
        aList.append(aPoint)
        y += steps
    return aList

def getCoordsB(aList, steps):
    pen.setheading(angle)
    bList = []
    x = 0
    LenOfList = len(aList)
    while x < LenOfList:
        pen.forward(steps)
        bPoint = Point(pen.xcor(), pen.ycor())
        bList.append(bPoint)
        x += 1
    # pen.setheading(90)
    return bList

def draw(pen, aList, bList):
    i = 0
    LenOfList = len(aList)
    while i < LenOfList:
        pen.penup()
        if i != len(aList) - 1 and len(bList) -1:
            pen.goto(aList[i+1].x, aList[i+1].y)
            pen.pendown()
            pen.goto(bList[i].x, bList[i].y)
        else:
            pen.goto(aList[i].x, aList[i].y)
            pen.pendown()
            pen.goto(bList[i].x, bList[i].y)
        i += 1


aList = getCoordsA(origin, aMax, steps, aMax.x)
bList = getCoordsB(aList, steps)
# print(aList)
# print(bList)

bList.reverse()

draw(pen, aList, bList)

wn.listen()
wn.onkeypress(quit, 'q')
wn.onkeypress(quit, 'Q')

while running:
    wn.update()