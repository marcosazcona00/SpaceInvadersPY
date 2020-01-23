import pygame
import threading
from time import sleep
from random import randint

class Enemy:
    def __init__(self):
        #El enemigo es de 20x20
        self.__yPosition = -20
        self.__xPosition = randint(0,600)
        self.__image = pygame.image.load('enemigo.png')
    
    def x_position(self):
        return self.__xPosition

    def y_position(self):
        return self.__yPosition

    def draw(self,screen):
        """
            Este método dibuja al enemigo
        """
        screen.blit(self.__image,(self.__xPosition,self.__yPosition))       
        self.__yPosition += 10
        sleep(0.001)

    def collideX(self,xStarshipPosition):
        """
           Este método verifica si el enemigo colisiona con la nave sobre el eje X
        """
        return xStarshipPosition >= self.__xPosition - 30 and xStarshipPosition <= self.__xPosition
    
    def collideY(self,yStarshipPosition):
        """
            Verifica si el bicho colisiona sobre el eje Y con la nave
        """
        return self.__yPosition >= yStarshipPosition and self.__yPosition <= yStarshipPosition + 40

    def exceded(self):
        """
            Este método retorna True el enemigo llegó al limite inferior de la pantalla
        """
        return self.__yPosition > 600

class Ball:
    def __init__(self,xStarshipPosition,ballIndex):
        #Recibo xStarshipPosition (posicion de la nave) porque desde el X de la nave disparo la bala
        self.__ballIndex = ballIndex #Se usa para distinguir qué numero de bala es
        self.__yPosition = 600 - 100
        self.__xPosition = xStarshipPosition
        self.__image = pygame.image.load('bala.jpeg')

    def shoot(self,screen):
        """
            Este método dibuja la bala en pantalla
        """
        print('Bala X {} Y {} '.format(self.__xPosition,self.__yPosition))
        screen.blit(self.__image,(self.__xPosition,self.__yPosition)) #Cambia de posicion la bala
        self.__yPosition -= 10 #Lo mueve 10 pixeles para atras

    def exceded(self):
        """
            Retorna true si la bala se pasó del límite superior de la pantalla. False si no se pasó
        """
        return self.__yPosition < 0

    def collideX(self,xEnemyPosition):
        """
            Retorna True si la bala colisiona con el enemigo sobre el eje X
        """
        return xEnemyPosition >= self.__xPosition - 30 and xEnemyPosition <= self.__xPosition

    def collideY(self,yEnemyPosition):
        """
            Retorna True si la bala colisiona con el enemigo sobre el eje X
        """
        return self.__yPosition >= yEnemyPosition and self.__yPosition <= yEnemyPosition + 40


class Starship:
    def __init__(self,width,height):
        self.__munition = list() #Lista de municiones
        self.__ballIndex = 0 #Indice para moverme en la lista de balas
        self.__xPosition = width // 2 - 50
        self.__yPosition = height - 100 
        self.__image = pygame.image.load('nave2.png')

    def draw(self,screen):
        """
            Dibuja la nave en la pantalla
        """
        screen.blit(self.__image,(self.__xPosition,self.__yPosition))

    def x_position(self):
        return self.__xPosition

    def y_position(self):
        return self.__yPosition

    def move_right(self):
        if self.__xPosition < 520:
            self.__xPosition += 10

    def move_left(self):
        if self.__xPosition > 0:
            self.__xPosition -= 10

    def shoot(self,screen):
        """
            Devuelve el objeto bala
        """
        self.__munition.append(Ball(self.__xPosition, self.__ballIndex)) #Creo la nueva bala
        self.__ballIndex += 1 #Incremento el indice
        return self.__munition[self.__ballIndex - 1] #Como incremente, si la primera vez que creo la bala ballIndex es 0,ahora es 1 y cuando pida en la lista ese elemento no va a estar porque solo va a estar ocupada la posicion 0



def main():

    pygame.init()
    screen_width = 600
    screen_height = 600
    captured_event = None
    used_munitions = list() #Lista de municiones
    background_color = (82,86,85)
    #enemys = [Enemy() for x in range(0,10)]
    starship = Starship(screen_width,screen_height)
    screen = pygame.display.set_mode((screen_width,screen_height))

    screen.fill(background_color)

    i = 0

    enemy = Enemy() #Creo un enemigo

    while True:

        try:

            for event in pygame.event.get():
                captured_event = event #Guardo el evento capturado
            if captured_event is not None and captured_event.type == 12:
                pygame.quit()
                break
            elif captured_event is not None and captured_event.type == pygame.KEYDOWN:
                #pygame.KEYDOWN si presionó una tecla del teclado
                if captured_event.key == pygame.K_LEFT:
                    starship.move_left()
                elif captured_event.key == pygame.K_RIGHT:
                    starship.move_right()
                elif captured_event.key == pygame.K_UP:
                    captured_event = None #Si no pongo esto queda trabado el K_UP Y tira 2 balas en vez de una
                    used_munitions.append(starship.shoot(screen)) #Como toco la flecha para arriba para disparar, agrego a la lista de balas una nueva bala
            
            screen.fill(background_color)

            #----- Carga las balas en pantalla ------#
            for munition in used_munitions:
                munition.shoot(screen) #Dibujo la animación de disparo de cada bala que haya sido disparada
            #----------------------------------------#
            print('Enemigo X {} Y {}'.format(enemy.x_position(),enemy.y_position()))
            #------ Verifica si cada bala se paso del limite de la pantalla y la saca de la lista ----------#
            for munition in used_munitions:
                if munition.exceded():
                    used_munitions.pop(0) #Saco la primer bala que llegó al límite de la lista
                else:
                    #Si la munición no excedió, sigue moviendose
                    if munition.collideY(enemy.y_position()) and munition.collideX(enemy.x_position()):
                        print('Colision!')
                        used_munitions.pop(0) #Saco la primer bala porque ya impactó
                        enemy = Enemy() #Creo al nuevo enemigo porque lo tocó
                    

            #----------------------------------------_#
            
            colisionoX = enemy.collideX(starship.x_position())
            colisionoY = enemy.collideY(starship.y_position())
            
            if enemy.exceded() and not colisionoX and not colisionoY:
                #Si el enemigo se pasó de los limites de la pantalla y no colisiono
                enemy = Enemy() #Creo un nuevo enemigo
            elif colisionoX and colisionoY:
                #Si colisiono
                print('FIN DEL JUEGO')
                break
                
            starship.draw(screen)
            enemy.draw(screen)
            pygame.display.flip() #Actualizo los cambios hechos
            sleep(0.03)
            
        except pygame.error:
            pass

if __name__ == '__main__':
    main()
