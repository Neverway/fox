import pygame
import logging

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

# Load sprites
fox = pygame.sprite.Sprite()  # create sprite
fox.base_image = pygame.image.load('sprites/entities/fox/fox_base.png').convert()
fox.right = pygame.transform.scale2x(fox.base_image)
fox.left = pygame.transform.flip(fox.right, True, False)
fox.image = fox.right
fox.rect = fox.image.get_rect()  # use image extent values
fox.width, fox.height = fox.rect.size

grass = pygame.image.load('sprites/environment/forest/grass.png')
dirt = pygame.image.load('sprites/environment/forest/dirt.png')
stone = pygame.image.load('sprites/environment/forest/stone.png')
tree = pygame.image.load('sprites/environment/forest/tree.png')
box = pygame.image.load('sprites/environment/other/box.png')


# Spawn player
def player(img, pos):
    game_display.blit(img, pos)


# Temp map
# Grass
def grid(pos, x_size=32, y_size=32):
    x, y = pos
    return x * x_size, y * y_size


map_1 = {
    # Left wall
    dirt: [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (0, 8),
        (0, 9),
        (0, 10),
        (0, 11),
        (0, 12),
        (0, 13),
        (0, 14),
        (0, 15),
        (0, 16),
        (0, 17),
        (0, 18),
        # Right wall
        (24, 0),
        (24, 1),
        (24, 2),
        (24, 3),
        (24, 4),
        (24, 5),
        (24, 6),
        (24, 7),
        (24, 8),
        (24, 9),
        (24, 10),
        (24, 11),
        (24, 12),
        (24, 13),
        (24, 14),
        (24, 15),
        (24, 16),
        (24, 17),
        (24, 18),
        ],
    grass: [
        # floor
        (1, 18),
        (2, 18),
        (3, 18),
        (4, 18),
        (5, 18),
        (6, 18),
        (7, 18),
        (8, 18),
        (9, 18),
        (10, 18),
        (11, 18),
        (12, 18),
        (13, 18),
        (14, 18),
        (15, 18),
        (16, 18),
        (17, 18),
        (18, 18),
        (19, 18),
        (20, 18),
        (21, 18),
        (22, 18),
        (23, 18),
        ],
    stone: [
        (18, 17),
        (18, 16),
        (17, 17)],
    box: [
        (18,153)

    ]
}


def display_image(img, pos):
    game_display.blit(img, grid(pos))


def display_map(map):
    for image, coords in map.items():
        for coord in coords:
            display_image(image, coord)


# Game loop
x = (display_width * 0.45)
y = (display_height * 0.8)
game_exit = False

x_accel = 5
y_accel = 5

while not game_exit:
    for event in pygame.event.get():
        log.debug(event)
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            # Left right movement
            if event.key == pygame.K_LEFT:
                fox.image = fox.left
                x += -x_accel
            if event.key == pygame.K_RIGHT:
                fox.image = fox.right
                x += x_accel
            # Up Down movement
            if event.key == pygame.K_UP:
                y += -y_accel
            if event.key == pygame.K_DOWN:
                y += y_accel

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass

    if x < 0:
        x = 0
    if x > display_width - fox.width:
        x = display_width - fox.width

    if y < 0:
        y = 0
    if y > display_height - fox.height:
        y = display_height - fox.height

    game_display.fill(sky_blue)
    player(fox.image, (x, y))
    display_map(map_1)
    pygame.display.update()
    clock.tick(framerate)

pygame.quit()
