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

# Load sprites
character = pygame.image.load('sprites/entities/fox/fox_base.png')


# Spawn player
def player(x, y):
    game_display.blit(character, (x, y))


# Game loop
x = (display_width * 0.45)
y = (display_height * 0.8)
game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        # Left right movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x += -0.015
            if event.key == pygame.K_RIGHT:
                x += 0.015

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass

        # Up Down movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y += -0.015
            if event.key == pygame.K_DOWN:
                y += 0.015

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass

    game_display.fill(black)
    player(x, y)
    pygame.display.update()

pygame.quit()
