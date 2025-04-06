#---------------Основа-----------------
from pygame import*
from button import*
from random import randint
import time as tm
clock = time.Clock()
window = display.set_mode((1000,700))
bg = image.load('bg1.png') 
mixer.init()
mixer.music.load("deadlocked.mp3")
kick1 = mixer.Sound("zvukipro.mp3")
kick2 = mixer.Sound("smerti.mp3")
collect = mixer.Sound("collect.mp3")
point = 0
b = []
x1,y1 = 150, 140
x2, y2 = 200, 200
x3,y3 = 250,100
ramke = [(x1,y1),(x2,y2),(x3,y3)]

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
    def for_x(self):
        if self.rect.x < -200:
            self.rect.x = 3500
def restart():
    global gamer, wall, square1, tringle1, money, square2,square3,square4,square5, tringle2, square6, square7, square8, tringle3, tringle4
    gamer.rect.x = 150
    gamer.rect.y = 395
    tringle1 = Enemy("tringle.png", 35,35,0,x4,450)
    tringle2 = Enemy("tringle.png", 35,35,0,x5,450)
    tringle3 = Enemy("tringle.png", 35,35,0,x6,450)
    tringle4 = Enemy("tringle.png", 35,35,0,x7,450)
    square1 = Enemy("square.png", 45,45,0,x8,445)
    square2 = Enemy("square.png", 45,45,0,x9,445)
    square3 = Enemy("square.png", 45,45,0,x10,445)
    square4 = Enemy("square.png", 45,45,0,x11,445)
    square5 = Enemy("square.png", 45,45,0,x12,445)
    square6 = Enemy("square.png", 45,45,0,x13,445)
    square7 = Enemy("square.png", 45,45,0,x14,445)
    square8 = Enemy("square.png", 45,45,0,x15,445)
    money = Enemy("money.png", 45,45,3,350,445)
    wall = Wall(28, 87, 189,0,485,100000,285) 
    gamer.update()
    gamer.risovka()
    money.update()
    btn_home2.draw_btn(window)
    btn_play.draw_btn(window)
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
    btn_home2.draw_btn(window)
def skins():
    window.blit(bg,(0,0))
    btn_home2.draw_btn(window)
    gamer4.draw_btn(window)
    gamer2.draw_btn(window)
    gamer3.draw_btn(window)
    gamer5.draw_btn(window)
    gamer6.draw_btn(window)
    gamer7.draw_btn(window)
    gamer8.draw_btn(window)
    gamer9.draw_btn(window)
x4 = 620
x5 = 1550
x6 = 2650
x7 = 3050
x8 = 450
x9 = 800
x10 = 1020
x11 = 1245
x12 = 1500
x13 = 1750
x14 = 2000
x15 = 2200
#------------------Создание спрайтов-------------- 
btn_play = Button(420,300,"play.png", 120,120) 
btn_skins = Button(240,300,"skins.png", 120,120)
btn_nast = Button(600,300, "nastroyki.png", 120,120)
btn_home2 = Button(850,10,"go_home.png", 110,110)
btn_home = Button(450,150,"go_home.png", 110,110)
btn_restart = Button(290,150,"restart.png", 110,110)
btn_soundon = Button(100,250,"music_on .png", 100,100)
btn_soundoff = Button(250,250,"music_off.png", 100,100)
nadpis1 = Button(170,30,"geometrydash.png", 650,100)
gamer = Player("sprite1.png", 45,45,2,150,395)

gamer4 = Button(150,100,"sprite1.png", 100,100)
gamer2 = Button(280,100,"sprite8.png", 100,100)
gamer3 = Button(410,100,"sprite9.jpg", 100,100)
gamer5 = Button(150,250,"sprite11.png", 100,100)
gamer6 = Button(240,230,"sprite12.png", 160,160)
gamer7 = Button(410,250,"sprite13.png", 100,100)
gamer8 = Button(540,250,"sprite14.png", 100,100)
gamer9 = Button(540,100,"sprite16.png", 100,100)

