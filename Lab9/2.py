import pygame
from random import randrange
pygame.init()

RES = 800
SIZE = 50


x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

# List of possible food values (weights)
FOOD_VALUES = [1, 2, 3]   # 1 = common, 3 = rare

# Generate first food
food_value = 1
food_timer = 0
food_max_time = 120        # frames until food disappears
food = randrange(0, RES, SIZE), randrange(0, RES, SIZE)


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


# Function to spawn new food 
def spawn_food():
    global food, food_value, food_timer
    food = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
    food_value = FOOD_VALUES[randrange(0, len(FOOD_VALUES))]
    food_timer = 0  # reset life timer



running = True
while running:
    screen.fill(pygame.Color("black"))

    # Draw snake
    [pygame.draw.rect(screen, pygame.Color("green"), (i, j, SIZE - 2, SIZE - 2)) for i, j in snake]

    # Choose food color based on value
    food_color = "red" if food_value == 1 else "yellow" if food_value == 2 else "purple"

    # Draw food
    pygame.draw.rect(screen, pygame.Color(food_color), (*food, SIZE, SIZE))

    render_score = font_score.render(f"SCORE: {score}", 1, pygame.Color("orange"))
    screen.blit(render_score, (5, 5))

    render_level = font_level.render(f"LEVEL: {level}", 1, pygame.Color("orange"))
    screen.blit(render_level, (5, 30))


    # Move Snake 
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    #  Food Timer
    food_timer += 1
    if food_timer > food_max_time:
        spawn_food()  # food disappears and respawns


    #  Eating food 
    if snake[-1] == food:
        length += 1
        score += food_value
        spawn_food()

        # Level up every 4 score
        if score % 4 == 0:
            level += 1
            fps += 0.5


    #  Collision Check 
    if (
        x < 0 or x > RES - SIZE or
        y < 0 or y > RES - SIZE or
        len(snake) != len(set(snake))  # snake hits itself
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


    #  Keyboard Controls 
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
