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
ball_speed = 2
ball_moving = True

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bar_x > 0:
        bar_x -= bar_speed
    if keys[pygame.K_RIGHT] and bar_x < width - bar_width:
        bar_x += bar_speed

    # Draw the basket
    paddle = pygame.draw.rect(screen, (255, 255, 255), [bar_x, bar_y, bar_width, bar_length])

    # Draw the ball

    ball_1 = pygame.draw.circle(screen, "red", (ball_pos_x, ball_pos_y), ball_radius)
    if ball_moving:
        # simple collision detection
        if ball_pos_y + ball_radius >= bar_y and bar_x <= ball_pos_x <= bar_x + bar_width:
            ball_speed *= -1
            ball_pos_y += ball_speed
        else:
            ball_pos_y += ball_speed
    if ball_pos_y == 2:
        ball_speed *= -1
        ball_pos_y += ball_speed

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

