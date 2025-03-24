#---------------Основа-----------------
from pygame import*
from button import*
import time as tm
clock = time.Clock()
window = display.set_mode((1000,700))
bg = image.load('bg1.png')
mixer.init()
mixer.music.load("geometrydash.mp3")
kick1 = mixer.Sound("zvukipro.mp3")
#------------------Класи----------------------
class GameSprite(sprite.Sprite):
    def __init__(self, images, w,h, speed ,x ,y):
        self.image = transform.scale(image.load(images),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = w-1.2
        self.rect.height = h-1.2
    def risovka(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_SPACE] and self.rect.colliderect(wall):
            self.rect.y -= 100
        if not self.rect.colliderect(wall):
             self.rect.y += 3

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3, wall_x , wall_y, wall_width , wall_height):
        self.color_1 = color_1
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x , self.rect.y))
class Enemy(GameSprite):
    def update(self):
        self.rect.x -= 5
        window.blit(self.image, (self.rect.x, self.rect.y))
def restart():
    global sprite, wall, square1, tringle1
    sprite = Player("sprite1.png", 40,40,2,150,620)
    tringle1 = Enemy("tringle.png", 40,40,0,550,650)
    square1 = Enemy("square.png", 40,40,0,450,650)
    wall = Wall(0,0,0,0,685,100000,20)  
    sprite.update()
    sprite.risovka()
    tringle1.update()
    square1.update()
    wall.draw_wall()
def lose():
    window.blit(bg,(0,0))
    btn_home.draw_btn(window)
    btn_restart.draw_btn(window)
def menu():
    window.blit(bg,(0,0))
    btn_play.draw_btn(window)
    btn_skins.draw_btn(window)
    btn_nast.draw_btn(window) 
    nadpis1.draw_btn(window)
    
def nastr():
    window.blit(bg,(0,0))
    btn_soundon.draw_btn(window)
    btn_soundoff.draw_btn(window)
#------------------Создание спрайтов-------------- 
btn_play = Button(420,300,"play.png", 120,120) 
btn_skins = Button(240,300,"skins.png", 120,120)
btn_nast = Button(600,300, "nastroyki.png", 120,120)
btn_home = Button(480,250,"go_home.png", 110,110)
btn_restart = Button(290,250,"restart.png", 110,110)
btn_soundon = Button(100,100,"music_on.png", 100,100)
btn_soundoff = Button(200,100,"music_off.png", 100,100)
nadpis1 = Button(170,30,"geometrydash.png", 650,100)
sprite = Player("sprite1.png", 40,40,2,150,640)
tringle1 = Enemy("tringle.png", 40,40,0,550,650)
square1 = Enemy("square.png", 40,40,0,450,650)
wall = Wall(0,0,0,0,685,100000,20)

game = True
a = "menu"
FPS = 60
#mixer.music.play()
    
#-------------------Цикл-------------------
while game:
    window.blit(bg,(0,0))
    if a == "menu":
        menu()
    if a == "lose":
        lose()
    if a == "nast":
        nastr()
    if a == "game1":       
        sprite.update()
        sprite.risovka()
        tringle1.update()
        square1.update()
        wall.draw_wall()
        if sprite.rect.colliderect(tringle1) or sprite.rect.colliderect(square1):
            a = "lose"
            restart()
    for ev in event.get():
        if ev.type == QUIT:
            game = False
        if btn_play.check_kasanie(mouse.get_pos(), ev):
            a = "game1"
            kick1.play()
        if btn_skins.check_kasanie(mouse.get_pos(), ev):
            kick1.play()
        if btn_nast.check_kasanie(mouse.get_pos(), ev):
            a == "nast"
            kick1.play()
        if btn_restart.check_kasanie(mouse.get_pos(),ev):
            a = "game1"
            kick1.play()
        if btn_home.check_kasanie(mouse.get_pos(),ev):
            a = "menu"
            kick1.play()
            #mixer.music.play()

    clock.tick(FPS)
    display.update()   