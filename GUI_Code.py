class CActor:
    x=0 #postion of the square in x-axis
    y=0 #postion of the square in y-axis
    ht=70 #height of the square
    wd=70 #width of the square
    type=0 # type 0 for normal square - 1 for start and end squares - 2 for walls that stops the search
# Importing the library
import pygame
import sys

n=8
thisList=[]
largeList=[]
# creating the 2D List of objects from type CActor
for r in range(n):
    for c in range(n):
        act = CActor()

        act.x= act.x + ( c * act.wd)
        act.y= act.y + ( r * act.ht)


        thisList.append(act)


    largeList.append(thisList)
    thisList = []

# Initializing Pygame
pygame.init()
SCREEN_HEIGHT = 620
SCREEN_WIDTH = 620
# Initializing surface
surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # size of the window

# Initialing Color
normal_color = (100, 88, 99)
startAndend_color = (255,0,0)
wall_color=(100,50,0)

ctClicks=0
# infinite loop to display the game
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        # check if user click the mouse button and we use it to know the Start and End of search
        if event.type == pygame.MOUSEBUTTONDOWN:
            # the user have only two clicks one for Start and the second one for End
            if ctClicks <2:
                ctClicks+=1
                # check if user click the mouse button in the area of the board not outside
                if pygame.mouse.get_pos()[1] < n*70 and pygame.mouse.get_pos()[0] < n*70:
                    # tring to find the selected square that the user clicked on it and change its type to 1
                    for x in largeList:
                        for i in range(n):
                            if pygame.mouse.get_pos()[0] > x[i].x and pygame.mouse.get_pos()[0] < x[i].x +x[i].wd and pygame.mouse.get_pos()[1] >x[i].y and pygame.mouse.get_pos()[1] <x[i].y +x[i].ht:
                                x[i].type=1
        # check if user click any button and we use it to put walls
        if event.type == pygame.KEYDOWN:
            # check if user click the mouse button in the area of the board not outside
            if pygame.mouse.get_pos()[1] < n * 70 and pygame.mouse.get_pos()[0] < n * 70:
                # tring to find the selected square that the user clicked on it and change its type to 1
                for x in largeList:
                    for i in range(n):
                        if pygame.mouse.get_pos()[0] > x[i].x and pygame.mouse.get_pos()[0] < x[i].x + x[i].wd and pygame.mouse.get_pos()[1] > x[i].y and pygame.mouse.get_pos()[1] < x[i].y + x[i].ht:
                            x[i].type = 2

    # Drawing Squares
    for x in largeList:
        for i in range(n):
            if x[i].type == 0:
                pygame.draw.rect(surface, normal_color, pygame.Rect(x[i].x, x[i].y, x[i].wd-2, x[i].ht-2))
            elif x[i].type == 1:
                pygame.draw.rect(surface, startAndend_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            else:
                pygame.draw.rect(surface, wall_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))

#khalid

    pygame.display.flip()

#helllooo