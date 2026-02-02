import pygame
import time
#setup
pygame.init()

pygame.display.set_caption('Open whiteboard')
screen = pygame.display.set_mode((2560, 1440))

#clock self explanatory
clock = pygame.time.Clock()

#create saved coordinates lists
blocks = []

#load images
bluebutton = pygame.image.load('bluebutton.png')
redbutton = pygame.image.load('redbutton.png')
eraserbutton = pygame.image.load('eraser.png')
greenbutton = pygame.image.load('greenbutton.png')
tipsbutton = pygame.image.load('TIPS.png')

#str's
current_color = "blue"

#int's
size = 30

#bools
nextframe = True
running = True
pygame.mouse.set_visible(False)
tips = True

while running:
    #check of mouse down
    mouse_clicked = pygame.mouse.get_pressed()[0]

    #get mouse pointer coordinates
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    #draw
    for tempx, tempy, color, tempsize in blocks:
        if color == "blue":
            pygame.draw.rect(screen, (0, 0, 255), (tempx-15, tempy-15, tempsize, tempsize))
        elif color == "red":
            pygame.draw.rect(screen, (255, 0, 0), (tempx-15, tempy-15, tempsize, tempsize))
        elif color == "white":
            pygame.draw.rect(screen, (255, 255, 255), (tempx-15, tempy-15, tempsize, tempsize))
        elif color == "green":
            pygame.draw.rect(screen, (0, 255, 0), (tempx-15, tempy-15, tempsize, tempsize))
        else:
            raise ValueError(f"Unsupported color: {color}")      

    #event handler
    for event in pygame.event.get():
        
        #change color
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:
                print("E PRESSED")
                if current_color == "blue":
                    current_color = "red"
                elif current_color == "red":
                    current_color = "green"
                elif current_color == "green":
                    current_color = "white"
                elif current_color == "white":
                    current_color = "blue"

            #reset canvas
            elif event.key == pygame.K_SPACE:
                blocks = []

            #hide tip
            elif event.key == pygame.K_h:
                if tips == True:
                    tips = False

            #quit event
            elif event.key == pygame.K_ESCAPE:
                running = False
            
            #size changer
            elif event.key == pygame.K_t:
                size += 10
            elif event.key == pygame.K_r:
                size -= 10

    #show tips button
    if tips == True:
        screen.blit(tipsbutton, (1000, 0))
    else:
        pass
    
    #save block states at mouse click
    if mouse_clicked == True:
        blocks.append((x, y, current_color, size))
    else:
        pass
    
    #cursor
    if current_color == "blue":
        bluecursorrect = pygame.draw.rect(screen, (0, 0, 255), (x-15, y-15, size, size))
        screen.blit(bluebutton, (0, 0))
    elif current_color == "red":
        redcursorrect = pygame.draw.rect(screen, (255, 0, 0), (x-15, y-15, size, size))
        screen.blit(redbutton, (0, 0))
    elif current_color == "green":
        redcursorrect = pygame.draw.rect(screen, (0, 255, 0), (x-15, y-15, size, size))
        screen.blit(greenbutton, (0, 0))
    else:
        whitecursorrect = pygame.draw.rect(screen, (0, 0, 0), (x-15, y-15, size, size))
        screen.blit(eraserbutton, (0, 0))

    

    #end setup
    pygame.display.update()
     
    clock.tick(1000)
    screen.fill((255, 255, 255))