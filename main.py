import pygame
#WELCOME
#PROPERTY OF APE STUDIOS(2023)
#no its not

#DO NOT TOUCH
pygame.init()
screen_size = (1920,1810)
screen = pygame.display.set_mode(screen_size) 
running = True
controls = pygame.transform.scale(pygame.image.load("assets/controls.png"),(2000,1000))
#you can touch now

#the studio variable
#basically means if 
#its gonna show the
#studio intro.
#i turned it to false
#so that it cuts straight to the game
studio = False
#list of frames in the studio intro
apes = ["assets/studio/1.png","assets/studio/2.png","assets/studio/3.png","assets/studio/3.png","assets/studio/4.png","assets/studio/5.png"]
#fills the screen to make sure the background doesnt show in the intro
screen.fill((26,19,22))
counter = 0

#just loads assets(load your assets here)
#titlescreen is like studio var
titlescreen = False
titletext = pygame.transform.scale(pygame.image.load("assets/titlescreen/text.png"),(1000,100))
background = pygame.transform.scale(pygame.image.load("assets/titlescreen/background.png"),(2000,1000))
pplleeaasseeee = pygame.transform.scale(pygame.image.load("assets/titlescreen/enter.png"),(400,120))
#like the studio var but not
game = True
you = pygame.transform.scale(pygame.image.load("assets/you/normal_u.png"),(225,425))
#DECLARE YOUR VARIABLES HERE
stage = -1
x = 1500
y = 340
dialogue = False
talking = -1
right = False
left = False
down = False
up = False
canGoDown = False
walking = ["assets/you/walk1.png","assets/you/walk2.png"]
r_step_counter = 0
l_step_counter = 0
bedroom = pygame.transform.scale(pygame.image.load("assets/house/bedroom1.png"),(2000,1000))
stairs = pygame.transform.scale(pygame.image.load("assets/house/stairs.png"),(2000,1000))
living = pygame.transform.scale(pygame.image.load("assets/house/living1.png"),(3000,1000))
#all speech bubble things
speech = ["assets/parents/mom.png",
          "assets/you/sleep.png",
          "assets/you/sound.png"]

#the talk function. thats how you talk
def talk():
    global talking
    screen.blit(pygame.transform.scale(pygame.image.load(speech[talking]),(800,400)),(575,550))

#sets fps
clock = pygame.time.Clock()
clock.tick(15)

#actual game code in the loop
while running:
    #key presses and events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if titlescreen == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    titlescreen = False
                    game = True

        #TODO: add up arrow to function on stairs :)
        elif game == True:
            if dialogue == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and dialogue == True:
                        stage += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    left = True
                    l_step_counter += 1
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    right = True
                    r_step_counter += 1
                if event.key == pygame.K_DOWN and canGoDown:
                    down = True
                if event.key == pygame.K_UP and canGoDown:
                    up = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    l_step_counter = 0
                    left = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    r_step_counter = 0
                    right = False
                if event.key == pygame.K_DOWN and canGoDown:
                    down = False
                if event.key == pygame.K_UP and canGoDown:
                    down = True
    #for walk animation
    if r_step_counter != 0:
        r_step_counter += 1
        if r_step_counter == 2:
            you = pygame.transform.scale(pygame.image.load(walking[0]),(225,425))
        if r_step_counter == 20:
            you = pygame.transform.scale(pygame.image.load(walking[1]),(225,425))
        elif r_step_counter == 40:
            you = pygame.transform.scale(pygame.image.load(walking[0]),(225,425))
            r_step_counter = 1
    #another walk anim
    if l_step_counter != 0:
        l_step_counter += 1
        if l_step_counter == 2:
            you = pygame.transform.flip(pygame.transform.scale(pygame.image.load(walking[0]),(225,425)), True, False)
        if l_step_counter == 20:
            you = pygame.transform.flip(pygame.transform.scale(pygame.image.load(walking[1]),(225,425)), True, False)
        elif l_step_counter == 40:
            you = pygame.transform.flip(pygame.transform.scale(pygame.image.load(walking[0]),(225,425)), True, False)
            l_step_counter = 1
    #fuck DRY(Dont Repeat Yourself)

    #changes x and y coord for walking
    if right == True:
        x += 7
    elif left == True:
        x -= 7
    elif right != True and left != True:
        you = pygame.transform.scale(pygame.image.load("assets/you/normal_u.png"),(225,425))
    if down == True:
        y += 7
    elif up == True:
        y -= 7

    #for studio
    if studio == True:
        counter += 5
        if counter == 5:
            screen.blit(pygame.transform.scale(pygame.image.load(apes[0]),(2000,1000)),(-150,0))
        elif counter == 1000:
            screen.blit(pygame.transform.scale(pygame.image.load(apes[1]),(2000,1000)),(-150,0))
        elif counter == 2000:
            screen.blit(pygame.transform.scale(pygame.image.load(apes[2]),(2000,1000)),(-150,0))
        elif counter == 3000:
            screen.blit(pygame.transform.scale(pygame.image.load(apes[3]),(2000,1000)),(-150,0))
        elif counter == 4000:
            screen.blit(pygame.transform.scale(pygame.image.load(apes[4]),(2000,1000)),(-150,0))
        elif counter == 5000:
            screen.blit(pygame.transform.scale(pygame.image.load(apes[5]),(2000,1000)),(-150,0))
        elif counter == 5005:
            counter = 0
            studio = False
            titlescreen = True

    #titlescreen
    if titlescreen == True:
        screen.blit(background, (-80,0))
        screen.blit(titletext, (500,250))
        screen.blit(pplleeaasseeee, (800,600))

    #the game is divided in "stages". each stage is separated by dialogue and rooms
    elif game == True:
        if stage == -1:
            counter += 1
            if counter != 1: #TODO: turn to 200 when dev is up
                screen.blit(controls,(-80,0))
            else:
                stage += 1
        else:
            if stage == 0:
                talking = 0
                screen.blit(bedroom,(-40,0))
                screen.blit(you,(x,y))
                dialogue = True
                talk()
            elif stage == 1:
                talking = 1
                bedroom = pygame.transform.scale(pygame.image.load("assets/house/bedroom2.png"),(2000,1000))
                screen.blit(bedroom,(-40,0))
                screen.blit(you,(x,y))
                dialogue = True
                counter = 0
                talk()
            elif stage == 2:
                counter += 1
                dialogue = False
                screen.blit(bedroom,(-40,0))
                screen.blit(you,(x,y))
                if counter == 1:
                    stage += 1
            elif stage == 3:
                talking = 2
                dialogue = True
                screen.blit(bedroom,(-40,0))
                screen.blit(you,(x,y))
                talk()
            elif stage == 4:
                dialogue = False
                if x <= 150:
                    stage += 1
                    if stage == 5:
                        x = 1810
                        y = 400
                screen.blit(bedroom,(-40,0))
                screen.blit(you,(x,y))
            elif stage == 5:
                if x > 116 and x < 438:
                    canGoDown = True
                else:
                    canGoDown = False
                if y > 600:
                    stage += 1
                    canGoDown = False
                screen.blit(stairs,(0,0))
                screen.blit(you,(x,y))
            elif stage == 6:
                screen.blit(living, (0,5))
                screen.blit(you,(x,500))

    pygame.display.flip()