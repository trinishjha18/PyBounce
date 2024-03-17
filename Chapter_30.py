"""
Chapter_30 is about working on pygame the ball bouncing game
Created on: 2/16/24
Modified on:3/17/24 by Trinish Jha
Modified on: 3/15/24 by Rahul Tevatia
"""
import pygame

# Initialize pygame
pygame.init()
# Screen setup
width = 640
length = 480
screen = pygame.display.set_mode((width, length))
clock = pygame.time.Clock()
dt = 0

# Settings for bar
bar_width = 70
bar_length = 20
bar_x = 385
bar_y = 450
bar_speed = 5

# Settings for ball
ball_radius = 13
ball_pos_x = 200
ball_pos_y = 70
ball_speed_y = 2
ball_speed_x = 2

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bar_x > 0:
        bar_x -= bar_speed
    if keys[pygame.K_RIGHT] and bar_x < width - bar_width:
        bar_x += bar_speed


    # Update ball's position
    ball_pos_x += ball_speed_x
    ball_pos_y += ball_speed_y

    # Bounce off left and right walls
    if ball_pos_x - ball_radius <= 0 or ball_pos_x + ball_radius >= width:
        ball_speed_x = -ball_speed_x

    # Bounce off the bar
    if ball_pos_y + ball_radius >= bar_y and bar_x <= ball_pos_x <= bar_x + bar_width:
        ball_speed_y = -ball_speed_y  # Reverse the vertical direction

    # Bounce off the top window edge
    if ball_pos_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y  # Reverse the vertical direction

    # Ball disappears when it moves beyond the bottom of the window
    if ball_pos_y - ball_radius > length:
        ball_pos_x, ball_pos_y = -30, -30  # Move the ball off-screen

    # Draw the basket
    pygame.draw.rect(screen, (255, 255, 255), [bar_x, bar_y, bar_width, bar_length])

    # Draw the ball
    pygame.draw.circle(screen, "red", (ball_pos_x, ball_pos_y), ball_radius)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
