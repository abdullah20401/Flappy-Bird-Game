import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,450))
    screen.blit(floor_surface, (floor_x_pos + 285,450))

pygame.init()
# screen = pygame.display.set_mode((576, 1024))
screen = pygame.display.set_mode((285, 512))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert()
# bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png')
# floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0,0))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -285:
        floor_x_pos = 0
    # screen.blit(floor_surface, (floor_x_pos,400))

    pygame.display.update()
    clock.tick(120)