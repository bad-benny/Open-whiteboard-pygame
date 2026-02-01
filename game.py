import pygame
import sys

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
#str's
current_color = "blue"

#bools
nextframe = True
running = True
pygame.mouse.set_visible(False)

while running:
    #check of mouse down
    mouse_clicked = pygame.mouse.get_pressed()[0]

    #get mouse pointer coordinates
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    #draw
    for tempx, tempy, color in blocks:
        if color == "blue":
            pygame.draw.rect(screen, (0, 0, 255), (tempx-15, tempy-15, 30, 30))
        elif color == "red":
            pygame.draw.rect(screen, (255, 0, 0), (tempx-15, tempy-15, 30, 30))
        elif color == "white":
            pygame.draw.rect(screen, (255, 255, 255), (tempx-15, tempy-15, 30, 30))
        else:
            raise ValueError(f"Unsupported color: {color}")      

    #quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #change color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                print("E PRESSED")
                if current_color == "blue":
                    current_color = "red"
                elif current_color == "red":
                    current_color = "white"
                elif current_color == "white":
                    current_color = "blue"
        
            elif event.key == pygame.K_SPACE:
                blocks = []

        
    #save block states at mouse click
    if mouse_clicked == True:
        blocks.append((x, y, current_color))
        print(blocks)
    else:
        pass
    
    #cursor
    if current_color == "blue":
        bluecursorrect = pygame.draw.rect(screen, (0, 0, 255), (x-15, y-15, 30, 30))
        screen.blit(bluebutton, (0, 0))
    elif current_color == "red":
        redcursorrect = pygame.draw.rect(screen, (255, 0, 0), (x-15, y-15, 30, 30))
        screen.blit(redbutton, (0, 0))
    else:
        whitecursorrect = pygame.draw.rect(screen, (0, 0, 0), (x-15, y-15, 30, 30))
        screen.blit(eraserbutton, (0, 0))

    

    #end setup
    pygame.display.flip()
     
    clock.tick(240)
    screen.fill((255, 255, 255))