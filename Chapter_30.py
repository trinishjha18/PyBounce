"""
Chapter_30 is about working on pygame the ball bouncing game
Created on: 2/16/24
Modified on:3/17/24 by Trinish Jha
Modified on: 3/15/24 by Rahul Tevatia
"""
import pygame
import random

# Initialize pygame
pygame.init()
# Screen setup
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
dt = 0

# Settings for bar
bar_width = 70
bar_length = 20
bar_x = 135
bar_y = 450
bar_speed = 5

# Settings for ball
ball_radius = 13
# ball_pos_x = random.randint(12, width - ball_radius)
ball_pos_x = 100
ball_pos_y = 70
ball_speed_y = 2
ball_speed_x = 2
# ball_moving = True

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
    ball = pygame.draw.circle(screen, "red", (ball_pos_x, ball_pos_y), ball_radius)
    ball_pos_y += ball_speed_y
    ball_pos_x += ball_speed_x

    # simple collision detection
    if ball_pos_y + ball_radius >= bar_y and bar_x <= ball_pos_x <= bar_x + bar_width:
        ball_speed_y *= -1
    elif ball_pos_y <= 2:
        ball_speed_y *= -1
    if ball_pos_x >= width:
        ball_speed_x *= -1
    elif ball_pos_x <= 0:
        ball_speed_x *= -1
    if ball_pos_y > 550:
        ball_speed_x *= 0
        exit()
    # print(ball_pos_x, ball_pos_y)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()


def main():
    pass


if __name__ == "__main__":
    main()
