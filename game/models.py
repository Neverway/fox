import pygame.image
from pygame.sprite import Sprite

from game.constants import Direction
from game.utils import grid


class Block(Sprite):
    image = pygame.image.load('sprites/missing.png')

    def __init__(self, x, y):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.move_ip(*grid(x, y))


class Box(Block):
    image = pygame.image.load('sprites/environment/other/box.png')


class Dirt(Block):
    image = pygame.image.load('sprites/environment/forest/dirt.png')


class Grass(Block):
    image = pygame.image.load('sprites/environment/forest/grass.png')


class Stone(Block):
    image = pygame.image.load('sprites/environment/forest/stone.png')


class Tree(Block):
    image = pygame.image.load('sprites/environment/forest/tree.png')


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
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, value):
        self.rect.x = value

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, value):
        self.rect.y = value

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
