import pygame, time, random
pygame.init()

screensize = (640,480)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("images/Acid Rain")
background = pygame.image.load('images/2.png')
background.convert()
Clock = pygame.time.Clock()
white = (240,240,240)
black = (10,10,10)

def main():
    running = True

    class Player(object):
        def __init__(self,x,y):
            self.colour = (32,65,210)
            self.rect = pygame.Rect(x,y,25,25)
            self.direction = [0,0]
            self.speed = 3
            self.lose = False
            self.score = 0
            self.ship = pygame.image.load("images/Ship.png")
            self.ship.convert()
            self.hiScore = 0
        def update(self, screen):
            self.score += 0.03
            if self.rect[0] > screensize[0] - 30 and self.direction[0] == 1:
                self.direction[0] = 0
            if self.rect[0] < 5 and self.direction[0] == -1:
                self.direction[0] = 0
            if self.rect[1] > screensize[1] - 30 and self.direction[1] == 1:
                self.direction[1] = 0
            if self.rect[1] < 5 and self.direction[1] == -1:
                self.direction[1] = 0
            pygame.display.update(self.rect)
            self.rect.move_ip(self.direction[0] * self.speed,
                           self.direction[1] * self.speed)
            screen.blit(self.ship, (self.rect[0], self.rect[1]))
            pygame.display.update(self.rect)
            for enemy in enemyList:
                if self.rect.colliderect(enemy.rect):
                    self.lose = True
            if self.score > self.hiScore:
                self.hiScore = self.score
                    
    class Enemy(object):
        def __init__(self,x,y):
            self.colour = (100,255,100)
            self.rect = pygame.Rect(x,y,5,5)
            self.direction = (1,1)
            self.speed = 3
            self.sprite = pygame.image.load('images/rain.png').convert()
        def update(self,screen):
            pygame.display.update(self.rect)
            self.rect = self.rect.move(self.direction[0] * self.speed,
                                       self.direction[1] * self.speed)
            screen.blit(self.sprite, (self.rect[0], self.rect[1]))
            pygame.display.update(self.rect)

    def textToScreen(message,x,y, size):
        font = pygame.font.Font(None, size)
        text = font.render(str(message), 1, (10, 10, 10))
        text.get_rect(center = (x,y))
        pygame.draw.rect(screen, white, text.get_rect())
        screen.blit(text, (text.get_rect(center = (x,y))))
        pygame.display.update(text.get_rect())
    def textToScreenNoCenter(message,x,y,size):
        font = pygame.font.Font(None, size)
        text = font.render(str(message), 1, (10, 10, 10))
        pygame.draw.rect(screen, white, text.get_rect())
        screen.blit(text, (x,y))
        pygame.display.update(text.get_rect())
    def textToScreenWhite(message,x,y,size):
        font = pygame.font.Font(None, size)
        text = font.render(str(message), 1, (225,225,225))
        screen.blit(text, (x,y))
        pygame.display.update(text.get_rect())

    def enemySpawn():
        x = random.randint(-450,screensize[0])
        y = 0
        enemyList.append(Enemy(x,y))
        for enemy in enemyList:
            if enemy.rect[0] > screensize[0] + 5 or \
               enemy.rect[1] > screensize[1] + 5:
                enemyList.remove(enemy)
    def pause():
        pause = True
        box = pygame.Rect(0,0,100,25)
        box2 = pygame.Rect(0,0,100,25)
        box.center = (screensize[0]/2, screensize[1]/2)
        box2.center = (screensize[0]/2, screensize[1]/2 + 35)
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if box.collidepoint((pygame.mouse.get_pos())):
                        pause = False
                    if box2.collidepoint((pygame.mouse.get_pos())):
                        quit()
            screen.fill(white)
            pygame.draw.rect(screen,(100,100,100),box)
            pygame.draw.rect(screen,(0,0,0),box,1)
            pygame.draw.rect(screen,(100,100,100),box2)
            pygame.draw.rect(screen,(0,0,0),box2,1)
            textToScreen('Paused', screensize[0]/2, 50, 72)
            textToScreen('Resume', screensize[0]/2, screensize[1]/2, 36)
            textToScreen('Quit', screensize[0]/2, screensize[1]/2 + 35, 36)
            pygame.display.update()
        screen.fill(white)
        screen.blit(background,(0,0))
        pygame.display.update()
            
            
    frame = 1
    player = Player(600,400)
    enemyList = []
    screen.blit(background,(0,0))
    pygame.display.update()

    
    while not player.lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.direction[0] = -1
                elif event.key == pygame.K_LEFT:
                    player.direction[0] = -1
                if event.key == pygame.K_d:
                    player.direction[0] = 1
                elif event.key == pygame.K_RIGHT:
                    player.direction[0] = 1
                if event.key == pygame.K_s:
                    player.direction[1] = 1
                elif event.key == pygame.K_DOWN:
                    player.direction[1] = 1
                if event.key == pygame.K_w:
                    player.direction[1] = -1
                elif event.key == pygame.K_UP:
                    player.direction[1] = -1
                if event.key == pygame.K_p:
                    pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player.direction[0] = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.direction[0] = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.direction[1] = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.direction[1] = 0
        screen.blit(background,(0,0))
        player.update(screen)
        for enemy in enemyList:
            enemy.update(screen)
            if enemy.rect[1] > 700:
                enemyList.remove(enemy)
        frame += 1
        if frame == 2:
            enemySpawn()
            frame = 0
        Clock.tick(60)
        textToScreenWhite('Score: ' + str(int(player.score)), 0,0, 24)
        ##textToScreenWhite('High Score: ' + str(int(player.hiScore)), 0,15, 24)
    screen.fill(white)
    textToScreen('You Got Hit! Your Score Was: ' + str(int(player.score)),
                 screensize[0]/2, screensize[1]/2, 56)
    pygame.display.update()
    time.sleep(1)
    main()
main()
