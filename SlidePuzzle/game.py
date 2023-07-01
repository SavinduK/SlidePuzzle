import pygame
import random
import math

pygame.init()
win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Slide Puzzle")
run = True
clock = pygame.time.Clock()

x,y = -1,-1
selected = False
selected_block = [-1,-1]
empty_block = [2,2]

img_1 = pygame.image.load("Assets/0.jpg")
img_1 = pygame.transform.scale(img_1,(200,200))
img_2 = pygame.image.load("Assets/1.jpg")
img_2 = pygame.transform.scale(img_2,(200,200))
img_3 = pygame.image.load("Assets/2.jpg")
img_3 = pygame.transform.scale(img_3,(200,200))
img_4 = pygame.image.load("Assets/3.jpg")
img_4 = pygame.transform.scale(img_4,(200,200))
img_5 = pygame.image.load("Assets/4.jpg")
img_5 = pygame.transform.scale(img_5,(200,200))
img_6 = pygame.image.load("Assets/5.jpg")
img_6 = pygame.transform.scale(img_6,(200,200))
img_7 = pygame.image.load("Assets/6.jpg")
img_7 = pygame.transform.scale(img_7,(200,200))
img_8 = pygame.image.load("Assets/7.jpg")
img_8 = pygame.transform.scale(img_8,(200,200))
img_9 = pygame.image.load("Assets/8.jpg")
img_9 = pygame.transform.scale(img_9,(200,200))

img_list = [img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8]

#0-empty
game_list = [1,2,3,4,5,6,7,8]
random.shuffle(game_list)

game_grid = [
    [game_list[0],game_list[1],game_list[2]],
    [game_list[3],game_list[4],game_list[5]],
    [game_list[6],game_list[7],0]
    ]

print(game_grid)              


def draw():
    for i in range(0,3):
        for j in range(0,3):
            if not game_grid[j][i] == 0:
                win.blit(img_list[game_grid[j][i]-1],(i*200,j*200))

while run :
    clock.tick(60)
    win.fill("black")
    draw()
    pygame.display.update()
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            a,b = pygame.mouse.get_pos()
            x = int(b/200)
            y = int(a/200)
            print(x,y)

             
            if selected == False:
                
                for i in range(0,3):
                    for j in range(0,3):
                        if  game_grid[j][i] == 0:
                            empty_block[0],empty_block[1] = j,i

                if x == empty_block[0]-1 and y == empty_block[1] :
                    print("selected")
                    selected = True
                    selected_block = [x,y]
                    
                elif  x ==  empty_block[0]+1 and y == empty_block[1] :
                    print("selected")
                    selected = True
                    selected_block =[x,y]
                    
                elif y == empty_block[1]-1 and x == empty_block[0]: 
                        print("selected")
                        selected = True
                        selected_block = [x,y]

                elif  y ==  empty_block[1]+1 and x == empty_block[0]:
                     print("selected")
                     selected = True
                     selected_block = [x,y]

                print("grid",game_grid,"empty",empty_block,"sel",selected_block)
                        
            elif selected == True :
                move = False
                if x == empty_block[0] :
                    if  y == empty_block[1]:
                        print("move")
                        move = True
                        
                if move == False :
                    selected = False
                    selected_block = [-1,-1]

               
                if move :
                   game_grid[empty_block[0]][empty_block[1]] = game_grid[selected_block[0]][selected_block[1]] 
                   game_grid[selected_block[0]][selected_block[1]] = 0
                   selected_block = [-1,-1]
                   selected = False
                   
                print("grid",game_grid,"empty",empty_block,"sel",selected_block)
                   
                    

                            
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
              game_grid = [
                        [1,2,3],
                        [4,5,6],
                        [7,8,0]]
          x,y = -1,-1
          selected = False
          selected_block = [-1,-1]
          empty_block = [2,2]


          if event.key == pygame.K_s:
                random.shuffle(game_list)
                game_grid = [
                    [game_list[0],game_list[1],game_list[2]],
                    [game_list[3],game_list[4],game_list[5]],
                    [game_list[6],game_list[7],0]]
                print(game_grid)
                x,y = -1,-1
                selected = False
                selected_block = [-1,-1]
                empty_block = [2,2]

            
