#Developped by Swifty
import turtle
import random


court_height = 1000
court_width = 600


cursor_size = 15
snake_height = 25
snake_width = 10
body_space = 25
 
loose = False

score = 0

#Screen
wn = turtle.Screen()
wn.title("Snake Block")
wn.setup(height = 1.0, width = 1.0)
wn.bgcolor("black")
wn.tracer(2)


# Snake
snake = turtle.Turtle()
snake.color("white")
snake.shape("square")
snakespeed = 2
snake.pu()
snake.setheading(90)
snake.speed("fastest")

#Apple
apple = turtle.Turtle()
apple.color("cyan")
apple.shape("square")
apple.pu()
apple.speed(0)
#Score
turtle_score = turtle.Turtle()
turtle_score.speed(0)
turtle_score.pu()
turtle_score.ht()
turtle_score.color("white")
turtle_score.setposition(-cursor_size*5, court_width/2+cursor_size)



#Blocks
blocks = [ ]

#We define our writing turtle
twrite = turtle.Turtle()
twrite.ht()
twrite.pu()
twrite.setx(-court_width/5)
twrite.color("white")


        
def terrain():
    b = turtle.Turtle()
    b.color("white")
    b.speed(5)
    b.width(3)
    b.ht()
    b.pu() 
    b.setposition(-court_height/2, court_width/2)
    b.pd()
    for i in range (2):
        b.fd(court_height)
        b.right(90)
        b.fd(court_width)
        b.right(90)


def up():
    global snake
    if snake.heading() != 270:
        snake.setheading(90)
        turning_x = snake.xcor()
        turning_y = snake.ycor()
        
def left():
    global snake
    if snake.heading() != 0:
        snake.setheading(180)
        turning_x = snake.xcor()
        turning_y = snake.ycor()
def right():
    global snake
    if snake.heading() != 180:
        snake.setheading(0)
        turning_x = snake.xcor()
        turning_y = snake.ycor()
        
def down():
    global snake
    if snake.heading() != 90:
        snake.setheading(270)
        turning_x = snake.xcor()
        turning_y = snake.ycor()
def loose():
    twrite = turtle.Turtle()
    twrite.ht()
    twrite.pu()
    twrite.setx(-court_width/5)
    twrite.color("white")
    twrite.write("You loose ", font = ("Arial", 44, "normal" ))

def food():
    apple_x = random.randint(-court_height/2+cursor_size,court_height/2-cursor_size)
    apple_y = random.randint(-court_width/2+cursor_size, court_width/2-cursor_size)
    apple.setposition(apple_x, apple_y)
       
def blocks1():
    block = turtle.Turtle()
    block.speed(0)
    block.color("red")
    block.pu()
    block.shape("square")
    block.setposition(snake.xcor() - cursor_size, snake.ycor() - cursor_size)
    blocks.append(block)
    
def distance(t1,t2):
    global score
    distance = t1.distance(t2)
    if distance < cursor_size:
        food()
        blocks1()
        score += 10
        turtle_score.clear()
        turtle_score.write("Score: "+str(score), font = ("Calibri", 44, "normal") )
def distanceblock():
    global loose
    for block in blocks:
        distanceB = snake.distance(block)
        if distanceB < cursor_size:
            loose()
            loose = True
def restart():
    loose = False
    for block in blocks:
        block.reset()
    wn.reset()
    game()
    
turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(down, "Down")
turtle.onkey(restart, "space")

#Main loop
def main():

    terrain()
    food()
    global loose, apple
    turtle_score.write("Score: "+str(score), font = ("Calibri", 44, "normal"))
    while loose != True:
        snake.fd(snakespeed)
        y = snake.ycor()
        x = snake.xcor()
        if x > court_height/2 - cursor_size or x < - court_height/2 + cursor_size:
            loose()
            break
        if y > court_width/2-cursor_size or y < -court_width/2+cursor_size:
            loose()
            break
        distance(snake,apple)
        distanceblock()


main()
turtle.mainloop()
