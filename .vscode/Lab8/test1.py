import pygame, random, time
pygame.init()
FPS = pygame.time.Clock()

W, H = 400, 600
SPEED = 5
SCORE = 0
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))


background = pygame.image.load("images/race.jpg")
background = pygame.transform.scale(background, (W, H))


class Enemy(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()  
        self.image = pygame.image.load("images/redcar.jpg")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.jpg")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

        if self.rect.colliderect(P1.rect):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/bluecar.jpg")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
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


running = True
b_y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.blit(background, (0, b_y))
    screen.blit(background, (0, b_y - H))

    scores = font_small.render(str(SCORE), True, (0, 0, 0))
    screen.blit(scores, (10, 10))

   
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("music/crash.wav").play()
        time.sleep(0.5)
        screen.fill(pygame.Color("red"))
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        exit()

    
    b_y += 5
    if b_y > H:
        b_y = 0

    pygame.display.flip()
    FPS.tick(60)
