def OpenStartScreen():
    import pygame, ChooseClassScreen,CaptRectcreate
    pygame.init()
    pygame.font.init()
    pygame.display.init()                                                       #Initialisiert das display module



    pygame.display.set_caption('Rats Everywhere')
    StartScreen = pygame.display.set_mode(size = (1300,800))                        #Initilisiert die display surface
                                 
    ExitRect = CaptRectcreate.CaptRect((100,600),(150,50),'Exit')
   
    StartRect = CaptRectcreate.CaptRect((100,400),(100,50),'Start')
    
    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
    while a == 0:
        for event in pygame.event.get():                                        #grabs all events from the event que      
            if event.type == pygame.MOUSEBUTTONDOWN:                            #Checks if these events are Mousebuttonpresses
                if ExitRect.collidepoint(pygame.mouse.get_pos()):              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                    a = 2
                    pygame.display.quit()
                    break                                                   #closes entire display module
                
                elif StartRect.collidepoint(pygame.mouse.get_pos()):
                    a = 1
                    StartButDraw = pygame.draw.rect(StartScreen, (0,0,0), StartRect)
                    ChooseClassScreen.ChooseClass()
            else:
                continue


        
    
