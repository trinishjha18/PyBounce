"""
Chapter_30 is about working on pygames
Created on: 2/16/24
Modified on:2/16/24 by Trinish Jha
Modified on: 3/9/24 by Rahul
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
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Setting for bar

bar_width = 70
bar_length = 20
# bar_x = 40
# bar_y = 20
# pygame.draw.rect(screen, "green", [40, 70, 90, 30]) # Homework 1 : Figure out which number is for what

bar_x = (width / 2) - (bar_width / 2)
bar_y = length - bar_length - 10
bar_speed = 5


running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")


# Homework 2 : Make the bar moving as per user command

    # pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP] and bar_x >0:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_DOWN]:
    #     player_pos.y += 300 * dt
    if keys[pygame.K_LEFT] and bar_x > 0:
        bar_x -= bar_speed
    if keys[pygame.K_RIGHT] and bar_x < width - bar_width:
        bar_x += bar_speed

    # Draw the basket
    pygame.draw.rect(screen, (255, 255, 255), [bar_x, bar_y, bar_width, bar_length])

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
