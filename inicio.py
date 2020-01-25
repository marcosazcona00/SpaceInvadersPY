import pygame
import starship

def try_game_again(enemys_killed):
    """
        Retorna si quiere o no continuar
    """
    pygame.init()
    pygame.font.init()

    captured_event = None

    cursor_yes = True #El cursor inicialmente va a estar para presionar SI (para reintentar de vuelta)

    screen = pygame.display.set_mode((300,300))

    font_text = pygame.font.SysFont('arial',30)
    no = font_text.render('NO',True,[238,226,71], [0,0,0] )
    yes = font_text.render('SI',True,[238,226,71], [0,0,0] )
    score_text = font_text.render('PUNTAJE',True,[238,226,71], [0,0,0] )
    enemys_killed_text = font_text.render(str(enemys_killed),True, [238,226,71], [0,0,0])

    rect = pygame.Rect(20,205,20,20) #Posiciono el rectangulo apuntando al SI

    while True:
        screen.fill((0,0,0))
      
        try:
            for event in pygame.event.get():
                captured_event = event

            if captured_event.type == 12:
                #Si toca la X para cerrar la pantalla
                pygame.quit()
                break
            elif captured_event.type == pygame.KEYDOWN:
                if captured_event.key == pygame.K_LEFT and not cursor_yes:
                    rect = pygame.Rect(20,205,20,20) #Posiciono el rectangulo apuntando al SI
                    cursor_yes = True #Ahora el cursor si apunta al SI
                elif captured_event.key == pygame.K_RIGHT and cursor_yes:
                    rect = pygame.Rect(150,205,20,20) #Posiciono el rectangulo apuntando al NO
                    cursor_yes = False #Ahora el cursor apunta al NO. 
                elif captured_event.key == pygame.K_SPACE:
                    pygame.quit()
                    break

            pygame.draw.rect(screen,[136,136,136],rect) #Dibujo el rectangulo
            #----------------Dibujo los textos ---------------------- #
            screen.blit(score_text,(70,50))
            screen.blit(enemys_killed_text,(120,100))
            screen.blit(yes,(50,200))
            screen.blit(no,(180,200))
            #-------------------------------------------------------- #
            pygame.display.flip() #Actualizo los cambios

        except pygame.error:
            pass    

    return cursor_yes #Retorno si eligió SI o NO. True si toco SI, False si tocó NO


def main():
    """
        MAIN QUE MUESTRA EL PRIMER MENU
    """
    pygame.init()
    pygame.font.init()
    
    width = 490 #Ancho pantalla
    height = 490 #Alto pantalla
    arrow_up = True #Se va a usar para detectar si presióno o no la flecha para arriba para moverse por el emnu
    captured_event = None
    
    
    font = pygame.font.SysFont('arial',60) #Establezco la fuente de la letra
    space_text = font.render("SPACE", True, [238,226,71], [0,0,0])     #render('Texto',True,[R,G,B colores de la letra],[R G B color fondo de letra])
    invaders_text = font.render("INVADERS", True, [238,226,71], [0,0,0])
    
    font_2 = pygame.font.SysFont('arial',30)
    main_text = font_2.render("INICIAR", True, [238,226,71], [0,0,0])
    exit_text = font_2.render("SALIR", True, [238,226,71], [0,0,0])

    rect = pygame.Rect(0,300,10,30) #DIbujo el rectangulo apuntado al Iniciar

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
                    rect = pygame.Rect(0,300,10,30) #Dibujo el rectangulo apuntando al Iniciar
                elif captured_event.key == pygame.K_DOWN and arrow_up:
                    arrow_up = False
                    rect = pygame.Rect(0,370,10,30) #Dibujo el rectangulo apuntando al Salir
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
        #Si está posicionado en "START basicamente"
        wantsContinue = True
        while wantsContinue:
            enemys_killed = starship.main() #Ejecuto el main del Starship
            wantsContinue = try_game_again(enemys_killed)
if __name__ == '__main__':
    main()