import pygame
import logging
import enum

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


class Direction(enum.Enum):
    left = 'left'
    right = 'right'


class Mob(pygame.sprite.Sprite):
    base_image = pygame.image.load('sprites/missing.png')

    def __init__(self, x, y):
        super().__init__()
        self.image_right = self.base_image
        self.image_left = pygame.transform.flip(self.base_image, True, False)
        self.rect = self.base_image.get_rect()
        self.rect.move_ip(x, y)
        self.facing = Direction.right

    @property
    def image(self):
        if self.facing == Direction.left:
            return self.image_left
        elif self.facing == Direction.right:
            return self.image_right


class Fox(Mob):
    base_image = pygame.transform.scale2x(
        pygame.image.load('sprites/entities/fox/fox_base.png')
    )


# Temp map
def grid(x, y, x_size=32, y_size=32):
    return x * x_size, y * y_size


class Block(pygame.sprite.Sprite):
    image = pygame.image.load('sprites/missing.png')

    def __init__(self, x, y):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.move_ip(*grid(x, y))


class Grass(Block):
    image = pygame.image.load('sprites/environment/forest/grass.png')


class Dirt(Block):
    image = pygame.image.load('sprites/environment/forest/dirt.png')


class Stone(Block):
    image = pygame.image.load('sprites/environment/forest/stone.png')


class Box(Block):
    image = pygame.image.load('sprites/environment/other/box.png')


class Tree(Block):
    image = pygame.image.load('sprites/environment/forest/tree.png')


fox = Fox(*grid(0, 16))
mobs = pygame.sprite.Group()
mobs.add(
    fox,
)

terrain = pygame.sprite.Group()
terrain.add(
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
    Box(7, 17),
)


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
                fox.facing = Direction.left
                x += -x_accel
            if event.key == pygame.K_RIGHT:
                fox.facing = Direction.right
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
    if x > display_width - fox.rect.x:
        x = display_width - fox.rect.x

    if y < 0:
        y = 0
    if y > display_height - fox.rect.y:
        y = display_height - fox.rect.y

    game_display.fill(sky_blue)
    mobs.draw(game_display)
    terrain.draw(game_display)
    pygame.display.update()
    clock.tick(framerate)

pygame.quit()
