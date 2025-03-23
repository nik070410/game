from pygame import*
class Button:
    def __init__(self, x, y, im, width, height):
           self.width = width
           self.height = height
           self.image = image.load(im)
           self.image = transform.scale(self.image, (self.width, self.height))
           self.rect = self.image.get_rect()
           self.rect.x = x
           self.rect.y = y
           self.is_kasanie = False
           
    def draw_btn(self, scr):
       scr.blit(self.image, (self.rect.x, self.rect.y))
       #font1 = font.Font("Christmas ScriptC.ttf", 40)
       #text_surface = font1.render(self.text, True, (0,0,0))
       #text_rect = text_surface.get_rect(center = self.rect.center)
       #scr.blit(text_surface, text_rect)
       
    def check_kasanie(self, mouse_pos, event):
        self.is_kasanie = self.rect.collidepoint(mouse_pos)
        if self.is_kasanie and event.type == MOUSEBUTTONDOWN:
            return True
