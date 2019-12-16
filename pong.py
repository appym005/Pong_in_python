import turtle
import os
import random

#game setup

#----
#initializing screen
wm = turtle.Screen()
wm.title("Pong by @appy_m_005")
wm.bgcolor("green")
wm.setup(width = 800, height = 600)
#stops window from updating
wm.tracer(0)
#----

#game_control_variable
gcv= False

#paddle a
paddle_a = turtle.Turtle()
#not the speed of paddle but speed of animation.This command sets animation to 
#max possible speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.dy = 20


#paddle b
paddle_b = turtle.Turtle()
#not the speed of paddle but speed of animation.This command sets animation to 
#max possible speed
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.dy = 20


#ball
ball = turtle.Turtle()
#not the speed of paddle but speed of animation.This command sets animation to 
#max possible speed
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(-0,0)
#d in dx is delta, as in small difference. 
#instructs ball to move n px x and y
ball.dx =  0
ball.dy =  0
#variables to store dx and dy values while paused
x = 0
y = 0


#pen2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)
pen2.write("Choose Game Mode\n    press 'A' for single-player\n    press 'B' for multiplayer",align = "center", font = ("Courier", 24, "normal"))


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))


#score
score_a = 0
score_b = 0


#paddle a Functions
def paddle_a_up():
	if paddle_a.ycor() + 40 < 290:
		y = paddle_a.ycor()
		y += paddle_a.dy
		paddle_a.sety(y)

def paddle_a_down():
	if paddle_a.ycor() - 40 > -290:
		y = paddle_a.ycor()
		y -= paddle_a.dy
		paddle_a.sety(y)


#paddle b Functions
def paddle_b_up():
	if paddle_b.ycor() + 40 < 290:
		y = paddle_b.ycor()
		y += paddle_b.dy
		paddle_b.sety(y)

def paddle_b_down():
	if paddle_b.ycor() - 40 > -290:
		y = paddle_b.ycor()
		y -= paddle_b.dy
		paddle_b.sety(y)

#control variables
ends = 100

#starting functions
def starting_condition():
	if start_screen == True:
		pen2.clear()
		pen2.write("Choose end score:\n press '1' for 10\n press '2' for 15\n press '3' for 20", align = "center", font = ("Courier", 24, "normal"))

def set_end_10():
	if start_screen == True:
		global ends
		ends = 1
		set_ball_displacement()

def set_end_15():
	if start_screen == True:
		global ends
		ends = 15
		set_ball_displacement()

def set_end_20():
	if start_screen == True:
		global ends
		ends = 20
		set_ball_displacement()

def set_ball_displacement():
	pen2.clear()
	global start_screen 
	start_screen = False
	a = [0.05,-0.05]
	ball.dx = a[random.randint(0,1)]
	ball.dy = a[random.randint(0,1)]

#variable checking  state
paused = False
start_screen = True
end_screen = False
#state change function
def do():
	if paused:
		resume()
	else:
		if not paused and not start_screen:
			pause()
	
#pause function
def pause():
	global paused
	paused = True
	global x
	global y
	x = ball.dx
	y = ball.dy
	ball.dx = 0
	ball.dy = 0
	pen2.write("Paused\nPress 'r' to restart", align = "center", font = ("Courier", 24, "normal"))

def resume():
	global paused
	paused = False
	pen2.clear()
	ball.dx = x
	ball.dy = y

def game_stop():
	global end_screen
	end_screen = True
	ball.dx = 0
	ball.dy = 0
	pen2.clear()
	if score_a > score_b:
		pen2.write("Player A wins\n rematch?\n press 'y' or 'n'", align = "center", font = ("Courier", 24, "normal"))
	elif score_a < score_b:
		pen2.write("Player B wins\n rematch?\n press 'y' or 'n'", align = "center", font = ("Courier", 24, "normal"))
	else:
		pen2.write("Draw\n rematch?\n press 'y' or 'n'", align = "center", font = ("Courier", 24, "normal"))

def rematch():
	ball.setx(0)
	ball.sety(0)
	global end_screen 
	global Paused
	if end_screen == True or paused == True:
		paused = False
		pen2.clear()
		global score_a
		score_a = 0
		global score_b
		score_b = 0
		end_screen = False
		global start_screen
		start_screen = True
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align = "center", font = ("Courier", 24, "normal"))
		pen2.clear()
		pen2.write("Choose Game Mode\n    press 'A' for single-player\n    press 'B' for multiplayer",align = "center", font = ("Courier", 24, "normal"))


def end():
	if end_screen == True:
		wm.bye()

#keyboard binding
wm.listen()
wm.onkeypress(paddle_a_up,"w")
wm.onkeypress(paddle_a_down,"s")
wm.onkeypress(paddle_a_up,"W")
wm.onkeypress(paddle_a_down,"S")
wm.onkeypress(paddle_b_up,"Up")
wm.onkeypress(paddle_b_down,"Down")
wm.onkeypress(starting_condition,"A")
wm.onkeypress(starting_condition,"b")
wm.onkeypress(starting_condition,"a")
wm.onkeypress(starting_condition,"B")
wm.onkeypress(do,"Escape")
wm.onkeypress(set_end_10, "1")
wm.onkeypress(set_end_15, "2")
wm.onkeypress(set_end_20, "3")
wm.onkeypress(rematch, "y")
wm.onkeypress(rematch, "Y")
wm.onkeypress(end, "n")
wm.onkeypress(end, "N")
wm.onkeypress(rematch, "r")
wm.onkeypress(rematch, "R")



#main game loop
while True:
	wm.update()

	if score_a >= ends or score_b >= ends:
		game_stop()

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#border checking
	if ball.ycor() > 290:
		ball.sety(290)
		#reverses the direction
		ball.dy *= -1
		os.system("aplay pong/bounce.wav&")

	if ball.ycor() < -290:
		ball.sety(-290)
		#reverses the direction
		ball.dy *= -1
		os.system("aplay pong/bounce.wav&")

	#right
	if ball.xcor() > 390:
		ball.setx(390)
		#reverses the direction
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align = "center", font = ("Courier", 24, "normal"))
		os.system("aplay pong/bounce.wav&")

	#left
	if ball.xcor() < -390:
		ball.setx(-390)
		#reverses the direction
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align = "center", font = ("Courier", 24, "normal"))
		os.system("aplay pong/bounce.wav&")


	#collision check
	if ball.xcor() > 330 and ball.xcor() < 350 and ball.ycor()  < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
		ball.setx(330)
		ball.dx += (0.005 if ball.dx > 0 else -0.005)
		ball.dx *= -1
		paddle_b.dy += 0.001
		os.system("aplay pong/bounce.wav&")

	if ball.xcor() < -330 and ball.xcor() > -350 and ball.ycor()  < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
		ball.setx(-330)
		ball.dx += (0.005 if ball.dx > 0 else -0.005)
		ball.dx *= -1
		paddle_a.dy += 0.001
		os.system("aplay pong/bounce.wav&") 