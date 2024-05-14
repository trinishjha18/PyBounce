import random


def screen_settings():
    # Screen setup
    width = 640
    height = 480
    return width, height


def bar_settings():
    bar_width = 70
    bar_length = 20
    bar_x = 135
    bar_y = 450
    bar_speed = 5
    return bar_width, bar_length, bar_y, bar_x,


def ball_settings():
    # Settings for ball
    ball_radius = 13
    ball_pos_x = random.randint(12, 640 - ball_radius)
    # ball_pos_x = 100
    ball_pos_y = 70
    ball_speed_y = 2
    ball_speed_x = 2
    return ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x, bar_speed
