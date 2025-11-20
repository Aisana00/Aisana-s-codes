import pygame
import math
pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

draw_mode = 0  # Current shape mode

# List to store all drawn shapes
shapes_drawn = []  # Each shape: (draw_mode, color, pos)

class drawing(object):
    def __init__(self):
        self.color = (0, 0, 0)  # Default color is black
        self.width = 10
        self.height = 10
        self.rad = 6  

    # Add a shape to the list
    def draw(self, win, pos):
        global draw_mode
        shapes_drawn.append((draw_mode, self.color, pos))

    # Draw all shapes from the list
    def draw_all(self, win):
        for mode, color, pos in shapes_drawn:
            if mode == 0:  # Circle
                pygame.draw.circle(win, color, pos, self.rad)
            elif mode == 1:  # Square
                pygame.draw.rect(win, color, (pos[0], pos[1], 50, 50))
            elif mode == 2:  # Right triangle
                points = [
                    (pos[0], pos[1]),
                    (pos[0] - 25, pos[1] + 50),
                    (pos[0] + 25, pos[1] + 50)
                ]
                pygame.draw.polygon(win, color, points)
            elif mode == 3:  # Equilateral triangle
                side_length = 50
                height = side_length * math.sqrt(3) / 2
                points = [
                    (pos[0], pos[1]),
                    (pos[0] - side_length / 2, pos[1] + height),
                    (pos[0] + side_length / 2, pos[1] + height)
                ]
                pygame.draw.polygon(win, color, points)
            elif mode == 4:  # Rhombus
                points = [
                    (pos[0], pos[1] - 25),
                    (pos[0] + 25, pos[1]),
                    (pos[0], pos[1] + 25),
                    (pos[0] - 25, pos[1])
                ]
                pygame.draw.polygon(win, color, points)
            # Eraser
            if color == (255, 255, 255):
                pygame.draw.circle(win, color, pos, 20)

    # Handle mouse clicks
    def click(self, win, list_buttons):
        global draw_mode
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and pos[0] < 400 and pos[1] > 25:
            self.draw(win, pos)  # Add shape to the list
        elif pygame.mouse.get_pressed()[0]:
            # Color buttons
            for button in list_buttons:
                if button.x < pos[0] < button.x + button.width and button.y < pos[1] < button.y + button.height:
                    self.color = button.color2
            # Shape buttons
            if 407 <= pos[0] <= 447 and 214 <= pos[1] <= 254: draw_mode = 0
            elif 453 <= pos[0] <= 493 and 214 <= pos[1] <= 254: draw_mode = 1
            elif 407 <= pos[0] <= 447 and 260 <= pos[1] <= 300: draw_mode = 2
            elif 453 <= pos[0] <= 493 and 260 <= pos[1] <= 300: draw_mode = 3
            elif 407 <= pos[0] <= 447 and 306 <= pos[1] <= 346: draw_mode = 4


class button(object):
    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color  # Border color
        self.outline = outline  # Border thickness
        self.color2 = color2  # Main button color
        self.action = action  # Button action (unused here)
        self.text = text  # Button text

    # Draw button with text
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.outline)
        font = pygame.font.SysFont('Arial', 12)
        # Text for shape buttons
        if self.x == 407 and self.y == 214: win.blit(font.render('Circle', True, (0,0,0)), (self.x + 5, self.y + 15))
        elif self.x == 453 and self.y == 214: win.blit(font.render('Square', True, (0,0,0)), (self.x + 5, self.y + 15))
        elif self.x == 407 and self.y == 260: win.blit(font.render('R-Tri', True, (0,0,0)), (self.x + 5, self.y + 15))
        elif self.x == 453 and self.y == 260: win.blit(font.render('E-Tri', True, (0,0,0)), (self.x + 5, self.y + 15))
        elif self.x == 407 and self.y == 306: win.blit(font.render('Rhomb', True, (0,0,0)), (self.x + 5, self.y + 15))


# Initialize drawing object
drawing1 = drawing()

# Color buttons
blueButton = button(407, 30, 40, 40, (0,0,255), (0,0,255))
redButton = button(453, 30, 40, 40, (255,0,0), (255,0,0))
greenButton = button(407, 76, 40, 40, (0,255,0), (0,255,0))
orangeButton = button(453, 76, 40, 40, (255,192,0), (255,192,0))
yellowButton = button(407, 122, 40, 40, (255,255,0), (255,255,0))
purpleButton = button(453, 122, 40, 40, (112,48,160), (112,48,160))
blackButton = button(407, 168, 40, 40, (0,0,0), (0,0,0))
whiteButton = button(453, 168, 40, 40, (0,0,0), (255,255,255), 1)  # Eraser

# Shape buttons
circleButton = button(407, 214, 40, 40, (0,0,0), (200,200,200), 1)
squareButton = button(453, 214, 40, 40, (0,0,0), (200,200,200), 1)
rightTriangleButton = button(407, 260, 40, 40, (0,0,0), (200,200,200), 1)
equilateralTriangleButton = button(453, 260, 40, 40, (0,0,0), (200,200,200), 1)
rhombusButton = button(407, 306, 40, 40, (0,0,0), (200,200,200), 1)

# List of all buttons
Buttons_color = [
    blueButton, redButton, greenButton, orangeButton,
    yellowButton, purpleButton, blackButton, whiteButton,
    circleButton, squareButton, rightTriangleButton,
    equilateralTriangleButton, rhombusButton
]

# Draw everything on screen
def draw(win):
    drawing1.click(win, Buttons_color)  # Handle mouse clicks
    drawing1.draw_all(win)  # Draw all shapes
    for button in Buttons_color:
        button.draw(win)  # Draw buttons
    font = pygame.font.SysFont('Arial', 16)
    modes = ['Circle', 'Square', 'Right Triangle', 'Equilateral Triangle', 'Rhombus']
    win.blit(font.render(f'Current: {modes[draw_mode]}', True, (0,0,0)), (410, 500))  # Show current mode
    pygame.display.update()  


# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Clear screen
    draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False

pygame.quit()
