
 
#Hecho por Juan Barraco, modificando el pong escrito por Daniel Fuentes B (https://www.pythonmania.net/es/2010/04/07/tutorial-pygame-3-un-videojuego/).




# ---------------------------
# Importacion de los módulos
# ---------------------------
 
import pygame
from pygame.locals import *
import os
import sys
import random      
 
# -----------
# Constantes
# -----------
 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMG_DIR = "imagenes"
SONIDO_DIR = "sonidos"
 
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
 
 
def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print ("Error, no se puede cargar la imagen: ", ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

def load_sound(nombre, dir_sonido):
    ruta = os.path.join(dir_sonido, nombre)
    # Intentar cargar el sonido
    try:
        sonido = pygame.mixer.Sound(ruta)
    except (pygame.error) as message:
        print("No se pudo cargar el sonido:", ruta)
        sonido = None
    return sonido
 
 
# -----------------------------------------------
# Creamos los sprites (clases) de los objetos del juego:


 
 
class Pelota(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bola.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [3, 3]
 
    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.speed[0] = -self.speed[0]

class PelotaRapida(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bola.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [6, 3]
 
    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.speed[0] = -self.speed[0]

class PelotaRapida1(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bola.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [3, 6]
 
    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.speed[0] = -self.speed[0]

class PelotaCrece(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bolacrece.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [int(random.randrange(1,6)), int(random.randrange(1,6))]  #velocidad random
 
    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -(random.randint(7, 15)/10)*self.speed[0]  #cambio de velocidad v = 0,7-1,5 v
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -(random.randint(7, 15)/10)*self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        if self.speed[0]>10:
            self.speed[0]=4
        if self.speed[1]>10:
            self.speed[1]=ACTIVEEVENT
        
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.speed[0] = -(random.randint(7, 15)/10)*self.speed[0]
            self.speed[1] = -(random.randint(7, 15)/10)*self.speed[1]
        if self.speed[0]>10:
            self.speed[0]=4
        if self.speed[1]>10:
            self.speed[1]=4

class PelotaBuena(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bolabuena.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [int(random.randrange(1,6)), int(random.randrange(1,6))]
 
    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -(random.randint(7, 15)/10)*self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -(random.randint(7, 15)/10)*self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        if self.speed[0]>10:
            self.speed[0]=4
        if self.speed[1]>10:
            self.speed[1]=4
        
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.speed[0] = -(random.randint(7, 15)/10)*self.speed[0]
            self.speed[1] = -(random.randint(7, 15)/10)*self.speed[1]
        if self.speed[0]>10:
            self.speed[0]=4
        if self.speed[1]>10:
            self.speed[1]=4

class PelotaLentaM(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bola1.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [2, 2]
 #       self.sonido_pop = sonido_pop
 
    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -(random.randint(7, 15)/10)*self.speed[0]
 #           self.sonido_pop.play()
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -(random.randint(7, 15)/10)*self.speed[1]
 #           self.sonido_pop.play()
        self.rect.move_ip((self.speed[0], self.speed[1]))
        if self.speed[0]>10:
            self.speed[0]=4
        if self.speed[1]>10:
            self.speed[1]=4
        
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.speed[0] = -(random.randint(7, 15)/10)*self.speed[0]
            self.speed[1] = -(random.randint(7, 15)/10)*self.speed[1]
        if self.speed[0]>10:
            self.speed[0]=4
        if self.speed[1]>10:
            self.speed[1]=4
 
 
 
class Guy(pygame.sprite.Sprite):
    "Jugador"
 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("guy.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 40
        self.rect.centery = SCREEN_HEIGHT / 2
 
    def humano(self):
        # Controlar que la paleta no salga de la pantalla
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        elif self.rect.top <= 0:
            self.rect.top = 0

 
# ------------------------------
# Funcion principal del juego
# ------------------------------
 

def main():
    game = True
    pygame.init()
    pygame.mixer.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Some guy, some balls")

    #creo fuentes y mensajes    

    fuente1= pygame.font.SysFont("Arial",20,True,False)
    info1 = fuente1.render("Some Guy...",0,(255,255,255))
    fuente2= pygame.font.SysFont("Lucida Console",25,True,False)
    fuente3= pygame.font.SysFont("Lucida Console",30,True,False)

    
    info2 = fuente1.render("...Some Balls",0,(255,255,255))

    
    pygame.display.flip()

 
    # cargamos los objetos
    sonido_goddam = load_sound("goddamn1.wav", SONIDO_DIR)
    sonido_musica = load_sound("musicBG.wav", SONIDO_DIR)
    sonido_mygod = load_sound("mygod.wav", SONIDO_DIR)
    sonido_big = load_sound("big.wav", SONIDO_DIR)
    sonido_pop = load_sound("pop.wav", SONIDO_DIR)
    sonido_woho = load_sound("woohoo.wav", SONIDO_DIR)
    sonido_comeon = load_sound("comeon.wav", SONIDO_DIR)
    sonido_yes = load_sound("yes.wav", SONIDO_DIR)
    sonido_no = load_sound("no.wav", SONIDO_DIR)

    sonidos_buenos = [sonido_woho, sonido_comeon, sonido_yes]  #listas con sonidos para usar random
    sonidos_malos = [sonido_goddam, sonido_mygod, sonido_goddam, sonido_mygod, sonido_no]

    

    fondo = load_image("fondo1.png", IMG_DIR, alpha=False)
    bola = Pelota(50,50)    
    bola2 = PelotaRapida(25,25)
    bola3 = PelotaRapida(100,300)
    bolam = PelotaLentaM(500,100)
    bola5 = PelotaRapida1(25,25)
    bolac = PelotaCrece(70,110)
    bolab = PelotaBuena(150,70)
    bb = Pelota(200,50)
    bb1 = Pelota(400,400)
    bb2 = Pelota(345,123)
    player = Guy()
 
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 25)  # Activa repeticion de teclas
    pygame.mouse.set_visible(False)

    sonido_musica.play(10)          #reproduce musica fondo

    size = 1
    vidas = 10
    score = 0

    GameOver = False  #para un segundo while true (menu)


    lastscore = [0]    #hago una lista vacia para ir añadiendo todos los scores
    lasttime = [0]

    
    # el bucle principal del juego
    while game == True:

        #la intro + ultimo score
        while GameOver == False:
            fondo = load_image("fondo1.png", IMG_DIR, alpha=False)
            infoscore = fuente2.render("Last score: "+str(lastscore[-1]),0,(255,255,255))
            infotime = fuente2.render("Last time: "+str(lasttime[-1])+" sec.",0,(255,255,255))

            infoplayer = fuente2.render("That's You",0,(10,10,10))
            infoballm = fuente2.render("Avoid these balls",0,(10,10,10))
            infoballb = fuente2.render("Get this one",0,(10,10,10))

            infoPLAY = fuente3.render("press spacebar to PLAY",0,(10,10,10))


            
            reloj= [0]                                  #lista para los tiempos                       
            segundos3 = pygame.time.get_ticks()/1000




            player = Guy()
            player.humano()
            pos_mouse = pygame.mouse.get_pos()
            mov_mouse = pygame.mouse.get_rel()


            pygame.display.update()
            

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        GameOver = True
                        reloj.append(segundos3)     #agrego para que empiece a contar de cero
                        size = 1                    #resetea los parametros iniciales                  
                        vidas = 10
                        score = 0
                        pygame.mouse.set_pos([40,SCREEN_HEIGHT/2])  #te lleva el mouse a donde esta el guy
                        
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)
                    elif mov_mouse[1] != 0:
                        player.rect.centery = pos_mouse[1]
                        player.rect.centerx = pos_mouse[0]

            bola = Pelota(50,50)                 #los cargo devuelta pq dps de perder no empezaban del mismo lugar
            bola2 = PelotaRapida(25,25)
            bola3 = PelotaRapida(100,300)
            bolam = PelotaLentaM(200,50)          
            bola5 = PelotaRapida1(25,25)
            bolac = PelotaCrece(70,110)
            bolab = PelotaBuena(150,370)
            bb = Pelota(500,50)
            bb1 = Pelota(400,400)
            bb2 = Pelota(345,123)
            player = Guy()


            clock = pygame.time.Clock()
                        

            screen.blit(fondo, (0, 0))
            screen.blit(infoscore, (330,50))
            screen.blit(infoPLAY, (320,450))
            screen.blit(infotime, (330,70))
            screen.blit(infoballb,(170,365))
            screen.blit(infoballm,(60,60))
            screen.blit(infoplayer,(60,480/2))
            screen.blit(bb.image, bb.rect)
            screen.blit(bb1.image, bb1.rect)
            screen.blit(bb2.image, bb2.rect)
            screen.blit(bola.image, bola.rect)
            screen.blit(bola2.image, bola2.rect)
            screen.blit(bola3.image, bola3.rect)
            screen.blit(bolam.image, bolam.rect)
            screen.blit(bola5.image, bola5.rect)
            screen.blit(bolac.image, bolac.rect)
            screen.blit(bolab.image, bolab.rect)

            screen.blit(player.image, player.rect)
            screen.blit(bolac.image, bolac.rect)
            pygame.display.flip()            
            pygame.display.update()

  


            
            
        clock.tick(60)
        # Obtenemos la posicon del mouse
        pos_mouse = pygame.mouse.get_pos()
        mov_mouse = pygame.mouse.get_rel()
 
        # Actualizamos los obejos en pantalla
        player.humano()
        bola.update()
        bola2.update()
        bola3.update()
        bolam.update()
        bola5.update()
        bolac.update()
        bolab.update()
        bb.update()
        bb1.update()
        bb2.update()
 
        # Comprobamos si colisionan los objetos
        bola.colision(player)
        bola2.colision(player)
        bola3.colision(player)
        bolam.colision(player)
        bolac.colision(player)
        bola5.colision(player)
        bolab.colision(player)
        bb.colision(player)
        bb1.colision(player)
        bb2.colision(player)


        if bolab.rect.colliderect(player.rect):
            score += 1
            bolab = PelotaBuena(int(random.randrange(50,590)),int(random.randrange(50,400)))  
            sonidos_buenos[int(random.randrange(3))].play()
       

        if bola.rect.colliderect(player.rect):
            vidas -= 1
            sonidos_malos[int(random.randrange(3))].play()
                  
        if bolac.rect.colliderect(player.rect):
            size += 1
            bolac = PelotaCrece(int(random.randrange(50,590)),int(random.randrange(50,400)))
            sonido_big.play()

        if bola3.rect.colliderect(player.rect):
            vidas -= 1
            sonidos_malos[int(random.randrange(3))].play()
        if bola2.rect.colliderect(player.rect):
            vidas -= 1
            sonidos_malos[int(random.randrange(3))].play()
        if bola5.rect.colliderect(player.rect):
            vidas -= 1
            sonidos_malos[int(random.randrange(3))].play()
            
        if bolam.rect.colliderect(player.rect):
            vidas -= 2
            sonido_no.play()
            killchance = int(random.randrange(10))     # 5/11 chances que te mate de una
            if killchance >= 6:                
                vidas = 0
        if bb.rect.colliderect(player.rect):
            vidas -= 1
            sonidos_malos[int(random.randrange(3))].play()

        if bb1.rect.colliderect(player.rect):
            vidas -= 1
            sonidos_malos[int(random.randrange(3))].play()

        if bb2.rect.colliderect(player.rect):
            vidas -= 1
            sonidos_malos[int(random.randrange(3))].play()

        



        if size%2 ==0:
            player.image = load_image("guy1.png", IMG_DIR, alpha=True)
        else:   player.image = load_image("guy.png", IMG_DIR, alpha=True)  

        if score == 100:
            print("You win")
            print("Score: ",score)
            print("life/s left: ",vidas)
            print("Time: ",segundos2)
            GameOver = False
            lastscore.append(score)
            lasttime.append(int(segundos)-int(segundos3))     #tiempo desde q abrio el programa - tiempo de que juego
            print(lastscore)



        

        if vidas == 0 or vidas < 0:
            print("You lose")
            print("Score: ",score)
            print("life/s left: ",vidas)
            GameOver = False
            lastscore.append(score)
            lasttime.append(int(segundos)-int(segundos3))
            print(lastscore)



        segundos = pygame.time.get_ticks()/1000
        segundos2 = pygame.time.get_ticks()/1000
        tiempo = str(int(segundos)-int(segundos3))      #hago la resta tiempo que inicio el programa- tiempo que estoy jugando
        segundos2 =int(segundos2)
        cronometro = fuente1.render("Time: "+tiempo,0,(1,1,1))
        puntaje = fuente2.render("Score: "+str(score),0, (20,20,20))
        health = fuente2.render("Health: "+str(vidas),0,(20,20,20))

                
            
            
  
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            
            # Si el mouse no esta quieto mover la paleta a su posicion
            elif mov_mouse[1] != 0:
                player.rect.centery = pos_mouse[1]
                player.rect.centerx = pos_mouse[0]
 
        # actualizamos la pantalla
        screen.blit(fondo, (0, 0))
        screen.blit(info1,(5,5))
        screen.blit(info2,(540,5))
        screen.blit(cronometro,(300,5))
        screen.blit(puntaje,(540,450))
        screen.blit(health,(2,450))
        screen.blit(bb.image, bb.rect)
        screen.blit(bb1.image, bb1.rect)
        screen.blit(bb2.image, bb2.rect)
        screen.blit(bola.image, bola.rect)
        screen.blit(bola2.image, bola2.rect)
        screen.blit(bola3.image, bola3.rect)
        screen.blit(bolam.image, bolam.rect)
        screen.blit(bola5.image, bola5.rect)
        screen.blit(bolac.image, bolac.rect)
        screen.blit(bolab.image, bolab.rect)
        screen.blit(player.image, player.rect)
        pygame.display.flip()




 
 
if __name__ == "__main__":
    main()