tringle1 = Enemy("tringle.png", 35,35,0,x4,450)
tringle2 = Enemy("tringle.png", 35,35,0,x5,450)
tringle3 = Enemy("tringle.png", 35,35,0,x6,450)
tringle4 = Enemy("tringle.png", 35,35,0,x7,450)
square1 = Enemy("square.png", 45,45,0,x8,445)
square2 = Enemy("square.png", 45,45,0,x9,445)
square3 = Enemy("square.png", 45,45,0,x10,445)
square4 = Enemy("square.png", 45,45,0,x11,445)
square5 = Enemy("square.png", 45,45,0,x12,445)
square6 = Enemy("square.png", 45,45,0,x13,445)
square7 = Enemy("square.png", 45,45,0,x14,445)
square8 = Enemy("square.png", 45,45,0,x15,445)
wall = Wall(28, 87, 189,0,485,100000,285)
x = 350

for i in range(5):
    money = Enemy("money.png", 45,45,3,x,445)
    x += randint(1000,2000)
    b.append(money)

game = True
graviti = False
jump = False
j = 15
a = "menu"
FPS = 80
# mixer.music.play()

#-------------------Цикл-------------------
while game:
    window.blit(bg,(0,0))
    if a == "menu":
        menu()
    if a == "skins":
        skins()
        draw.lines(window,(100,100,100),False,ramke,9)
    if a == "lose":
        lose()
    if a == "nast":
        nastr()
    if a == "game1":  
        #mixer.music.play()     
        gamer.update()
        gamer.risovka()
        tringle1.update()
        tringle1.for_x()
        tringle2.update()
        tringle2.for_x()
        tringle3.update()
        tringle3.for_x()
        tringle4.update()
        tringle4.for_x()
        square1.update()
        square1.for_x()
        square2.update()
        square2.for_x()
        square3.update()
        square3.for_x()
        square4.update()
        square4.for_x()
        square5.update()
        square5.for_x()
        square6.update()
        square6.for_x()
        square7.update()
        square7.for_x()
        square8.update()
        square8.for_x()
        btn_home2.draw_btn(window)
        if graviti:
            gamer.rect.y += 7
        if jump:
            if j > 0:
                gamer.rect.y -= 13
                j -= 1
            else:
                j = 15
                jump = False
        for i in b:
            i.update()
            if gamer.rect.colliderect(i):
                collect.play()
                point += 1
                i.rect.x += randint(2000,3000)
        # if square1.rect.x < -200():
        #         x4 += 4000
        wall.draw_wall()
    if (gamer.rect.colliderect(wall) or
        gamer.rect.collidepoint(square1.rect.midtop or square1.rect.topleft or square1.rect.topright) or
        gamer.rect.collidepoint(square2.rect.midtop or square2.rect.topleft or square2.rect.topright) or
        gamer.rect.collidepoint(square3.rect.midtop or square3.rect.topleft or square3.rect.topright) or
        gamer.rect.collidepoint(square4.rect.midtop or square4.rect.topleft or square4.rect.topright) or
        gamer.rect.collidepoint(square5.rect.midtop or square5.rect.topleft or square5.rect.topright) or
        gamer.rect.collidepoint(square6.rect.midtop or square6.rect.topleft or square6.rect.topright) or
        gamer.rect.collidepoint(square7.rect.midtop or square7.rect.topleft or square7.rect.topright) or
        gamer.rect.collidepoint(square8.rect.midtop or square8.rect.topleft or square8.rect.topright)):
        graviti = False
    else:
        graviti = True
    if (gamer.rect.collidepoint(square1.rect.midleft) or
        gamer.rect.collidepoint(square2.rect.midleft) or
        gamer.rect.collidepoint(square3.rect.midleft) or
        gamer.rect.collidepoint(square4.rect.midleft) or
        gamer.rect.collidepoint(square5.rect.midleft) or
        gamer.rect.collidepoint(square6.rect.midleft) or
        gamer.rect.collidepoint(square7.rect.midleft) or
        gamer.rect.collidepoint(square8.rect.midleft) or
        gamer.rect.colliderect(tringle1) or gamer.rect.colliderect(tringle2) or
        gamer.rect.colliderect(tringle3) or gamer.rect.colliderect(tringle4)):
        a = "lose"
        kick2.play()
        restart()    
    for ev in event.get():
        if ev.type == QUIT:
            game = False
        if btn_play.check_kasanie(mouse.get_pos(), ev):
            a = "game1"
            kick1.play()
        if btn_skins.check_kasanie(mouse.get_pos(), ev):
            kick1.play()
            a = "skins"
        if btn_nast.check_kasanie(mouse.get_pos(), ev):
            a = "nast"
            kick1.play()
            restart()
        if btn_restart.check_kasanie(mouse.get_pos(),ev):
            a = "game1"
            kick1.play()
        if btn_home2.check_kasanie(mouse.get_pos(),ev):
            a = "menu"
            kick1.play()
            restart()
            #mixer.music.play()
        if btn_home.check_kasanie(mouse.get_pos(),ev):
            a = "menu"
            kick1.play()
            #mixer.music.play()
        if btn_soundon.check_kasanie(mouse.get_pos(),ev):
            mixer.music.play()
        if btn_soundoff.check_kasanie(mouse.get_pos(),ev):
            mixer.music.stop()
        if point >= 0 and gamer4.check_kasanie(mouse.get_pos(), ev):
            gamer.image = transform.scale(image.load("sprite1.png"),(45,45))
            x1,y1 = 150, 140
            x2, y2 = 200, 200
            x3,y3 = 250,100
            ramke = [(x1,y1),(x2,y2),(x3,y3)]
        if point >= 2 and gamer2.check_kasanie(mouse.get_pos(), ev):
            gamer.image = transform.scale(image.load("sprite8.png"),(45,45))
            point -= 2
            x1,y1 = 280, 140
            x2,y2 = 330,200
            x3,y3 = 380,100
            ramke = [(x1,y1),(x2,y2),(x3,y3)]
        if point >= 5 and gamer3.check_kasanie(mouse.get_pos(), ev):
            gamer.image = transform.scale(image.load("sprite9.jpg"),(45,45))
            point -= 5
            x1,y1 = 410,140
            x2,y2 = 460,200
            x3,y3 = 510,100
            ramke = [(x1,y1),(x2,y2),(x3,y3)]
        if point >= 8 and gamer9.check_kasanie(mouse.get_pos(), ev):
            gamer.image = transform.scale(image.load("sprite16.png"),(45,45))
            point -= 8
            x1,y1 = 590,140
            x2,y2 = 640,200
            x3,y3 = 540,100
            ramke = [(x1,y1),(x2,y2),(x3,y3)]
        if point >= 10 and gamer5.check_kasanie(mouse.get_pos(), ev):
            gamer.image = transform.scale(image.load("sprite11.png"),(45,45))
            point -= 10
            x1,y1 = 150,290
            x2,y2 = 200,350
            x3,y3 = 250,250
            ramke = [(x1,y1),(x2,y2),(x3,y3)]
        if point >= 15 and gamer6.check_kasanie(mouse.get_pos(), ev):
            gamer.image = transform.scale(image.load("sprite12.png"),(45,45))
            point -= 15
            x1,y1 = 280,290
            x2,y2 = 330,350
            x3,y3 = 380,250
            ramke = [(x1,y1),(x2,y2),(x3,y3)]
        if point >= 20 and gamer7.check_kasanie(mouse.get_pos(), ev):
            gamer.image = transform.scale(image.load("sprite13.png"),(45,45))
            point -= 20
            x1,y1 = 410,290
            x2,y2 = 460,350
            x3,y3 = 510,250
            ramke = [(x1,y1),(x2,y2),(x3,y3)]
        if point >= 25 and gamer8.check_kasanie(mouse.get_pos(), ev):
            gamer.image = transform.scale(image.load("sprite14.png"),(45,45))
            point -= 25
            x1,y1 = 590,290
            x2,y2 = 640,350
            x3,y3 = 540,250
            ramke = [(x1,y1),(x2,y2),(x3,y3)]
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE and graviti == False:
                jump = True
        if ev.type == MOUSEBUTTONDOWN and graviti == False:
            jump = True
    
    clock.tick(FPS)
    display.update()   