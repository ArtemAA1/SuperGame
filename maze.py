from pygame import *

win_widht = 700
win_height = 500 
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load("background.jpg"),(win_widht,win_height))

run = True
finish = False
clock = time.Clock()
FPS = 60 

font.init()
font = font.Font(None,70)
win = font.render("YOU WIN!",True,(255,215,0))
lose = font.render('BRUH YOU LOSE!',True,(180,0,0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self): 
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < win_widht -  70:
            self.rect.x += self.speed
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
        


class Enemy(GameSprite):
    def update(self):
    pass

class Wall(sprite.Sprite):
    def __init__(self,wall_x,wall_y,width,height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def resert(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



player = Player('hero.png',100,400,4)
cyborg = Enemy('cyborg.png',500,300,2)
treasure = GameSprite('treasure.png',550,350,0)
wall1 = Wall(175,75,10,300)
wall2 = Wall(175,75,200,10)
 
while run:
    for e in event.get():
        if e.type == QUIT:
            run  = False
    
    if not finish:
        window.blit(background,(0,0))
        player.update()
        cyborg.update()
        wall1.resert()
        wall2.resert()

        player.reset()  
        cyborg.reset()
        treasure.reset()

        if sprite.collide_rect(player,treasure):
            finish = True
            money.play()
            window.blit(win,(200,200))

        if sprite.collide_rect(player,cyborg) or sprite.collide_rect(player,wall1) or sprite.collide_rect(player,wall2):
            finish = True
            kick.play()
            window.blit(lose,(100,200))
            
    display.update()
    clock.tick(FPS)