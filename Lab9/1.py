import pygame, random, time
pygame.init()
FPS = pygame.time.Clock()


W, H = 400, 600
SPEED = 5                  # Enemy speed
SCORE = 0                  # Player score

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")

font = pygame.font.SysFont("Verdana", 60)      
font_small = pygame.font.SysFont("Verdana", 20)  
game_over = font.render("Game Over", True, (0, 0, 0))

background = pygame.image.load("images/race.jpg")
background = pygame.transform.scale(background, (W, H))


# Enemy 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/redcar.jpg")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        # Move enemy downward
        self.rect.move_ip(0, SPEED)

        # Respawn enemy at top when leaving screen
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)


# Coin 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.new_coin()

    def new_coin(self):
        # Random coin value: 1 = common, 2 = rare, 3 = very rare
        self.value = random.choice([1, 2, 3])

        img = pygame.image.load("images/coin.jpg")

        # Bigger coin for higher value
        size = 30 + self.value * 5
        self.image = pygame.transform.scale(img, (size, size))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # Respawn coin if it goes off screen
        if self.rect.top > H:
            self.new_coin()

        # Check collision with player
        if self.rect.colliderect(P1.rect):
            SCORE += self.value     # Add coin value to score
            self.new_coin()


#  Player 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/bluecar.jpg")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        # Move right
        if keys[pygame.K_RIGHT] and self.rect.right < W:
            self.rect.move_ip(5, 0)



E1 = Enemy()
P1 = Player()
C1 = Coin()

enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

enemies.add(E1)
coins.add(C1)
all_sprites.add(E1, P1, C1)

pygame.mixer.Sound("music/background.wav").play(-1)


#  Main Game Loop 
running = True
b_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw scrolling background
    screen.blit(background, (0, b_y))
    screen.blit(background, (0, b_y - H))

    # Increase enemy speed every 5 score
    if SCORE != 0 and SCORE % 5 == 0:
        SPEED = 5 + SCORE // 5

    # Draw score
    scores = font_small.render(str(SCORE), True, (0, 0, 0))
    screen.blit(scores, (370, 10))

    # Draw and move all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Check collision with enemy → Game Over
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("music/crash.wav").play()
        time.sleep(0.5)

        screen.fill(pygame.Color("red"))
        screen.blit(game_over, (30, 250))
        pygame.display.update()

        # Remove all sprites
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        exit()

    # Background scrolling
    b_y += 5
    if b_y > H:
        b_y = 0

    pygame.display.flip()
    FPS.tick(60)
