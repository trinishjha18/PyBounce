import random
import pygame


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
    return bar_width, bar_length, bar_y, bar_x, bar_speed


def ball_settings():
    # Settings for ball
    ball_radius = 13
    ball_pos_x = random.randint(12, 640 - ball_radius)
    # ball_pos_x = 100
    ball_pos_y = 70
    ball_speed_y = 2
    ball_speed_x = 2
    return ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x


def colors():
    green = (0, 255, 0)
    blue = (0, 0, 128)
    return green, blue


def play_again(width, height, bar_x, bar_y, bar_width, bar_length, screen, ball_pos_x, ball_pos_y, ball_radius):
    font1 = pygame.font.Font('freesansbold.ttf', 32)
    text = font1.render('Play again?', 13, (0, 0, 0))
    text_x = width / 2 - text.get_width() / 2
    text_y = height / 2 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
    paddle = pygame.draw.rect(screen, (255, 255, 255), [bar_x, bar_y, bar_width, bar_length])
    ball = pygame.draw.circle(screen, "red", (ball_pos_x, ball_pos_y), ball_radius)
    return text, text_x, text_y, textx_size, texty_size, paddle, ball, font1
