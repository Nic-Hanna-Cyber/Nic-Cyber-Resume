"""
This program will allow the user to play a simple game of pong using the
turtle module to draw the objects
Author: Nic Hanna
Date: April 27th
Have Fun!
"""
import turtle as t
import time

def create_display():
    """
    This function will create the display for pong using the turtle
    screen function.
    Input: None
    Output: None
    """
    sc = t.Screen()  # create turtle screen object for interface
    sc.title("PONG")
    sc.bgcolor("white")
    sc.setup(width = 1000, height = 1000)
    return sc

def create_left_paddle():
    """
    This program will create the paddle objects for the pong game
    Input = None
    Output = None
    """
    left_paddle = t.Turtle()
    left_paddle.speed(0)
    left_paddle.shape("square")
    left_paddle.color("red")
    left_paddle.shapesize(stretch_wid= 6,stretch_len= 2)  # form paddle 
    left_paddle.penup()  # move without drawing
    left_paddle.goto(-400,0)
    return left_paddle

def create_right_paddle():
    """
    This program will create the paddle objects for the pong game
    Input = None
    Output = None
    """ 
    right_paddle = t.Turtle()
    right_paddle.speed(0)
    right_paddle.shape("square")
    right_paddle.color("blue")
    right_paddle.shapesize(stretch_wid= 6,stretch_len= 2)
    right_paddle.penup()
    right_paddle.goto(400,0)
    return right_paddle

def create_ball():
    """
    This function will create the ball for the game
    Input: None
    Output: Ball object
    """
    ball = t.Turtle()
    ball.speed(40)
    ball.shape("circle")
    ball.color("green")
    ball.penup()  # do not draw when moving
    ball.goto(0,0)
    ball.dx = 5  # determines the movement on the x-plane of the ball when the game is going on
    ball.dy =-5  # determines movement on the y-plane
    return ball

def initialize_score():
    """
    This function will create a score list object
    Input: None
    Return: List of score values
    """
    left_player = 0
    right_player = 0
    return [right_player, left_player]  # return values as a list

def display_score():
    """
    This function displays the initial score for the game, starts both players at 0
    Input: None
    Output: Sketch object which is essentially the display text for the score
    """
    sketch = t.Turtle()
    sketch.speed(0)
    sketch.color("black")
    sketch.penup()
    sketch.goto(0,375)  # move to top
    sketch.write("Left Player = 0     Right Player = 0 ", align = "center", font = ("Times New Roman", 24 ,"normal")) # create title, format places score
    sketch.hideturtle()  # hide cursor
    return sketch

def update_score(sketch,score):
    """
    This function will update the text display previously created to track score, it will use a score list object to update score which will be subscribed
    Input: Display sketch object and score list int object
    Return: None, updates score in place
    """
    sketch.clear()
    sketch.write("Left Player = {}     Right Player = {}".format(score[1], score[0]), align = "center", font = ("Times New Roman", 24 ,"normal"))

def end_game(sketch):
    """
    This function will update the text display to say game over
    """
    sketch.clear()
    sketch.write("GAME OVER", align = "center", font = ("Times New Roman", 24 ,"normal"))

def move_left_up(left_paddle):
    y = left_paddle.ycor()  # get cords for location of paddle on y axis
    if y < 250:  # limit movement
        y += 20  # increment for movement
        left_paddle.sety(y)  # set the new y cord to account for user movement of paddle

def move_left_down(left_paddle):
    y = left_paddle.ycor() 
    if y > -240:
        y -= 20 
        left_paddle.sety(y)

def move_right_up(right_paddle):
    y = right_paddle.ycor()
    if y < 250: 
        y += 20 
        right_paddle.sety(y) 

def move_right_down(right_paddle):
    y = right_paddle.ycor()  
    if y > -240:
        y -= 20 
        right_paddle.sety(y)

def bind_keys(sc,left_paddle,right_paddle):
    """
    This function will bind movement of paddles to keys
    Input = Screen object, Right paddle, Left paddle
    Output = None
    """
    sc.listen()  # prompts the window to "listen" for inputs

    sc.onkeypress(lambda: move_left_up(left_paddle), "w")  # lambda allows for the move function to be dependent on pressing "w"
    sc.onkeypress(lambda: move_left_down(left_paddle), "s")
    sc.onkeypress(lambda: move_right_up(right_paddle), "Up")
    sc.onkeypress(lambda: move_right_down(right_paddle), "Down")
def main():
  sc = create_display()  # create screen object
  score = initialize_score()

  left_paddle = create_left_paddle()
  right_paddle = create_right_paddle()
  ball = create_ball()

  bind_keys(sc, left_paddle, right_paddle)
  score_display = display_score()

  Game_not_over = True
  while Game_not_over:
    sc.update()  # updates the screen with ball and paddle movement

    # Below code sets the movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 280:  # checking boundary to make sure ball stays in play
        ball.sety(280) # reset ball if it goes out bounds
        ball.dy *= -1  # flip the sign

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1  # makes sign positive since the ball is already going down i.e negative

    if ball.xcor() > 500:  # pass threshold on right
        ball.goto(0,0)  # reset ball
        ball.dy *= -1 
        score[1] += 1 # update left player score to 1
        update_score(score_display,score)

    if ball.xcor() <- 500:  # pass threshold on right
        ball.goto(0,0)
        ball.dy *= -1
        score[0] += 1  # update right player score to 1
        update_score(score_display,score)
        """
        the below conditional statement will make sure that the ball will not phase through the paddle by making sure it is stopped at the edge of the paddle not the
        middle thus, it checks the x cord. In terms of the y, the middle of the paddle will be used for the y cord so 70 must be added or removed in order to accurately
        track the height of the paddle
        """
    if (ball.xcor() > 360 and ball.xcor() < 370) and \
    (ball.ycor() < right_paddle.ycor() + 70 and ball.ycor() > right_paddle.ycor() - 70):
        ball.setx(360)  # reset ball to position at front of paddle to avoid phasing and clipping
        ball.dx *= -1  # flip ball movement

    if (ball.xcor() < -360 and ball.xcor() > -370) and \
    (ball.ycor() < left_paddle.ycor() + 70 and ball.ycor() > left_paddle.ycor() - 70):
        ball.setx(-360)
        ball.dx *= -1
    if score[0] or score[1] == 10:
        Game_not_over = False
        end_game(score_display)
  t.mainloop()  # keep window open
if __name__ ==  "__main__":
    main()