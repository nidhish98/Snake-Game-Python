import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
blue=(0,0,155)
red=(255,0,0)
green=(0,155,0)

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snaky Game!Back to childhood and nokia 3301')


block_size=20.0

direction="right"
clock=pygame.time.Clock()
FPS=15

font=pygame.font.SysFont(None,25)

img=pygame.image.load('snake1.png')

score=0
direction="right"
def snake(block_size,snake_list):
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = pygame.transform.rotate(img,0)
    if direction=="down":
        head = pygame.transform.rotate(img,180)

    gameDisplay.blit(head,(snake_list[-1][0],snake_list[-1][1]))

    for XnY in snake_list[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()

def message_to_screen(msg,color):
    textSurf,textRect =  text_objects(msg,color)
    textRect.center=(display_width/2),(display_height/2)
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    

def score_display(txt,color):
    score_text=font.render(txt,True,color)
    gameDisplay.blit(score_text,[300,500])


def gameLoop():
    global direction
    global score
    #flag=random.randrange(0,1)
    flag=1
    gameExit = False
    gameOver = False
    
    lead_x=display_height/2
    lead_y=display_width/2

    lead_x_change=0
    lead_y_change=0

    snake_List=[]
    snakeLength=1
    randAppleX=round(random.randrange(0,display_width-block_size)/block_size)*block_size
    randAppleY=round(random.randrange(0,display_height-block_size)/block_size)*block_size
    randX=random.randrange(0,display_width-10)
    randY=random.randrange(0,display_height-10)
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over,Press C to play again,Q to Quit",red)
            score_display("Final Score:"+str(score),blue)   
            pygame.display. update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False  
                    elif event.key == pygame.K_c:
                        score=0
                        gameLoop()           

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if(direction != "right"):
                        direction = "left"
                        lead_x_change = -block_size
                        lead_y_change=0
                elif event.key == pygame.K_RIGHT:
                    if(direction != "left"):
                        direction = "right"
                        lead_x_change = block_size
                        lead_y_change=0
                elif event.key == pygame.K_UP:
                    if(direction != "down"):                    
                        direction = "up"
                        lead_y_change = -block_size
                        lead_x_change=0
                elif event.key == pygame.K_DOWN:
                    if(direction != "up"):
                        direction = "down"
                        lead_y_change = block_size
                        lead_x_change=0

        if lead_x >= display_width :
            lead_x = 0
        if lead_x < 0:
            lead_x = display_width
        if lead_y >= display_height :
            lead_y = 0
        if lead_y < 0:
            lead_y=display_height
            
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(black)

        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,block_size,block_size])
        if lead_x == randAppleX and lead_y == randAppleY:
            print("om om om")
            randAppleX=round(random.randrange(0,display_width-block_size)/block_size)*block_size
            randAppleY=round(random.randrange(0,display_height-block_size)/block_size)*block_size
            snakeLength+=1
            score+=10
 
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snake_List.append(snakeHead)
        if(len(snake_List)>snakeLength):
            del snake_List[0]
        for eachSegment in snake_List[:-1]:
           if eachSegment == snakeHead:
                gameOver = True

    
        score_text="Score:"+str(score)
        score_display(score_text,blue)
        gameDisplay.blit(font.render("Level 1",True,blue),[300,10])
        snake(block_size,snake_List)
        pygame.display.update()

      
        #gameDisplay.fill(red,rect=[200,200,50,50])

        
        clock.tick(FPS)
            
    pygame.quit()
    quit()

gameLoop()
