"""
Chapter_30 is about working on pygames
Created on: 2/16/24
Modified on:2/16/24
Trinish Jha
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


running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Setting for bar

    bar_width = 70
    bar_length = 20
    bar_x = 40
    bar_y = 20
    pygame.draw.rect(screen, "green", [70, 40, 30, 90]) # Homework 1 : Figure out which number is for what
# Homework 2 : Make the bar moving as per user command

    # pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
