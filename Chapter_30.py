"""
Chapter_30 is about working on pygame the ball bouncing game
Created on: 2/16/24
Modified on:3/17/24 by Trinish Jha
Modified on: 3/15/24 by Rahul Tevatia
"""
import pygame
from settings import screen_settings
from settings import bar_settings
from settings import ball_settings

width, height = screen_settings()
bar_width, bar_length, bar_y, bar_x = bar_settings()
ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x, bar_speed = ball_settings()

# Initialize pygame
pygame.init()
# Screen setup
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
dt = 0

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
    elif ball_pos_x <= ball_radius:
        ball_speed_x *= -1
    if ball_pos_y > height + ball_radius:
        ball_speed_x = 0
        ball_speed_y = 0
    if ball_pos_y == 430 and ball_pos_x == bar_x:
        # ball_speed_x *= -1
        ball_speed_y *= -1
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()


def main():
    pass


if __name__ == "__main__":
    main()
