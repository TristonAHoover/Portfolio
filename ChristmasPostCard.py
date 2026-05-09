import turtle as t
import random as r

wn = t.Screen()
wn.bgcolor("sky blue")

# ground

ground = t.Turtle()
ground.color("white")
ground.shape("square")
ground.shapesize(100)
ground.speed(0)

ground.penup()
ground.right(90)
ground.forward(1300)
ground.pendown()

# tree

tree = t.Turtle()
tree.color("darkgreen")
tree.pensize(10)
tree.speed(0)

tree.begin_fill()

tree.penup()
tree.backward(70)
tree.right(90)
tree.forward(200)
tree.left(90)
tree.pendown()
tree.left(180)
for i in range(3):
    tree.forward(90)
    tree.right(135)
    tree.forward(125)
    tree.left(135)
tree.right(135)
tree.forward(125)
tree.right(90)
tree.forward(250)
for i in range(2):
    tree.right(135)
    tree.forward(105)
    tree.left(135)
    tree.forward(125)
tree.right(135)
tree.forward(105)
tree.left(90)
tree.forward(100)
tree.right(90)
tree.forward(120) # tree base
tree.right(90)
tree.forward(100)

tree.end_fill()

# ornaments

ornament1 = t.Turtle()
ornament1.color("red")
ornament1.shape("circle")
ornament1.shapesize(2)
ornament1.speed(0)
ornament1.penup()
ornament1.backward(60)
ornament1.left(90)
ornament1.forward(20)
ornament1.pendown()

ornament2 = t.Turtle()
ornament2.color("blue")
ornament2.shape("circle")
ornament2.shapesize(2)
ornament2.speed(0)
ornament2.penup()
ornament2.forward(70)
ornament2.right(90)
ornament2.forward(80)
ornament2.pendown()

ornament3 = t.Turtle()
ornament3.color("gold")
ornament3.shape("circle")
ornament3.shapesize(2)
ornament3.speed(0)
ornament3.penup()
ornament3.backward(30)
ornament3.right(90)
ornament3.forward(160)
ornament3.pendown()

# snowman

snowman1 = t.Turtle()
snowman1.color("white")
snowman1.shape("circle")
snowman1.shapesize(6)
snowman1.speed(0)
snowman1.penup()
snowman1.backward(360)
snowman1.right(90)
snowman1.forward(250)
snowman1.pendown()

snowman2 = t.Turtle()
snowman2.color("white")
snowman2.shape("circle")
snowman2.shapesize(5)
snowman2.speed(0)
snowman2.penup()
snowman2.backward(360)
snowman2.right(90)
snowman2.forward(150)
snowman2.pendown()

snowman3 = t.Turtle()
snowman3.color("white")
snowman3.shape("circle")
snowman3.shapesize(4)
snowman3.speed(0)
snowman3.penup()
snowman3.backward(360)
snowman3.right(90)
snowman3.forward(70)
snowman3.pendown()

carrot = t.Turtle()
carrot.color("orange")
carrot.pensize(10)
carrot.speed(0)
carrot.penup()
carrot.backward(340)
carrot.right(90)
carrot.forward(70)
carrot.pendown()
carrot.left(90)
carrot.forward(25)

eye1 = t.Turtle()
eye1.color("black")
eye1.shape("circle")
eye1.shapesize(0.5)
eye1.speed(0)
eye1.penup()
eye1.backward(330)
eye1.right(90)
eye1.forward(60)
eye1.pendown()

eye2 = t.Turtle()
eye2.color("black")
eye2.shape("circle")
eye2.shapesize(0.5)
eye2.speed(0)
eye2.penup()
eye2.backward(360)
eye2.right(90)
eye2.forward(60)
eye2.pendown()

# star

star = t.Turtle()
star.color("gold")
star.speed(0)
star.pensize(2)

star.begin_fill()

star.penup()
star.left(86)
star.forward(220)
star.right(90)
star.pendown()

star.right(75)
star.forward(100)

for i in range (4):
    star.right(144)
    star.forward(100)

star.end_fill()

# presents

present1 = t.Turtle()
present1.color("red")
present1.shape("square")
present1.shapesize(3)
present1.speed(0)

present1.penup()
present1.backward(230)
present1.right(90)
present1.forward(275)
present1.pendown()

present2 = t.Turtle()
present2.color("blue")
present2.shape("square")
present2.shapesize(2)
present2.speed(0)

present2.penup()
present2.backward(160)
present2.right(90)
present2.forward(285)
present2.pendown()

# cloud

cloud1 = t.Turtle()
cloud1.color("light gray")
cloud1.shape("circle")
cloud1.shapesize(7)
cloud1.speed(0)
cloud1.penup()
cloud1.backward(340)
cloud1.left(90)
cloud1.forward(240)
cloud1.pendown()

cloud2 = t.Turtle()
cloud2.color("light gray")
cloud2.shape("circle")
cloud2.shapesize(5)
cloud2.speed(0)
cloud2.penup()
cloud2.backward(400)
cloud2.left(90)
cloud2.forward(220)
cloud2.pendown()

cloud3 = t.Turtle()
cloud3.color("light gray")
cloud3.shape("circle")
cloud3.shapesize(5)
cloud3.speed(0)
cloud3.penup()
cloud3.backward(270)
cloud3.left(90)
cloud3.forward(220)
cloud3.pendown()

# random birds in the sky

birdInTheSky = t.Turtle()
birdInTheSky.color("black")
birdInTheSky.speed(0)
birdInTheSky.pensize(5)
birdInTheSky.penup()
birdInTheSky.forward(270)
birdInTheSky.left(90)
birdInTheSky.forward(360)
birdInTheSky.pendown()
birdInTheSky.right(135)
birdInTheSky.forward(20)
birdInTheSky.left(90)
birdInTheSky.forward(20)

birdInTheSky2 = t.Turtle()
birdInTheSky2.color("black")
birdInTheSky2.speed(0)
birdInTheSky2.pensize(5)
birdInTheSky2.penup()
birdInTheSky2.forward(320)
birdInTheSky2.left(90)
birdInTheSky2.forward(340)
birdInTheSky2.pendown()
birdInTheSky2.right(135)
birdInTheSky2.forward(20)
birdInTheSky2.left(90)
birdInTheSky2.forward(20)

# Used https://docs.python.org/3/library/turtle.html to figure out text
t.pencolor("white")
t.write("Merry Chrimes", True, align="center", font=("arial",72,"bold"))

# Used https://stackoverflow.com/questions/40447880/how-can-i-import-an-image-in-python-turtle to figure out images
image = r"C:\Users\RebelScum\Pictures\goose.gif"

wn.addshape(image)
t.shape(image)

# snowflakes

snowflakes = []
for i in range(10):
    flake = t.Turtle()
    flake.color("white")
    flake.shape("circle")
    flake.speed(0)
    flake.teleport(r.randint(-400,400),r.randint(-300,300))
    snowflakes.append(flake)

# make em move
while True:
    for s in snowflakes:
        speedX,speedY = r.randint(-20,20),r.randint(-10,30)
        newX = s.xcor() + speedX
        newY = s.ycor() - speedY

        s.teleport(newX,newY)

        if s.ycor() < -400:
            s.penup()
            s.setx(r.randint(-400,400))
            s.sety(400)
            s.pendown()