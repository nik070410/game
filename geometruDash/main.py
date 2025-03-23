#---------------Основа-----------------
from pygame import*
from button import*
import time as tm
clock = time.Clock()
window = display.set_mode((1000,700))
bg = image.load('bg1.png')
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
            self.rect.y -= 90
        if not self.rect.colliderect(wall):
             self.rect.y += 2

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
        self.rect.x -= 4
        window.blit(self.image, (self.rect.x, self.rect.y))
def restart():
    global sprite, wall, square1, tringle1  
    sprite.update()
    sprite.risovka()
    tringle1.update()
    square1.update()
    wall.draw_wall()
#------------------Создание спрайтов-------------- 
btn_play = Button(350,350,"play.png", 100,100) 
btn_skins = Button(200,350,"skins.png", 100,100)
btn_nast = Button(480,350, "nastroyki.png", 100,100)
sprite = Player("sprite1.png", 40,40,2,150,640)
tringle1 = Enemy("tringle.png", 40,40,0,550,650)
square1 = Enemy("square.png", 40,40,0,450,650)
wall = Wall(0,0,0,0,685,100000,20)

game = True
a = "menu"
FPS = 60

def menu():
    window.blit(bg,(0,0))
    btn_play.draw_btn(window)
    btn_skins.draw_btn(window)
    btn_nast.draw_btn(window)     
#-------------------Цикл-------------------
while game:
    window.blit(bg,(0,0))
    if a == "menu":
        menu()
    if a == "game1":       
        sprite.update()
        sprite.risovka()
        tringle1.update()
        square1.update()
        wall.draw_wall()
        if sprite.rect.colliderect(tringle1) or sprite.rect.colliderect(square1):
            a = "menu"
    for ev in event.get():
        if ev.type == QUIT:
            game = False
        if btn_play.check_kasanie(mouse.get_pos(), ev):
            a = "game1"
        if btn_skins.check_kasanie(mouse.get_pos(), ev):
            pass
        if btn_nast.check_kasanie(mouse.get_pos(), ev):
            pass

    clock.tick(FPS)
    display.update()   