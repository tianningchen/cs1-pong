# Author: T.T. Chen
# Date: 2022_0902
# Purpose: Pong Game 2.0, with bells & whistles :)

from cs1lib import *
from random import uniform, randint
from math import sqrt
import math


# In this update of Pong Game 2.0:
    # current score
    # high score
    # color scheme change @ 11th hit
    # random velocities
    # standardized speed
    # paddle positions centered
    # ball accelerated when paddle is in motion during collision
    # animation for hitting center of paddle
    # .......


# Constants & Variables -----------------------
WINDOW_X = 1000
WINDOW_Y = 1000
game_in_progress = False

# periwinkle as initial color scheme, transparency for ball's confetti
r = 0.5
g = 0.5
b = 0.75
wh = 0.7

# ball
BR = WINDOW_X * (11/400)
BX_I = WINDOW_X // 2  # initial ball values
BY_I = WINDOW_Y // 2
bx = BX_I
by = BY_I
SPEED = 20
speed = SPEED
bvx = WINDOW_X // 35
bvy = WINDOW_Y // 45
# BUFFER = WINDOW_X // 20
bay = WINDOW_Y // 300  # ball's acceleration in y direction
mid_hit = True

# paddles
P_WIDTH = WINDOW_X // 20
P_LENGTH = WINDOW_Y // 5
LX_I = 0  # initial paddle values --------------------------------> CENTER BOTH!!!!!!!!!!!!!!!!!!!!
LY_I = WINDOW_Y // 2 - P_LENGTH // 2
RX_I = WINDOW_X - P_WIDTH
RY_I = WINDOW_Y // 2 - P_LENGTH // 2
lx = LX_I  # yes dumbass, I do need separate for tracking paddle's movement throughout game
ly = LY_I
rx = RX_I
ry = RY_I
y_move = (WINDOW_Y // 2 - P_LENGTH // 2) // 10
    # this must be a factor of (WINDOW_Y - P_LENGTH), otherwise there will be a gap!
    # --> ensure this by using fraction???? error????????????????? --> BC NO FLOATS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
y_min = y_move  # to allow one last move
y_max = WINDOW_Y - P_LENGTH - y_move


# key press
a_press = False
z_press = False
k_press = False
m_press = False
space_press = False
q_press = False

# scoring
hi_pts = 0
curr_pts = 0
SCX = BX_I
SHX = BX_I - 2 * P_LENGTH // 5
SCY = P_LENGTH // 3
SHY = P_LENGTH // 2
SCS = WINDOW_Y // 40
SHS = WINDOW_Y // 60


# Helper Functions -----------------------

# Change color scheme
def change_colors():
    global r, g, b
    if curr_pts > 10:
        r = uniform(0.4, 0.8)
        g = uniform(0.4, 0.8)
        b = uniform(0.4, 0.8)
        # print(r, g, b)


# Change score as game progresses
def change_scores():
    global curr_pts, hi_pts

    curr_pts = curr_pts + 1
    if curr_pts > hi_pts:
        hi_pts = hi_pts + 1


# Randomize velocity for start of every game (spacebar)
def rand_init_velocity():
    global bvx, bvy, speed

    bvx = 0  # so we don't repeat last velocity
    while abs(bvx) <= (1.1 * abs(bvy)):  # using "=" in case of bvx = 0
        bvx = randint(- WINDOW_X // 30, WINDOW_X // 30)
        bvy = randint(- WINDOW_X // 30, WINDOW_X // 30)
    # print(bvx, bvy, abs(bvy), abs(bvx) < (1.1 * abs(bvy)))

    # standardize bvx, bvy values. from "raw" speed to set speed. (haha cool I didn't even need sin, cos! :))
    speed = sqrt(bvx**2 + bvy**2)
    bvx = bvx / speed * SPEED
    bvy = bvy / speed * SPEED
    # print(bvx, bvy, speed)


# Draw a paddle
def draw_paddle(px, py, pw, pl):
    disable_stroke()
    set_fill_color(r, g, b)  # periwinkle
    draw_rectangle(px, py, pw, pl)


# Draw ball
def draw_ball(x, y, rad):
    global mid_hit

    disable_stroke()
    set_fill_color(wh, wh, wh)
    draw_circle(x, y, rad)


# Draws the line, helper function for following full confetti drawing
def draw_confetti_line(x, y, side, offset, length, theta):
    # ONLY INTEGERS MY GOODNESS
    draw_line(int(x) + side * int(math.cos(theta) * offset), int(y) + side * int(math.sin(theta) * offset),
              int(x) + side * int(math.cos(theta) * (offset + length)),
              int(y) + side * int(math.sin(theta) * (offset + length)))


# Draw middle confetti
def draw_mid_confetti(x, y):
    enable_stroke()
    set_stroke_width(8)
    set_stroke_color(wh, wh, wh)

    l_center = WINDOW_X // 50
    l_diag = WINDOW_X // 70
    l_side = WINDOW_X // 90
    offset = int(BR + WINDOW_X // 50)
    side = 1  # left default
    if x > WINDOW_X // 2:  # ball right side
        side = -1

    # ONLY INTEGERS MY GOODNESS
    draw_confetti_line(x, y, side, offset, l_center, 0)
    draw_confetti_line(x, y, side, offset, l_diag, math.pi / 4)
    draw_confetti_line(x, y, side, offset, l_diag, - math.pi / 4)
    draw_confetti_line(x, y, side, offset, l_side, math.pi / 2)
    draw_confetti_line(x, y, side, offset, l_side, - math.pi / 2)


# Display score of current game
def draw_curr_score(score, sx, sy, ss):
    enable_stroke()
    set_stroke_color(r, g, b)  # periwinkle
    set_font_size(ss)
    draw_text(str(score), sx, sy)


# Display the highest score accomplished during whole session
def draw_hi_score(score, sx, sy, ss):
    enable_stroke()
    set_stroke_color(r, g, b)  # periwinkle
    set_font_size(ss)
    draw_text("high score: " + str(score), sx, sy)


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

    if bx < BR or bx > WINDOW_X - BR:
        game_in_progress = False
        # "buffer" so that it looks like the ball keeps going off-screen -->
        # bx < BR - BUFFER or bx > WINDOW_X - BR + BUFFER


def ball_beyond_top_wall():
    global by, bvy

    if by < BR:
        by = BR
        bvy = -bvy
        return True


def ball_beyond_bottom_wall():
    global by, bvy

    if by > WINDOW_Y - BR:
        by = WINDOW_Y - BR
        bvy = -bvy
        return True


# whether hit left or right paddle
    # for inner face: if center of ball @ height of point on paddle and if past the paddle x boundary
    # AND for top & bottom of paddle?????????????????????????????????? --> extend upper and lower bounds instead

def ball_beyond_left_paddle():
    global bx, bvx, bvy

    # bounce ball towards right
    if ly - BR <= by <= ly + P_LENGTH + BR and bx < BR + P_WIDTH:
        bx = BR + P_WIDTH
        bvx = -bvx

        # accelerate ball either up or downwards depending on paddle movement
        # (apparently a_press AND z_press is impossible!)
        if a_press:
            bvy = bvy - bay
        elif z_press:
            bvy = bvy + bay
        else:
            print("the paddle is still upon collision")

        # see if hitting center of paddle
        if ly + 3 * P_LENGTH // 8 <= by <= ly + 5 * P_LENGTH // 8:
            draw_mid_confetti(bx, by)
            print(by, ly, ly + 3 * P_LENGTH // 8, ly + 5 * P_LENGTH // 8, ly + P_LENGTH)

        return True


def ball_beyond_right_paddle():
    global bx, bvx, bvy

    # bounce ball towards left
    if ry - BR <= by <= ry + P_LENGTH + BR and bx > WINDOW_X - BR - P_WIDTH:
        # omg RIGHT paddle!!! not ly.
        bx = WINDOW_X - BR - P_WIDTH
        bvx = -bvx
        freeze = by

        # accelerate ball either up or downwards depending on paddle movement
        # (apparently a_press AND z_press is impossible!)
        if k_press:
            bvy = bvy - bay
        elif m_press:
            bvy = bvy + bay
        else:
            print("the paddle is still upon collision")

        # see if hitting center of paddle
        if ry + 3 * P_LENGTH // 8 <= by <= ry + 5 * P_LENGTH // 8:
            draw_mid_confetti(bx, by)
            print(by, ry, ry + 3 * P_LENGTH // 8, ry + 5 * P_LENGTH // 8, ry + P_LENGTH)

        return True

    # what about hitting paddle from above!!! --> circumference of ball & perimeter of paddle? no. bc no collisions.
    # hehe can we make it hit off top at least? --> I think adding the buffer and the side part helped a lot!!!!!!!!!


# Draw pong graphics
def my_draw():
    global ly, ry, bx, by, bvx, bvy, game_in_progress, hi_pts, curr_pts, speed

    # sets background
    set_clear_color(0.1, 0.1, 0.1)  # dark grey
    clear()

    # display scores
    draw_curr_score(curr_pts, SCX, SCY, SCS)
    draw_hi_score(hi_pts, SHX, SHY, SHS)

    # draw paddles AND BALL NOW TOO :) bc we fixed ...
    draw_paddle(lx, ly, P_WIDTH, P_LENGTH)
    draw_paddle(rx, ry, P_WIDTH, P_LENGTH)
    draw_ball(bx, by, BR)

    # ... THIS!!! OH MY GOODNESS!!
    # this (stopping game) needs to come first, so it stops ONCE it's out of bounds (not one moment AFTER!! uh doy.)
    ball_beyond_vertical_walls()  # stops game

    # draws ball and sets paddle and ball movement
    if game_in_progress:  # don't need while loop because it's in my_draw
        move_paddles()
        bx = bx + bvx
        by = by + bvy
        # print(game_in_progress, bx, by, bvx, bvy)
        # print(curr_pts, hi_pts)

        # tracking speed
        speed = sqrt(bvx ** 2 + bvy ** 2)

        # checks if ball has moved beyond bounds, triggers bouncing of ball
        if ball_beyond_top_wall():
            pass
        elif ball_beyond_bottom_wall():
            pass
        elif ball_beyond_left_paddle():
            change_scores()
            change_colors()
        elif ball_beyond_right_paddle():
            change_scores()
            change_colors()
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
        curr_pts = 0
        rand_init_velocity()
        game_in_progress = True
    elif q_press:
        cs1_quit()


start_graphics(my_draw, key_press=my_key_press, key_release=my_key_release, width=WINDOW_X, height=WINDOW_Y)
