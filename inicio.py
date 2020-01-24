import pygame
import starship

def main():
    pygame.init()
    pygame.font.init()
    
    width = 490 #Ancho pantalla
    height = 490 #Alto pantalla
    arrow_up = True #Se va a usar para detectar si presióno o no la flecha para arriba para moverse por el emnu
    captured_event = None
    
    rect = pygame.Rect(0,310,10,58) #Establezco el objeto rect
    
    font = pygame.font.SysFont('arial',60) #Establezco la fuente de la letra
    space_text = font.render("SPACE", True, [238,226,71], [0,0,0])     #render('Texto',True,[R,G,B colores de la letra],[R G B color fondo de letra])
    invaders_text = font.render("INVADERS", True, [238,226,71], [0,0,0])
    main_text = font.render("START", True, [238,226,71], [0,0,0])
    exit_text = font.render("EXIT", True, [238,226,71], [0,0,0])

    background = pygame.image.load('inicio.jpeg')
    screen = pygame.display.set_mode((width,height))

    while True:
        try:
            for event in pygame.event.get():
                captured_event = event #Guardo el evento capturado
            if captured_event.type == 12:
                pygame.quit()
                arrow_up = None
                break
            if captured_event.type == pygame.KEYDOWN:
                if captured_event.key == pygame.K_UP and not arrow_up:
                    arrow_up = True
                    rect = pygame.Rect(0,310,10,58) #Establezco el objeto rect
                    pygame.draw.rect(screen, [136,136,136],rect) #Dibujo el rect (pantalla,color rgb, objeto_rect)
                elif captured_event.key == pygame.K_DOWN and arrow_up:
                    arrow_up = False
                    rect = pygame.Rect(0,370,10,58) #Establezco el objeto rect
                    pygame.draw.rect(screen, [136,136,136],rect) #Dibujo el rect (pantalla,color rgb, objeto_rect)
                if captured_event.key==pygame.K_SPACE:
                    pygame.quit()
                    break
                    
            screen.fill((0,0,0)) #Dibujo el fondo color negro
            pygame.draw.rect(screen, [136,136,136],rect) #Dibujo el rect (pantalla,color rgb, objeto_rect)
            screen.blit(space_text,(130,30)) #Dibujo el texto "SPACE"
            screen.blit(invaders_text,(85,120)) #Dibujo el texto "INVADERS"
            screen.blit(main_text,(20,300)) #Dibujo el texto "START"
            screen.blit(exit_text,(20,370)) #Dibujo el texto "EXIT"
            pygame.display.flip() #Actualizo los cambios en pantalla
        except pygame.error:
            pass

    if arrow_up is not None and arrow_up:
        starship.main()
if __name__ == '__main__':
    main()