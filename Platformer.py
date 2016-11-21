def main():

    import pygame, random
    pygame.init()

    screensize = (640,480)
    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption('Platformer')
    white = (200,200,200)
    black = (10,10,10)
    clock = pygame.time.Clock()
    running = True
    def textToScreen(message,x,y,size,color,default = True):
        font = pygame.font.Font(None, size)
        text = font.render(str(message), 1, color)
        pygame.draw.rect(screen,white, (x,y,text.get_rect()[2],text.get_rect()[3]))
        if default == True:
            rect = text.get_rect()
            rect.center = (x,y)
            screen.blit(text,rect)
        else:
            screen.blit(text, (x,y))
        pygame.display.update((x,y,text.get_rect()[2], text.get_rect()[3]))
    class Player(object):
        def __init__(self,x,y):
            self.colour = (100,100,100)
            self.x = x
            self.y = y
            self.rect = pygame.Rect(x,y,25,25)
            self.direction = [0,-1]
            self.xspeed = 4
            self.yspeed = 8
            self.death = False
            
        def update(self,screen):
            if self.rect[0] - 3 < 0:
                if self.direction[0] == -1:
                    self.direction[0] = 0
            if self.rect[0] > screensize[0] - 25:
                if self.direction[0] == 1:
                    self.direction[0] = 0
            for platform in platformList:
                if self.rect.colliderect(platform):
                    if self.rect[1] < platform.rect[1]:
                        self.yspeed = 5
                    if self.rect[1] > platform.rect[1]:
                        self.yspeed = -1
                    if platform.isbreakable == True:
                        platform.destroy(screen)
            if self.rect[1]-25 == 0:
                self.death = True
            pygame.draw.rect(screen, white, self.rect)
            self.rect.move_ip(self.direction[0] * self.xspeed,
                           self.direction[1] * self.yspeed)
            pygame.draw.rect(screen, self.colour, self.rect)
            pygame.draw.rect(screen, (0,0,0), self.rect, 1)
            self.yspeed -= 0.1
            if self.rect[1] > 500:
                main()
            
            
    class Platform(object):
        def __init__(self,x,y,screen,moving,breakable):
            self.colour = (2,2,2)
            self.x = x
            self.y = y
            self.direction = [0,0]
            self.rect = pygame.Rect(x,y,100,20)
            self.ismoving = moving
            self.isbreakable = breakable
            self.xspeed = 0
            self.yspeed = 0
            self.sprite = pygame.image.load('images/platform.png').convert()
            if self.isbreakable:
                self.sprite = pygame.image.load('images/PlatformBreakable.png').convert()
            self.spriteClear = pygame.image.load('images/platformClear.png').convert()
            
        def update(self,screen):
            screen.blit(self.spriteClear, (self.rect[0],self.rect[1]))
            self.rect.move_ip(self.direction[0] * self.xspeed,
                           self.direction[1] * self.yspeed)
            screen.blit(self.sprite, (self.rect[0],self.rect[1]))
            if player.yspeed * -1 < 0:
                self.rect[1] += 4
                
        def destroy(self, screen):
            pygame.draw.rect(screen, white, self.rect)
            platformList.remove(self)

    def platformSpawn():
        num = random.randint(0,100)
        if num % 2 == 0:
            num = True
        else:
            num = False
        platformList.append(Platform(random.randint(10,510),0,screen,False,num))

    platformList = []
    player = Player(320,480)
    scoreFrame = 0
    screen.fill(white)
    pygame.display.update()
    frame = 0
    spawnable = True
    platformSpawn()
    platformSpawn()
    platformSpawn()
    dirtyRects = []
    while running:
        screen.fill(white)
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[97]:
            player.direction[0] = -1
        elif keys[100]:
            player.direction[0] = 1
        else:
            player.direction[0] = 0
        player.update(screen)
        for platform in platformList:
            platform.update(screen)
        frame += 1
        if frame == 20:
            if player.yspeed * -1 < 0:
                platformSpawn()
            frame = 0
        clock.tick(60)
        if player.yspeed * -1 < 0:
            scoreFrame += 1
            textToScreen("Score: " + str(int(scoreFrame/60)), 0,0,36,(0,0,0),False)
        else:
            textToScreen("Score: " + str(int(scoreFrame/60)), 0,0,36,(0,0,0),False)            
        pygame.display.update()
    quit()
main()
