import sys,pygame,random

pygame.init()
WindowWidth = 800
WindowHeight = 512
FPS = 30

CarWidth = WindowWidth/9
CarHeight = WindowHeight/4
RecWidth = WindowWidth/32
RecHeight = WindowHeight/16

STEP = 5

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

clock = pygame.time.load("Player.png")
road = pygame.time.load("Coin.png")
road = pygame.time.load("Road.png")

pygame.display.set_caption("CAR GAME")

DISPLAY = pygame.display.set_mode(WindowWidth,WindowHeight)

def gameloop():
    Carx,Cary = WindowWidth/2,WindowHeight/2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame == pygame.K_LEFT:
                   direction = -1
                elif event.key ==pygame.K_RIGHT:
                    direction = 1
                elif event.key ==pygame.K_UP:
                    direction = 0

                    if direction == -1:
                        Carx -=STEP
                    elif direction ==1:
                        Carx +=STEP

                    

                    DISPLAY.fill(white)
                    pygame.draw.rect(DISPLAY,black,[Carx,Cary,CarWidth,CarHeight])
                    pygame.display.update()

                    gameloop()
