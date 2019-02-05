import pygame

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
character = pygame.image.load('sprites/entities/fox/fox_base.png')
grass = pygame.image.load('sprites/environment/forest/grass.png')
dirt = pygame.image.load('sprites/environment/forest/dirt.png')
stone = pygame.image.load('sprites/environment/forest/stone.png')
tree = pygame.image.load('sprites/environment/forest/tree.png')


# Spawn player
def player(x, y):
    game_display.blit(character, (x, y))


# Game loop
x = (display_width * 0.45)
y = (display_height * 0.8)
game_exit = False

x_accel = 5
y_accel = 5

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            # Left right movement
            if event.key == pygame.K_LEFT:
                x += -x_accel
            if event.key == pygame.K_RIGHT:
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

    game_display.fill(sky_blue)
    player(x, y)
    pygame.display.update()
    clock.tick(framerate)

pygame.quit()
