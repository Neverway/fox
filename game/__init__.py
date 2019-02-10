import logging

import pygame

from game.constants import Direction
from game.models import (
    Box,
    Dirt,
    Fox,
    Grass,
    Stone,
    Tree,
)
from game.utils import grid

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# Important and need to be first
pygame.init()

# Resolution of window
display_width = 800
display_height = 600

# Create window
game_display = pygame.display.set_mode((display_width, display_height))

# Window title
pygame.display.set_caption('Fox in a box')

# Window icon
window_icon = pygame.image.load('game.png')
pygame.display.set_icon(window_icon)

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
sky_blue = (125, 125, 255)

# Add clock
clock = pygame.time.Clock()
framerate = 60


fox = Fox(*grid(0, 16))
mobs = pygame.sprite.Group()
mobs.add(
    fox,
)


terrain1 = pygame.sprite.Group()
terrain1.add(
    Grass(0, 18),
    Grass(1, 18),
    Grass(2, 18),
    Grass(3, 18),
    Grass(4, 18),
    Grass(5, 18),
    Grass(6, 18),
    Grass(7, 18),
    Grass(8, 18),
    Grass(9, 18),
    Grass(10, 18),
    Grass(11, 18),
    Grass(12, 18),
    Grass(13, 18),
    Grass(14, 18),
    Grass(15, 18),
    Grass(18, 18),
    Grass(19, 18),
    Grass(20, 18),
    Grass(21, 18),
    Grass(22, 18),
    Grass(23, 18),
    Grass(24, 18),
    Stone(3, 17),
    Dirt(5, 17),
)

terrain2 = pygame.sprite.Group()
terrain2.add(
    Stone(0, 18),
    Stone(1, 18),
    Stone(2, 18),
    Stone(3, 18),
    Stone(4, 18),
    Stone(5, 18),
    Stone(6, 18),
    Stone(7, 18),
    Stone(8, 18),
    Stone(9, 18),
    Stone(10, 18),
    Stone(11, 18),
    Stone(12, 18),
    Stone(13, 18),
    Stone(14, 18),
    Stone(15, 18),
    Stone(18, 18),
    Stone(19, 18),
    Stone(20, 18),
    Stone(21, 18),
    Stone(22, 18),
    Stone(23, 18),
    Stone(24, 18),
)

goal = pygame.sprite.Group()
goal.add(
    Box(23, 17),
)

sky = sky_blue
level = terrain1


def display_image(img, pos):
    game_display.blit(img, grid(pos))


def display_map(map):
    for image, coords in map.items():
        for coord in coords:
            display_image(image, coord)


# Game loop
game_exit = False

delta_x = 0
delta_y = 0
x_accelerate = 5
y_accelerate = 16
gravity = -5

while not game_exit:
    collisions = pygame.sprite.groupcollide(mobs, level, False, False)
    # if collisions:
    #     log.info(collisions)
    win = pygame.sprite.groupcollide(mobs, goal, False, False)
    if win:
        print("You Win!")
        level = terrain2
        fox.x = 32
        fox.y = 32*17
        sky = black
    for event in pygame.event.get():
        log.debug(event)
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            # Left right movement
            if event.key == pygame.K_LEFT:
                delta_x = -x_accelerate
            if event.key == pygame.K_RIGHT:
                delta_x = x_accelerate
            if event.key == pygame.K_SPACE:
                delta_y = y_accelerate

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                delta_x = 0
            if event.key == pygame.K_SPACE:
                delta_y = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass

    if delta_x < 0:
        fox.facing = Direction.left
    if delta_x > 0:
        fox.facing = Direction.right

    fox.x += delta_x
    fox.y -= delta_y + gravity

    if fox.x < 0:
        fox.x = 0
    if fox.x > display_width - fox.rect.width:
        fox.x = display_width - fox.rect.width

    if fox.y < 0:
        fox.y = 0
    if fox.y > display_height - fox.rect.height:
        fox.y = display_height - fox.rect.height

    game_display.fill(sky)
    mobs.draw(game_display)
    level.draw(game_display)
    goal.draw(game_display)
    pygame.display.update()
    clock.tick(framerate)

pygame.quit()
