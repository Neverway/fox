import logging

import pygame

from game.constants import (
    Direction,
    black,
    blue,
    green,
    red,
    sky_blue,
    white,
)
from game.levels import (
    level_1,
    level_2,
    level_3,
    level_4,
    level_5,
    #level_6,

)
from game.models import (
    Box,
    Dirt,
    Fox,
    Grass,
    Stone,
    Tree,
    Poison
)
from game.physics import (
    displacement,
    distance,
)
from game.utils import grid

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def ground_clamp(mob, collisions):
    lowest_surface = max(
        collisions,
        key=lambda x: x.rect.top,
    )
    return min(mob.rect.bottom, lowest_surface.rect.top)


def run():
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

    # Add clock
    clock = pygame.time.Clock()
    framerate = 60

    fox = Fox(*grid(0, 16))
    mobs = pygame.sprite.Group()
    mobs.add(
        fox,
    )

    terrain1 = pygame.sprite.Group()
    terrain1.add(*level_1.terrain)

    terrain2 = pygame.sprite.Group()
    terrain2.add(*level_2.terrain)

    terrain3 = pygame.sprite.Group()
    terrain3.add(*level_3.terrain)

    terrain4 = pygame.sprite.Group()
    terrain4.add(*level_4.terrain)

    terrain5 = pygame.sprite.Group()
    terrain5.add(*level_5.terrain)

    goal = pygame.sprite.Group()
    goal.add(
        Box(23, 17),
    )

    sky = sky_blue

    level = terrain1
    next_level = 2

    # Game loop
    game_exit = False

    delta_x = 0
    delta_y = 0
    x_accelerate = 5
    y_accelerate = 16
    gravity = -5

    while not game_exit:
        for event in pygame.event.get():
            # log.debug(event)
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

            if event.type == pygame.KEYDOWN:
                # Dev meddler
                if event.key == pygame.K_2:
                    level = terrain2

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

        collisions = pygame.sprite.groupcollide(mobs, level, False, False)
        if collisions:
            pass
            # log.info(collisions)

        for mob in collisions:
            mob.rect.bottom = ground_clamp(mob, collisions[mob])

        win = pygame.sprite.groupcollide(mobs, goal, False, False)
        if win:
            if next_level == 2:
                print("Next level")
                level = terrain2
                fox.x = 32
                fox.y = 32*17
                sky = black
                next_level = 3
            elif next_level == 3:
                print("Next level")
                level = terrain3
                fox.x = 32
                fox.y = 32*17
                sky = black
                next_level = 4
            elif next_level == 4:
                print("Next level")
                level = terrain4
                fox.x = 32
                fox.y = 32*17
                sky = black
                next_level = 5
            elif next_level == 5:
                print("Next level")
                level = terrain5
                fox.x = 32
                fox.y = 32*17
                sky = black
                next_level = 6


        game_display.fill(sky)
        mobs.draw(game_display)
        level.draw(game_display)
        goal.draw(game_display)
        pygame.display.update()
        clock.tick(framerate)

    pygame.quit()
