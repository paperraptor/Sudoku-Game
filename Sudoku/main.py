import sudoku
from sudoku import *

def drawNum(s, s_font, screen, error, checking):
    num_x = 95
    num_y = 78
    index = getNum(num_x-10, num_y)
    color = GREY
    for row in s.grid:
        for col in row:
            index = getNum(num_x-10, num_y)
            if col != 0:
                if checking == True and index in error:
                    color = RED
                elif checking == True and index in s.empty:
                    color = GREEN                
                elif index in s.empty:
                    color = (136, 136, 136)
                else:
                    color = BLACK
                text_surface = s_font.render(str(col), False, color)
                screen.blit(text_surface, (num_x,num_y))
            num_x = num_x + 36
            
        num_y = num_y + 36
        num_x = 95

def drawGrid(screen):
    line_x = 90 + 30
    line_y = 78 + 38
    line_width = 1
    for i in range(8):
        if i == 2 or i == 5:
            line_width = 3
        else:
            line_width = 1
        pygame.draw.line(screen, BLACK, (line_x, 81), (line_x, 81+ 324), line_width)
        pygame.draw.line(screen, BLACK, (85, line_y), (85 + 324, line_y), line_width)
        line_x = line_x + 36
        line_y = line_y + 36    

def getNum(x, y):
    if (x < 85 or y < 78 or x > 85+324 or y > 78+324):
        return False
    x = int((x - 85)/36)
    y = int((y - 78)/36)
    return(y,x)

def drawShade(screen, mouse):
    if (mouse[0] < 85 or mouse[1] < 78 or mouse[0] > 85+324 or mouse[1] > 78+324):
        return
    rect_x = int(85 + int((mouse[0] - 85)/36)*36)
    rect_y = int(78 + int((mouse[1] - 78)/36)*36 + 3)
    pygame.draw.rect(screen, GREY, (rect_x, rect_y, 36, 36));

def mouseHover(screen, s):
    mouse = pygame.mouse.get_pos()
    drawShade(screen, mouse)

def click_getNumloc(screen):
    mouse = pygame.mouse.get_pos()
    if (mouse[0] < 85 or mouse[1] < 78 or mouse[0] > 85+324 or mouse[1] > 78+324):
        return False    
    
    rect_x = int(85 + int((mouse[0] - 85)/36)*36)
    rect_y = int(78 + int((mouse[1] - 78)/36)*36 + 3)
    pygame.draw.rect(screen, RED, (rect_x, rect_y, 36, 36), 2)
    return (rect_x, rect_y)

def getkeyPressed(event):
    #event = pygame.event.get()
    #for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            return 1
        elif event.key == pygame.K_2:
            return 2
        elif event.key == pygame.K_3:
            return 3
        elif event.key == pygame.K_4:
            return 4
        elif event.key == pygame.K_5:
            return 5
        elif event.key == pygame.K_6:
            return 6
        elif event.key == pygame.K_7:
            return 7
        elif event.key == pygame.K_8:
            return 8
        elif event.key == pygame.K_9:
            return 9
        elif event.key == pygame.K_c:
            return 'c'
        elif event.key == pygame.K_r:
            return 'r'        
    
    return -1

def enterAns(s, selected, event):
    if selected == False:
        return -1
    keyPressed = getkeyPressed(event)
    #print(keyPressed)
    if keyPressed == -1 or keyPressed == 'c' or keyPressed == 'r':
        return -1
    numIndex = getNum(selected[0], selected[1])
    if numIndex in s.empty:
        s.grid[numIndex[0]][numIndex[1]] = keyPressed
        #print(keyPressed)
        return s.grid
    return -1

def checkAns(s, event):
    error = []
    for x in range(9):
        for y in range(9):
            #print (s.grid[x][y], s.answer[x][y])
            if s.grid[x][y] != s.answer[x][y] and s.grid[x][y] != 0:
                error.append((x,y))
                #print (error)
    return error

def main():
    s = Sudoku()
    s.generateGrid()
    s.answer = copy.deepcopy(s.grid)
    s.generateQuestion(30)
    
    s.printGrid()
    print("")
    for row in s.answer:
        print(row)    
    print(s.empty)
    print("")
    pygame.init()
    pygame.font.init()
    
    screen = pygame.display.set_mode([500, 500])
    s_font = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()
    running = True
    selected = False
    error = []
    checking = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                checking = True
                error = checkAns(s, event)
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                #s = Sudoku()
                #error = []
                #selected = False
                #checking = False
                #s.empty = []
                #s.generateGrid()
                #s.answer = copy.deepcopy(s.grid)
                #s.generateQuestion(20)                
            elif event.type == pygame.KEYDOWN:
                checking = False
                ans = enterAns(s, selected, event)
                if ans != -1:
                    s.grid = ans                
        
        click = pygame.mouse.get_pressed()
        
        #refresh screen
        screen.fill((255, 255, 255))
        
        mouseHover(screen, s)
        
        #draw the numbers
        drawNum(s, s_font, screen, error, checking)
        
        #create the grid lines
        drawGrid(screen)
        
        if click[0]:
            selected = click_getNumloc(screen)
        if selected != False:
            pygame.draw.rect(screen, RED, (selected[0], selected[1], 36, 36), 2)
        
        #print(selected)
        #if selected != False:
            #n = getNum(selected[0], selected[1])
            #print(n)
        pygame.display.flip()
        clock.tick(60)
        
    
    pygame.quit()
    quit()
    
    #mainGame = App()
    #mainGame.on_execute()
    
if __name__ == "__main__" :
    main()