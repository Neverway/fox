from enum import Enum


# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
sky_blue = (125, 125, 255)

# Set character direction
class Direction(Enum):
    left = 'left'
    right = 'right'
