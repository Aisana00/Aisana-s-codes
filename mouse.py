import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 800, 800
center_x = WIDTH // 2
center_y = HEIGHT // 2
BG_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("images/main-clock.png")
hand_left = pygame.image.load("images/left-hand1.png")
hand_right = pygame.image.load("images/right-hand1.png")

clock_rect = background.get_rect()

def draw_rotated(surface, img, pos, angle):
    rotated = pygame.transform.rotate(img, angle)
    rect = rotated.get_rect(center=img.get_rect(center=pos).center)
    surface.blit(rotated, rect)

angle_left = 0
angle_right = 0

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            exit()

    now = datetime.datetime.now()
    minute_angle = now.minute * 6 - 90
    second_angle = now.second * 6 - 90

    screen.fill(BG_COLOR)
    screen.blit(background, (center_x, center_y))
    screen.blit(background, clock_rect)

    draw_rotated(screen, hand_left, (center_x, center_y), -second_angle)
    draw_rotated(screen, hand_right, (center_x, center_y), -minute_angle)

    pygame.display.update()
