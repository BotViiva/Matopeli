import pygame
from sys import exit
from random import randint
from pygame.math import Vector2

solu_koko = 40
solu_numero = 20
screen = pygame.display.set_mode((solu_koko * solu_numero,solu_koko * solu_numero))
clock = pygame.time.Clock()
running = True

class Main:
    def __init__(self) -> None:
        self.mato = Mato()
        self.omena = Omena()
        self.pisteet = 0

    def update(self):
        self.mato.mato_liikutus()
        self.omenan_syönti()
        self.tarkista_törmäys()

        
    def piirrä_elementit(self):
        self.omena.piirrä_omena()
        self.mato.piirrä_mato()
        self.piirrä_pisteet()

    def omenan_syönti(self):
        if self.omena.pos == self.mato.keho[0]:
            self.mato.lisää_pituus()
            self.omena.uusi_sijainti()
            self.mato.lisää_nopeus()
            self.pisteet += 1
    
    def tarkista_törmäys(self):
        if not 0 <= self.mato.keho[0].x < solu_numero or not 0 <= self.mato.keho[0].y < solu_numero:
            self.peli_ohi()

        for block in self.mato.keho[1:]:
            if block == self.mato.keho[0]:
                self.peli_ohi()

    def peli_ohi(self):
        pygame.quit
        exit()

    def piirrä_pisteet(self):
        
        pisteet_text = fontti.render(str(self.pisteet), (255,255,255), (0,0,0))
        screen.blit(pisteet_text, (760,760))

        

class Omena:
    def __init__(self) -> None:
        self.uusi_sijainti()
       
    def piirrä_omena(self):
        omena_rect = pygame.Rect(int(self.pos.x * solu_koko),int(self.pos.y * solu_koko), solu_koko,solu_koko)
        pygame.draw.rect(screen, (255, 0, 0), omena_rect)

    def uusi_sijainti(self):
        self.x = (randint(0,760))
        self.y = (randint(0,760))
        self.pos = Vector2(self.x//solu_koko, self.y//solu_koko)

    

class Mato():
    def __init__(self):
        self.keho = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.suunta = [Vector2(1,0)]
        self.nopeus = 150
        
        

    def piirrä_mato(self):
        for block in self.keho:
            x_pos = int(block.x * solu_koko)
            y_pos = int(block.y * solu_koko)
            mato_rect = pygame.Rect(x_pos,y_pos,40,40)
    
            pygame.draw.rect(screen, (0,0,0), mato_rect)
    
    def mato_liikutus(self):
        keho_kopio = self.keho[:-1]
        keho_kopio.insert(0,keho_kopio[0] + self.suunta[0])
        self.keho = keho_kopio[:]

    def lisää_pituus(self):
        keho_kopio = self.keho[:]
        keho_kopio.append(keho_kopio[-1] + self.suunta[0])
        self.keho = keho_kopio[:]
 
    def lisää_nopeus(self):
        if self.nopeus >100:
            self.nopeus -= 5
        elif self.nopeus >80:
            self.nopeus -= 2
        elif self.nopeus >70:
            self.nopeus -= 1
        else:
            pass

    def tarkista_suunta(self):
        if len(self.suunta) > 3 and self.suunta[0] == self.suunta[1] and self.suunta[2] == self.suunta[3]:
            self.suunta.pop(1)
            self.suunta.pop(2)
            print("popped, ", self.suunta)
        if len(self.suunta) > 3 and self.suunta[0] == self.suunta[2] and self.suunta[1] == self.suunta[3]:
            self.suunta.pop(1)
            self.suunta.pop(1)
            print("popped, ", self.suunta)
    
    
        
pygame.init()
fontti = pygame.font.Font(None, 60)
main_peli = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, main_peli.mato.nopeus)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == SCREEN_UPDATE:
            pygame.time.set_timer(SCREEN_UPDATE, main_peli.mato.nopeus)

            if len(main_peli.mato.suunta) > 1 and main_peli.mato.suunta[0] == main_peli.mato.suunta[1]:
                main_peli.mato.suunta.pop(1)
            if len(main_peli.mato.suunta) > 2 and main_peli.mato.suunta[0] == main_peli.mato.suunta[2]:
                main_peli.mato.suunta.pop(2)
            if len(main_peli.mato.suunta) > 1:
                main_peli.mato.suunta.pop(0)
            main_peli.update()

            print(main_peli.pisteet)

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and main_peli.mato.suunta[0] != Vector2(0,1) and main_peli.mato.suunta[-1] != Vector2(0,-1) and len(main_peli.mato.suunta) <4:
            main_peli.mato.suunta.append(Vector2(0,-1))
        if keys[pygame.K_DOWN] and main_peli.mato.suunta[0] != Vector2(0,-1) and main_peli.mato.suunta[-1] != Vector2(0,1)and len(main_peli.mato.suunta) <4:
            main_peli.mato.suunta.append(Vector2(0,1))
        if keys[pygame.K_RIGHT] and main_peli.mato.suunta[0] != Vector2(-1,0) and main_peli.mato.suunta[-1] != Vector2(1,0)and len(main_peli.mato.suunta) <4:
            main_peli.mato.suunta.append(Vector2(1,0))
        if keys[pygame.K_LEFT] and main_peli.mato.suunta[0] != Vector2(1,0) and main_peli.mato.suunta[-1] != Vector2(-1,0)and len(main_peli.mato.suunta) <4:
            main_peli.mato.suunta.append(Vector2(-1,0))

    main_peli.mato.tarkista_suunta()
    screen.fill ((0, 200, 0))
    main_peli.piirrä_elementit()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()