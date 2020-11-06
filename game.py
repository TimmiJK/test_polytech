import pygame
import random
import sys

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


def draw_block(column, row, color):
    pygame.draw.rect(screen, color, (size_block * column, size_block * row, size_block, size_block))


def draw_borders(column, row, color):
    pygame.draw.rect(screen, color, (size_block * column, size_block * row, size_block, size_block), 1)


def draw_right_eye(column, row, color):
    pygame.draw.rect(screen, color, (size_block * column+2, size_block * row+3, eye, eye))


def draw_left_eye(column, row, color):
    pygame.draw.rect(screen, color, (size_block * column+6, size_block * row+3, eye, eye))


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Apple:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1


class Fence:
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
font = pygame.font.SysFont('microsofttaile', 16)

snake_blocks = [Snake(25, 25)]
d_row = 0
d_col = 1
score = 0
speed = 0

apple_blocks = [Apple(random.randint(0, 49), random.randint(0, 49))]

fence_blocks = [Fence(random.randint(0, 47), random.randint(0, 47))]

clock = pygame.time.Clock()
Start = True

while Start:
    clock.tick(10+speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_DOWN and d_row != 0:
                d_row = 0
                d_col = 1
            elif event.key == pygame.K_RIGHT and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_col != 0:
                d_row = -1
                d_col = 0

    screen.fill((0, 0, 0))

    game_score = font.render("Game score: " + str(score), True, white, black)
    screen.blit(game_score, (25, 0))

    head = snake_blocks[0]
    tail = snake_blocks[-1]
    apple = apple_blocks[0]

    if head.x == -1:
        head.x = 50
    elif head.x == 50:
        head.x = 0
    elif head.y == -1:
        head.y = 50
    elif head.y == 50:
        head.y = 0

    for block1 in apple_blocks:
        draw_block(block1.x1, block1.y1, apple_color)
        draw_borders(block1.x1, block1.y1, white)

    for block in snake_blocks:
        draw_block(block.x, block.y, snake_color)
        draw_borders(block.x, block.y, dark_green)

    for b in range(len(snake_blocks)):
        draw_right_eye(head.x, head.y, black)
        draw_left_eye(head.x, head.y, black)

    if head.x == apple.x1 and head.y == apple.y1:
        new_apple = Apple(random.randint(0, 49), random.randint(0, 49))
        apple_blocks.insert(0, new_apple)
        apple_blocks.pop(-1)
        new_snake_block = Snake(tail.x, tail.y)
        snake_blocks.append(new_snake_block)
        score += 1
        if score % 5 == 0:
            speed += 10

    new_head = Snake(head.x + d_row, head.y + d_col)
    snake_blocks.insert(0, new_head)
    snake_blocks.pop(-1)

    pygame.display.update()
