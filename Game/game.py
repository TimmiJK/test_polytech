import pygame
from random import randint, randrange
import pygame_menu

pygame.init()

FPS = 30
size_block = 10
size = (500, 500)
eye = 2

snake_color = (0, 255, 0)
apple_color = (255, 0, 0)
black = (0, 0, 0)
dark_green = (50, 205, 50)
white = (255, 255, 255)


def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (size_block * x, size_block * y, size_block, size_block))


def draw_borders(x, y, color):
    pygame.draw.rect(screen, color, (size_block * x, size_block * y, size_block, size_block), 1)


def draw_right_eye(x, y, color):
    pygame.draw.rect(screen, color, (size_block * x + 2, size_block * y + 3, eye, eye))


def draw_left_eye(x, y, color):
    pygame.draw.rect(screen, color, (size_block * x + 6, size_block * y + 3, eye, eye))


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
font = pygame.font.SysFont('microsofttaile', 16)


def start_the_game():
    x_snake = 25
    y_snake = 25
    snake_blocks = [(x_snake, y_snake)]
    length = 1
    dx = 0
    dy = 0
    score = 0
    speed = 0

    move_control = {'w': True, 's': True, 'd': True, 'a': True}

    apple_blocks = randint(3, 49), randint(3, 49)

    clock = pygame.time.Clock()
    Start = True

    # fps and quit from game
    while Start:
        clock.tick(10 + speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Start = False
                break



        # draw black screen
        screen.fill(black)

        # draw apple
        draw_block(*apple_blocks, apple_color)

        # draw snake
        [(draw_block(i, j, snake_color)) for i, j in snake_blocks]

        # draw right eye
        draw_right_eye(*snake_blocks[-1], black)

        # draw left eye
        draw_left_eye(*snake_blocks[-1], black)

        # draw outline
        [(draw_borders(i, j, dark_green)) for i, j in snake_blocks]

        # text
        game_score = font.render("Game score: " + str(score), True, white, black)
        screen.blit(game_score, (15, 0))
        speed_value = font.render("Speed: " + str(speed), True, white, black)
        screen.blit(speed_value, (425, 0))

        # snake movement
        x_snake += dx
        y_snake += dy
        snake_blocks.append((x_snake, y_snake))
        snake_blocks = snake_blocks[-length:]

        # snake eat apple, spawn new apple and increase size of snake
        if snake_blocks[-1] == apple_blocks:
            apple_blocks = randint(3, 49), randint(3, 49)
            length += 1
            score += 1
            if score % 5 == 0:
                if speed <= 20:
                    speed += 1

        # snake eat tail
        if len(snake_blocks) != len(set(snake_blocks)):
            break

        # controls
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and move_control['w']:
            dx = 0
            dy = -1
            move_control = {'w': True, 's': False, 'd': True, 'a': True}
        elif key[pygame.K_s] and move_control['s']:
            dx = 0
            dy = 1
            move_control = {'w': False, 's': True, 'd': True, 'a': True}
        elif key[pygame.K_d] and move_control['d']:
            dx = 1
            dy = 0
            move_control = {'w': True, 's': True, 'd': True, 'a': False}
        elif key[pygame.K_a] and move_control['a']:
            dx = -1
            dy = 0
            move_control = {'w': True, 's': True, 'd': False, 'a': True}

        # teleport, if snake go out of screen
        if x_snake < 1:
            x_snake = 49
        elif x_snake > 49:
            x_snake = 0
        elif y_snake < 3:
            y_snake = 49
        elif y_snake > 49:
            y_snake = 2

        pygame.display.update()


list_of_difficulty = ['easy']


def set_difficulty(value, difficulty):
    select, index = value
    list_of_difficulty[0] = difficulty


def set_music(value, off_or_on):
    pass


def set_sounds(value, off_or_on):
    pass


def controls():
    pass


def resolution():
    pass


settings = pygame_menu.Menu(350, 400, 'Settings', theme=pygame_menu.themes.THEME_DARK)

settings.add_button('Controls', controls)
settings.add_selector('Music :', [('OFF', 1), ('ON', 2)], onchange=set_music)
settings.add_selector('Sounds :', [('OFF', 1), ('ON', 2)], onchange=set_sounds)
# settings.add_selector('Screen resolution :', [(1), (1)], onchange=resolution)

menu = pygame_menu.Menu(350, 400, 'Menu', theme=pygame_menu.themes.THEME_DARK)

menu.add_text_input('Name :', default='Player')
menu.add_button('Play', start_the_game)
menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('Settings', settings)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
