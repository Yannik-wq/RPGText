import pygame
pygame.init()
pygame.font.init()
pygame.display.init()                                                       #Initialisiert das display module

pygame.display.set_caption('Rats Everywhere')
screen = pygame.display.set_mode(size = (1300,800))                        #Initilisiert die display surface
#pygame.fill((50,50,0),screen)
Firstrect = pygame.Rect(100, 600, 1100, 50)                                  # creates the rectangle 'Firstrect' at position x:50;y:300, with width 50 and height 100 
Firstcolor = pygame.Color(150, 50, 100, 255)                                # Definiert das Color Object 'firstcolor'

Buttondraw = pygame.draw.rect(screen, Firstcolor, Firstrect)                #draws a rectangle on the surface 'screen' with the color "firstcolor" at the position of 'firstrect'

pygame.display.update(Firstrect)                                            # updates the surface at the position of 'Firstrect'
f = pygame.font.Font(None, 20)
EndBut = f.render('Ende', True, (255,255,100))
pygame.display.flip()
a = 0
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
while a == 0:
    for event in pygame.event.get():                                        #grabs all events from the event que      
        if event.type == pygame.MOUSEBUTTONDOWN:                            #Checks if these events are Mousebuttonpresses
            if Firstrect.collidepoint(pygame.mouse.get_pos()):              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                a = 1
        else:
            continue
        
pygame.display.quit()                                                       #closes entire display module
