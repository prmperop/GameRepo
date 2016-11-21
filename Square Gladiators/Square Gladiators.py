import pygame, random, time
import Intro
pygame.init()

screensize = (640,480)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Square Gladiators')
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
liveNumber = Intro.LiveGet()

def Main(liveNumber):
    
    def textToScreen(message,x,y,size,color,center = True):
        font = pygame.font.Font(None, size)
        text = font.render(str(message), 1, color)
        #pygame.draw.rect(screen,white, (x,y,text.get_rect()[3],text.get_rect[4]))
        if center == True:
            screen.blit(text,(text.get_rect(center = (x,y))))
        else:
            screen.blit(text,(x,y))
        #pygame.display.update(pygame.Rect(x,y,text.get_rect()[3], text.get_rect()[4])

    class Player(object):
        def __init__(self, x,y, num):
            self.rect = pygame.Rect(x,y,25,25)
            self.sprite = pygame.image.load('images/Player' + str(num) + '.png').convert()
            self.direction = [0,0]
            self.speed = 5
            self.bulletCount = 0
            self.clear = pygame.image.load('images/Clear.png').convert()
            self.owner = num
            self.health = liveNumber
            self.shot = False
            self.maxBullet = 3
        def update(self, screen):
            if self.rect[1] >= screensize[1] - 25 and self.direction[1] == 1:
                self.direction[1] = 0
            if self.rect[1] <= 25  and self.direction[1] == -1:
                self.direction[1] = 0
            if self.owner == 2:
                if self.rect[0] >= screensize[0] - 27 and self.direction[0] == 1:
                    self.direction[0] = 0
                if self.rect[0] <= screensize[0] / 2 + 2 and self.direction[0] == -1:
                    self.direction[0] = 0
            if self.owner == 1:
                if self.rect[0] >= screensize[0] / 2 - 27 and self.direction[0] == 1:
                    self.direction[0] = 0
                if self.rect[0] <= 0 and self.direction[0] == -1:
                    self.direction[0] = 0
            screen.blit(self.clear,(self.rect[0], self.rect[1]))
            pygame.display.update(self.rect)
            self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
            screen.blit(self.sprite,(self.rect[0], self.rect[1]))
            pygame.display.update(self.rect)
            if self.health == 0:
                self.death()
        def shoot(self):
            if self.bulletCount >= self.maxBullet:
                None
            else:
                if self.owner == 1:
                    x = 1
                    change = 10
                if self.owner == 2:
                    x = -1
                    change = -10
                
                z = Bullet(self.rect.center[0] + change, self.rect.center[1], [x, 0], self.owner)
                bulletList.append(z)
                self.bulletCount += 1
        def death(self):
            screen.fill(white)
            if self.owner == 1:
                jk = 'Blue'
                jkl = (0,0,255)
            if self.owner == 2:
                jk = 'Green'
                jkl = (100,255,100) 
            textToScreen(str(jk) + ' Wins!', screensize[0]/2, screensize[1]/2, 81,jkl)
            pygame.display.update()
            time.sleep(1)
            Main(liveNumber)

    class Bullet(object):
        def __init__(self,x,y,direction, owner):
            self.rect = pygame.Rect(x,y,5,5)
            self.sprite = pygame.image.load('images/Bullet.png').convert()
            self.clear = pygame.image.load('images/ClearBullet.png').convert()
            self.direction = direction
            self.speed = 15
            self.owner = owner
            self.back = False
        def update(self, screen):
            screen.blit(self.clear,(self.rect[0], self.rect[1]))
            pygame.display.update(self.rect)
            self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
            screen.blit(self.sprite,(self.rect[0], self.rect[1]))
            pygame.display.update(self.rect)
            if self.rect[0] >= screensize[0] - 5:
                if self.back == False:
                    self.direction[0] = -1
                    self.back = True
                else:
                    self.kill()
            if self.rect[0] <= 0:
                if self.back == False:
                    self.direction[0] = 1
                    self.back= True
                else:
                    self.kill()
            if self.rect.colliderect(Player1):
                self.kill()
                Player1.health -= 1
                pygame.draw.rect(screen, white, (screensize[0]/2 - 23,0,23,25))
                textToScreen(str(Player1.health),screensize[0]/2-23,3,36,black,False)
            if self.rect.colliderect(Player2):
                self.kill()
                Player2.health -= 1
                pygame.draw.rect(screen, white, (screensize[0]/2,0,23,25))
                textToScreen(str(Player2.health),screensize[0]/2 + 10,3,36,black,False)
        def kill(self):
            screen.blit(self.clear, (self.rect[0], self.rect[1]))
            pygame.display.update(self.rect)
            if self.owner == 1:
                Player1.bulletCount -=1
            if self.owner == 2:
                Player2.bulletCount -=1
            bulletList.remove(self)
            self = None
    class Powerup(object):
        def __init__(self,x,y,kind):
            self.rect = pygame.Rect(x,y,10,10)
            self.color = (0,0,0)
            self.kind = str(kind)
            self.sprite = pygame.image.load("images\Powerup" + str(kind) + ".png").convert()
            self.clear = pygame.image.load("images\powerupClear.png").convert()
            self.count = 300
                                           
        def update(self,screen):
            self.count -= 1
            screen.blit(self.sprite, (self.rect[0], self.rect[1]))
            dirtyRects.append(self.rect)
            if self.rect.colliderect(Player1.rect):
                if self.kind == 'Heal':
                    Player1.health += 1
                    self.kill(screen)
                    pygame.draw.rect(screen, white, (screensize[0]/2 - 23,0,23,25))
                    textToScreen(str(Player1.health),screensize[0]/2-23,3,36,black,False)
            if self.rect.colliderect(Player2.rect):
                if self.kind == 'Heal':
                    Player2.health += 1
                    self.kill(screen)
                    pygame.draw.rect(screen, white, (screensize[0]/2,0,23,25))
                    textToScreen(str(Player2.health),screensize[0]/2 + 10,3,36,black,False)
            if self.count == 0:
                self.kill(screen)
        def kill(self,screen):
            screen.blit(self.clear, (self.rect[0], self.rect[1]))
            dirtyRects.append(self.rect)
            powerupList.remove(self)
            self = None
    bulletList = []
    dirtyRects = []
    powerupList = []
    running = True
    Player1 = Player(25, 25, 1)
    Player2 = Player(600, 400, 2)
    screen.fill(white)
    textToScreen(str(Player1.health),screensize[0]/2-23,3,36,black,False)
    textToScreen(str(Player2.health),screensize[0]/2 + 10,3,36,black,False)
    pygame.display.update()
    
    
    while running:
        num = random.randint(1,1000)
        num2 = random.randint(1,1000)
        if num == num2:
            powerupList.append(Powerup(random.randint(0,640), random.randint(0,480), 'Heal'))
            print('dsafk')
        dirtyRects = []
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[97] or keys[100]:
            if keys[97]:
                Player1.direction[0] = -1
            else:
                Player1.direction[0] = 1
        else:
            Player1.direction[0] = 0
        if keys[119] or keys[115]:
            if keys[119]:
                Player1.direction[1] = -1
            else:
                Player1.direction[1] = 1
        else:
            Player1.direction[1] = 0
        if keys[276] or keys[275]:
            if keys[276]:
                Player2.direction[0] = -1
            else:
                Player2.direction[0] = 1
        else:
            Player2.direction[0] = 0
        if keys[273] or keys[274]:
            if keys[273]:
                Player2.direction[1] = -1
            else:
                Player2.direction[1] = 1
        else:
            Player2.direction[1] = 0
        if keys[32] and Player1.shot == False:
            Player1.shoot()
            Player1.shot = True
        if keys[32] == False:
            Player1.shot = False
        if keys[303] and Player2.shot == False:
            Player2.shot = True
            Player2.shoot()
        if not keys[303]:
            Player2.shot = False
        if keys[27]:
            pygame.quit()
        Player1.update(screen)
        Player2.update(screen)
        pygame.draw.rect(screen, black, (screensize[0]/2, 0, 1, screensize[1]))
        dirtyRects.append((screensize[0]/2, 0, screensize[0]/2, screensize[1]))
        dirtyRects.append((0,0,screensize[0], 20))
        for item in bulletList:
            item.update(screen)
        for item in powerupList:
            item.update(screen)
        pygame.display.update(dirtyRects)
        clock.tick(60)

Main(liveNumber)
quit()
