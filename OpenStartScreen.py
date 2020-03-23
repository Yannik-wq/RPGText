def OpenStartScreen():
    import pygame
    pygame.init()
    pygame.font.init()
    pygame.display.init()                                                       #Initialisiert das display module

    pygame.display.set_caption('Rats Everywhere')
    StartScreen = pygame.display.set_mode(size = (1300,800))                        #Initilisiert die display surface

    ExitRect = pygame.Rect(100, 600, 100, 50)                                  # creates the rectangle 'Firstrect' at position x:50;y:300, with width 50 and height 100 
    ExitColor = pygame.Color(150, 50, 100, 255)                                # Definiert das Color Object 'firstcolor'

    ExitButDraw = pygame.draw.rect(StartScreen, ExitColor, ExitRect)                #draws a rectangle on the surface 'screen' with the color "firstcolor" at the position of 'firstrect'

    StartRect = pygame.Rect(100, 400, 100, 50)
    StartColor = pygame.Color(150, 50, 100, 255)
    StartButDraw = pygame.draw.rect(StartScreen, StartColor, StartRect)

    #pygame.display.update(Firstrect, Startrect)                            # updates the surface at the position of 'Firstrect'


    f = pygame.font.Font(None, 50)                                              #sets the font and size of text None means system default font


    ExitBut = f.render('Exit', True, (255,255,100))                              #Endbut is the new surface on which the text 'Exit is drawn, colorcode in ()
    StartScreen.blit(ExitBut, ExitRect, area=None, special_flags=0)                  # the surface 'Endbut' is merged with the main surface 'screen' at the location of Firstrect



    StartBut = f.render('Start', True, (255,255,100))
    StartScreen.blit(StartBut, StartRect, area=None, special_flags=0)

    RectUps = (ExitRect,StartRect)
    pygame.display.update(RectUps)
    #pygame.display.update(StartRect)
    #pygame.display.flip()
    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
    while a == 0:
        for event in pygame.event.get():                                        #grabs all events from the event que      
            if event.type == pygame.MOUSEBUTTONDOWN:                            #Checks if these events are Mousebuttonpresses
                if ExitRect.collidepoint(pygame.mouse.get_pos()):              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                    a = 1
                    pygame.display.quit()                                                       #closes entire display module
                elif StartRect.collidepoint(pygame.mouse.get_pos()):
                    a = 1
                    ChooseClass()
            else:
                continue


        
    
