# Author: T.T. Chen
# Date: 04/20/2022
# Purpose: Pong Game

from cs1lib import *

# Constants & Variables -----------------------
WINDOW_X = 1000
WINDOW_Y = 1000
game_in_progress = False

# paddles
P_WIDTH = WINDOW_X // 20
P_LENGTH = WINDOW_Y // 5
LX_I = 0  # initial paddle values
LY_I = 0
RX_I = WINDOW_X - P_WIDTH
RY_I = WINDOW_Y - P_LENGTH
lx = LX_I  # tracking paddle's movement throughout game
ly = LY_I
rx = RX_I
ry = RY_I
y_move = (WINDOW_Y - P_LENGTH) // 25
    # this must be a factor of (WINDOW_Y - P_LENGTH), otherwise there will be a gap!
    # --> ensure this by using fraction???? error????????????????? --> BC NO FLOATS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
y_min = y_move  # to allow one last move
y_max = WINDOW_Y - P_LENGTH - y_move

# ball
BR = WINDOW_X * (11/400)
BX_I = WINDOW_X // 2  # initial ball values
BY_I = WINDOW_Y // 2
bvx = WINDOW_X // 35
bvy = WINDOW_Y // 45
bx = BX_I  # tracking ball's movement throughout game
by = BY_I
bvx = bvx
bvy = bvy
BUFFER = WINDOW_X // 20


# key press
a_press = False
z_press = False
k_press = False
m_press = False
space_press = False
q_press = False


# Helper Functions -----------------------

# Draw a paddle
def draw_paddle(px, py, pw, pl):
    disable_stroke()
    set_fill_color(0.5, 0.5, 0.75)  # periwinkle
    draw_rectangle(px, py, pw, pl)


# Draw ball
def draw_ball(bx, by, br):
    # enable_stroke()
    # set_stroke_color(0, 0, 0)
    disable_stroke()
    set_fill_color(0.7, 0.7, 0.7)
    draw_circle(bx, by, br)


# Determine whether keys have been pressed
def my_key_press(value):
    global a_press, z_press, k_press, m_press, space_press, q_press

    # to move paddles
    if value == "a":
        a_press = True  # what's the reason again that we use boolean AND put it in my_draw to be called continuously???
    if value == "z":
        z_press = True
    if value == "k":
        k_press = True
    if value == "m":
        m_press = True

    # to restart & quit game
    if value == " ":
        space_press = True
    if value == "q":
        q_press = True


# Determine whether keys have been released
def my_key_release(value):
    global a_press, z_press, k_press, m_press, space_press, q_press

    # to move paddles
    if value == "a":
        a_press = False
    if value == "z":
        z_press = False
    if value == "k":
        k_press = False
    if value == "m":
        m_press = False

    # to restart & quit game
    if value == " ":
        space_press = False
    if value == "q":
        q_press = False


# Move paddles based on key pressing
def move_paddles():
    global ly, ry
    if a_press and ly >= y_min:
        ly = ly - y_move
    if z_press and ly <= y_max:
        ly = ly + y_move
    if k_press and ry >= y_min:
        ry = ry - y_move
    if m_press and ry <= y_max:
        ry = ry + y_move


# Next 5 helper functions: determine if ball has "collided" (moved beyond) a vertical or horizontal wall, or paddle
    # "The ball might more than one pixel in each time step, so perfect equality may never be achieved.
    # Greater-than and less-than operators are great!"

def ball_beyond_vertical_walls():
    global bx, BR, game_in_progress

    if bx < BR - BUFFER or bx > WINDOW_X - BR + BUFFER:  # added "buffer" so that it looks like the ball keeps going off-screen
        game_in_progress = False


def ball_beyond_top_wall():
    global by, BR

    if by < BR:
        return True


def ball_beyond_bottom_wall():
    global by, BR

    if by > WINDOW_Y - BR:
        return True


# whether hit left or right paddle
    # for inner face: if center of ball @ height of point on paddle and if past the paddle x boundary
    # AND for top & bottom of paddle?????????????????????????????????? --> extend upper and lower bounds instead

def ball_beyond_left_paddle():
    global ly, by, bx, BR, P_LENGTH, P_WIDTH
    if ly - BR <= by <= ly + P_LENGTH + BR and bx < BR + P_WIDTH:
        return True


def ball_beyond_right_paddle():
    global ry
    if ry - BR <= by <= ry + P_LENGTH + BR and bx > WINDOW_X - BR - P_WIDTH:
        # omg don't forget this is RIGHT paddle!!! ry not ly.
        return True

    # what about hitting paddle from above!!! --> circumference of ball & perimeter of paddle? no. bc no collisions.
    # hehe can we make it hit off top at least? --> I think adding the buffer and the side part helped a lot!!!!!!!!!


# Draw pong graphics
def my_draw():
    global ly, ry, bx, by, bvx, bvy, game_in_progress

    # sets background
    set_clear_color(0.1, 0.1, 0.1)  # dark grey
    clear()

    # draws paddles
    draw_paddle(lx, ly, P_WIDTH, P_LENGTH)
    draw_paddle(rx, ry, P_WIDTH, P_LENGTH)

    # stops game, HAVE TO HAVE THIS HERE NOT LATER LMAOOOOOOOO
    ball_beyond_vertical_walls()

    # draws ball and sets paddle and ball movement
    if game_in_progress:  # don't need while loop because it's in my_draw
        draw_ball(bx, by, BR)
        move_paddles()
        bx = bx + bvx
        by = by + bvy

        # checks if ball has moved beyond bounds, triggers bouncing of ball when appropriate
        if ball_beyond_top_wall():
            by = BR
            bvy = -bvy
        elif ball_beyond_bottom_wall():
            by = WINDOW_Y - BR
            bvy = -bvy
        elif ball_beyond_left_paddle():
            bx = BR + P_WIDTH
            bvx = -bvx
        elif ball_beyond_right_paddle():
            bx = WINDOW_X - BR - P_WIDTH
            bvx = -bvx
            # GETS TRAPPED!!!!!!! --> omg we have to reset the position, bc it could overlap very far
            # and then reverse and still overlap and reverse and then redo over and over again.

    # restarts or quits game --> elifs here bc NOT allowed when game is in progress, so can't cheat and start over lol
    elif space_press:
        ly = LY_I
        ry = RY_I
        bx = BX_I
        by = BY_I
        bvx = bvx
        bvy = bvy
        game_in_progress = True
    elif q_press:
        cs1_quit()


start_graphics(my_draw, key_press=my_key_press, key_release=my_key_release, width=WINDOW_X, height=WINDOW_Y)
