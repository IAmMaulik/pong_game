import pygame, sys

pygame.init()
clock = pygame.time.Clock()

# seeting up the window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

    # Updating the window
    pygame.display.flip()
    clock.tick(60)