"""
Chapter_30 is about working on pygame the ball bouncing game
Created on: 2/16/24
Modified on:3/17/24 by Trinish Jha
Modified on: 3/15/24 by Rahul Tevatia
"""
import pygame
from settings import *
from collision_settings import collision


width, height = screen_settings()
ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x = ball_settings()
bar_width, bar_length, bar_y, bar_x, bar_speed = bar_settings()
counter = 0

# Initialize pygame
pygame.init()
# Screen setup
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
dt = 0
text, text_x, text_y, textx_size, texty_size, paddle, ball, font1 = play_again(width, height, bar_x, bar_y, bar_width, bar_length, screen, ball_pos_x, ball_pos_y, ball_radius)
green, blue = colors()
font = pygame.font.Font('freesansbold.ttf', 32)
running = True
game_over = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            if restart_button.collidepoint(mouse_pos[0], mouse_pos[1]):
                game_over = False
                counter = 0
                ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x = ball_settings()
                bar_width, bar_length, bar_y, bar_x, bar_speed = bar_settings()
    if not game_over:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        # When a key is pressed move it either to the left or the right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bar_x > 0:
            bar_x -= bar_speed
        if keys[pygame.K_RIGHT] and bar_x < width - bar_width:
            bar_x += bar_speed

        # Draw the basket
        paddle = pygame.draw.rect(screen, (255, 255, 255), [bar_x, bar_y, bar_width, bar_length])

        # Draw the ball
        ball = pygame.draw.circle(screen, "red", (ball_pos_x, ball_pos_y), ball_radius)
        # Start the ball movement
        ball_pos_y += ball_speed_y
        ball_pos_x += ball_speed_x

        # simple collision detection
        ball_speed_x, ball_speed_y, counter = collision(width, height, bar_width, bar_y, bar_x, ball_pos_y,
                                                        ball_speed_x,
                                                        ball_speed_y, ball_radius, ball_pos_x, counter)
        if ball_speed_x == 0 and ball_speed_y == 0:
            game_over = True

        text = font.render(f"Points: {counter}", True, green, blue)

        screen.blit(text, (10, 10))

    else:
        text2 = font.render(f"GAME OVER", True, green, blue)
        screen.blit(text2, (height/2, width/2))
        restart_button = pygame.draw.rect(screen, (255, 255, 255), [70, 20, 60, 50])

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()


# def main():
#     run_game()
#
#
# if __name__ == "__main__":
#     main()
