import pygame
from button2 import *

# initialize screen
pygame.init()
clock = pygame.time.Clock()

# create display
screen = pygame.display.set_mode((878, 878))

# title and icon
pygame.display.set_caption("Snake!")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# initialize board
board = Board()
types = {'empty': (0, 0, 0), 'food': (255, 0, 0), 'snake': (45, 175, 0)}

# game over text
font = pygame.font.Font('BalsamiqSans-Regular.ttf', 74)

def print_game_over():
    text = font.render('GAME OVER', True, (0, 0, 0))
    screen.blit(text, (218, 220))

running = True
key = prev = 'E'
while running:

    # RGB background
    screen.fill((240, 240, 240))

    # check for key press
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and prev != "N":
                key = 'S'
            elif event.key == pygame.K_UP and prev != "S":
                key = 'N'
            elif event.key == pygame.K_LEFT and prev != "E":
                key = 'W'
            elif event.key == pygame.K_RIGHT and prev != "W":
                key = 'E'
            elif board.game_over and event.key == pygame.K_SPACE:
                key = 'SPACE'
        elif event.type == pygame.QUIT:
            running = False

    # move snake
    if not board.game_over:
        board.move(key)
        prev = key

    # print board
    for row in board.map:
        for pix in row:
            color = types[pix.type]
            pygame.draw.rect(screen, color, pix.pos + (32, 32))

    # print game over screen
    if board.game_over:
        pygame.draw.rect(screen, (255, 255, 255), (213, 213, 452, 102))
        print_game_over()
        if key == 'SPACE':
            board = Board()
            key = prev = 'E'

    # update display
    pygame.display.update()

    # throttle frames per second and difficulty (higher FPS == harder)
    clock.tick(8)