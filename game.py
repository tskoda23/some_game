import pygame

pygame.init()

window_width = 1217
window_height = 533
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R.png'), pygame.image.load('R.png'), pygame.image.load('R.png'), pygame.image.load('R.png'), pygame.image.load(
    'R.png'), pygame.image.load('R.png'), pygame.image.load('R.png'), pygame.image.load('R.png'), pygame.image.load('R.png')]
walkLeft = [pygame.image.load('L.png'), pygame.image.load('L.png'), pygame.image.load('L.png'), pygame.image.load('L.png'), pygame.image.load(
    'L.png'), pygame.image.load('L.png'), pygame.image.load('L.png'), pygame.image.load('L.png'), pygame.image.load('L.png')]

bg = pygame.image.load('level1.png')
char = [pygame.image.load('guy.png'), pygame.image.load('guy2.png'), pygame.image.load('guy3.png')]

jump = pygame.mixer.Sound('jump.wav')
maintheme = pygame.mixer.music.load('flow.mp3')
pygame.mixer.music.play(-1)
x = 50
y = 400
width = 40
height = 60
vel = 10

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0
guy_anim = 0
yspeed = 10


def redrawGameWindow():
    global walkCount
    global guy_anim

    win.blit(bg, (0, 0))
    if(guy_anim) + 1>=3:
    	guy_anim = 0
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char[guy_anim], (x, y))
        guy_anim +=1
        walkCount = 0

    pygame.display.update()


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < window_width - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            jump.play()
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()


pygame.quit()
