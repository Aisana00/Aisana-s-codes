import pygame
from random import randrange

pygame.init()


RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {"UP": True, "LEFT": True, "DOWN": True, "RIGHT": True}
length = 1
snake = [(x, y)]
dx, dy = 1, 0 
score = 0
fps = 3        
level = 1

screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 26, bold=True)
font_end = pygame.font.SysFont("Arial", 66, bold=True)
font_level = pygame.font.SysFont("Arial", 26, bold=True)


running = True
while running:
    screen.fill(pygame.Color("black"))

    
    [pygame.draw.rect(screen, pygame.Color("green"), (i, j, SIZE - 2, SIZE - 2)) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color("red"), (*apple, SIZE, SIZE))

    
    render_score = font_score.render(f"SCORE: {score}", 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))
    render_level = font_level.render(f"LEVEL: {level}", 1, pygame.Color('orange'))
    screen.blit(render_level, (5, 30))

    
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        if score % 4 == 0:  
            level += 1
            fps += 0.5  

    
    if (
        x < 0 or x > RES - SIZE or
        y < 0 or y > RES - SIZE or
        len(snake) != len(set(snake))
    ):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps) 

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dirs["UP"]:
                dx, dy = 0, -1
                dirs = {"UP": True, "LEFT": True, "DOWN": False, "RIGHT": True}
            if event.key == pygame.K_DOWN and dirs["DOWN"]:
                dx, dy = 0, 1
                dirs = {"UP": False, "LEFT": True, "DOWN": True, "RIGHT": True}
            if event.key == pygame.K_LEFT and dirs["LEFT"]:
                dx, dy = -1, 0
                dirs = {"UP": True, "LEFT": True, "DOWN": True, "RIGHT": False}
            if event.key == pygame.K_RIGHT and dirs["RIGHT"]:
                dx, dy = 1, 0
                dirs = {"UP": True, "LEFT": False, "DOWN": True, "RIGHT": True}
