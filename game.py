import turtle
import random
import winsound
import platform

score = 0
lives=3

# create the main window
wn = turtle.Screen()
wn.title("Cloudy with a Chance of Burgers!")
wn.bgcolor("green")
wn.bgpic("skyback.gif")
wn.setup(width=800, height=600)
wn.tracer(0)


wn.register_shape("simp.gif")
wn.register_shape("burger.gif")
wn.register_shape("salad.gif")
wn.register_shape("simpr.gif")
wn.register_shape("heart.gif")

# add player
# starting position (bottom and without drawing line)
player = turtle.Turtle()
player.speed(0)
player.shape("simp.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# list of burgers
burgers = []


# add burgers
for i in range(8):
    burger = turtle.Turtle()
    burger.speed(0)
    burger.shape("burger.gif")
    burger.color("blue")
    burger.penup()
    burger.goto(-100, 250)
    burger.speed = random.randint(1, 2)
    burgers.append(burger)

# list of salads
salads = []

# add salads
for i in range(12):
    salad = turtle.Turtle()
    salad.speed(0)
    salad.shape("salad.gif")
    salad.color("red")
    salad.penup()
    salad.goto(100, 250)
    salad.speed = random.randint(1, 2)
    salads.append(salad)

# list of extra lives
extralives = []

# add extra lives
for i in range(1):
    extralive = turtle.Turtle()
    extralive.speed(0)
    extralive.shape("heart.gif")
    extralive.color("red")
    extralive.penup()
    extralive.goto(100, 250)
    extralive.speed = random.randint(1,2)
    extralives.append(extralive)

# create the pen to show score and lives
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0, 250)
font = ("Helvetica", 25, "normal")
pen.clear()
pen.write("Score: {}   Lives: {}".format(score, lives), align="center", font=font)


# functions
def go_left():
    player.direction = "left"
    player.shape("simp.gif")


def go_right():
    player.direction = "right"
    player.shape("simpr.gif")



# keyboard binding (listening to keyboard)
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def play_sound(sound_file, time = 0):
    # windows
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # linux
    elif platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    # mac
    else:
        os.system("afplay {}&".format(sound_file))


play_sound("africa.wav", 294)

# main game loop
while True:

    # update screen
    wn.update()


    # player movement
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    # moving burgers
    for burger in burgers:
        y = burger.ycor()
        y -= burger.speed
        burger.sety(y)

        # check for off-screen
        if y < -300:
            # random position after off-screen
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            burger.goto(x, y)

        # check for collision
        if burger.distance(player) < 40:
            play_sound("coin.wav")
            # random position after collision
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            burger.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)


    # moving salads
    for salad in salads:
        y = salad.ycor()
        y -= salad.speed
        salad.sety(y)

        # check for off-screen
        if y < -300:
            # random position after off-screen
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            salad.goto(x, y)

        # check for collision
        if salad.distance(player) < 40:
            play_sound("fail.wav")
            # random position after collision
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            salad.goto(x, y)
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    for extralive in extralives:
        y = extralive.ycor()
        y -= extralive.speed
        extralive.sety(y)

        # check for off-screen
        if y < -300:
            # random position after off-screen
            x = random.randint(-380, 380)
            y = random.randint(1000, 2000)
            extralive.goto(x, y)

        # check for collision
        if extralive.distance(player) < 40:
            play_sound("life.wav")
            # random position after collision
            x = random.randint(-380, 380)
            y = random.randint(1000, 2000)
            extralive.goto(x, y)
            lives += 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

    # game over screen
    if lives <= 0:
        play_sound("over.wav")
        pen.clear()
        pen.goto(0,0)
        font2= ("Helvetica", 50, "bold")
        pen.write("GAME OVER!", align="center", font=font2)
        pen.goto(0,-40)
        pen.write("Score: {}".format(score),align="center",font=font)
        pen.goto(0,-80)
        font3=("Helvetica", 10, "normal")
        pen.write("Click to quit game.", align="center", font=font3)
        wn.exitonclick()


wn.mainloop()
