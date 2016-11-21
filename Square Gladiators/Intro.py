def LiveGet():
    import pygame
    pygame.init()


    screensize = (640,480)
    screen = pygame.display.set_mode(screensize)
    titleImage = pygame.image.load('images/title.jpg')
    titleImage.convert()

    def textToScreen(message,x,y,size,color,center = True):
        font = pygame.font.Font(None, size)
        text = font.render(str(message), 1, color)
        if center == True:
            screen.blit(text,(text.get_rect(center = (x,y))))
        else:
            screen.blit(text, (x,y))

    running = True
    stage1 = True
    stage2 = False
    x = 0
    box1 = pygame.Rect(0,0,50,50)
    box1.center = (screensize[0]/4 * 0 + 80, screensize[1]/2)
    box2 = pygame.Rect(0,0,50,50)
    box2.center = (screensize[0]/4 * 1 + 80, screensize[1]/2)
    box3 = pygame.Rect(0,0,50,50)
    box3.center = (screensize[0]/4 * 2 + 80, screensize[1]/2)
    box4 = pygame.Rect(0,0,50,50)
    box4.center = (screensize[0]/4 * 3 + 80, screensize[1]/2)
    boxList = [box1, box2, box3, box4]
    numList = [1,3,5,10]
    while running:
        if stage1 == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    stage1 = False
            screen.fill((200,200,200))
            screen.blit(titleImage, (titleImage.get_rect(center = (screensize[0]/2, screensize[1]/2))))
            textToScreen('Press Any Button To Continue...', screensize[0]/2, screensize[1] -20, 32, (0,0,0))
            textToScreen('Artwork by: Peter Bignold', screensize[0] - 170, 0, 18, (50,50,50), False)
            pygame.display.update()
            x += 1
            if pygame.mouse.get_pressed()[0] == True:
                stage1 = False
        else:
            screen.fill((81,253,181))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 1:
                        return (1)
                    if event.key == 3:
                        return ( 3 )
                    if event.key == 5:
                        return ( 5) 
                    if event.key == 10:
                        return (10 )
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickPlace = pygame.mouse.get_pos()
                    for item in boxList:
                        if item.collidepoint(clickPlace):
                            if clickPlace[0] < 160:
                                return(1)
                            if clickPlace[0] > 160 and clickPlace[0] < 320:
                                return(3)
                            if clickPlace[0] > 320 and clickPlace[0] < 480:
                                return(5)
                            else:
                                return(10)
                iteration = 0
                
                for item in boxList:
                    if iteration >3:
                        break
                    pygame.draw.rect(screen, (17,109,162), item)
                    pygame.draw.rect(screen, (0,0,0), item, 1)
                    textToScreen(str(numList[iteration]), item.center[0], item.center[1], 21, (255,255,255))
                    iteration += 1
                textToScreen("How many Lives?", screensize[0]/2, 50, 45, (0,0,0))
                pygame.display.update()

                        
            
            
            
