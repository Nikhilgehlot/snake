import random

import pygame
from pygame import *

pygame.mixer.init()
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
brown = (80, 0, 0)
green = (0, 29, 29)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))  # to create display

# background image
bgimage = pygame.image.load("snake.jpg")
bgimage = pygame.transform.scale(bgimage, (screen_width, screen_height)).convert_alpha()
bgimage1 = pygame.image.load("gameover.jpg")
bgimage1 = pygame.transform.scale(bgimage1, (screen_width, screen_height)).convert_alpha()
bgimage2 = pygame.image.load("welcome.jpg")
bgimage2 = pygame.transform.scale(bgimage2, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snakes_By_Nikhil")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 65)  # to include font
font2 = pygame.font.SysFont(None, 25)


def text_screen2(text, color, x, y):
    screen_text2 = font2.render(text, True, color)  # to enter text
    gameWindow.blit(screen_text2, [x, y])


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):  # to display on window
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:

        gameWindow.fill((240, 211, 240))  # to fill window
        gameWindow.blit(bgimage2, (0, 0))  # to add image

        text_screen("Welcome to Snakes", black, 225, 160)
        text_screen("Press Space Bar To Play", black, 185, 220)
        text_screen2("Created By: NIKHIL GEHLOT", black, 15, 565)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play(10)
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(55, screen_width - 200)
    food_y = random.randint(55, screen_height - 200)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(bgimage1, (0, 0))
            text_screen("Press Enter To Continue", white, 200, 500)
            text_screen("Score : " + str(score), white, 350, 80)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        exit_game = True
                        pygame.mixer.music.load('welcome.mp3')
                        pygame.mixer.music.play()
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 30 and abs(snake_y - food_y) < 30:

                score += 10

                food_x = random.randint(55, screen_width - 200)
                food_y = random.randint(55, screen_height - 200)
                snk_length += 5

                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimage, (0, 0))
            text_screen("Score: " + str(score) + "  Highcore: " + str(hiscore), green, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, brown, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit()


pygame.mixer.music.load('welcome.mp3')
pygame.mixer.music.play()
welcome()
