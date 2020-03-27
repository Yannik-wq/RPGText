import pygame, ChooseClassScreen, Class_Rect

def open_start_screen():
                                                         #Initialisiert das display module

    start_screen = pygame.display.set_mode(size = (1300,800))                        #Initilisiert die display surface

    exit =  Class_Rect.TextBox(start_screen,(100,600),(100,50),50,'Exit')
    exit_rect = exit.give_rect()
    exit.draw_button()
    #CaptRectcreate.capt_rect((100,600),(150,50),'Exit',50)

    start = Class_Rect.TextBox(start_screen,(100,400),(100,50),50,'Start')
    #CaptRectcreate.capt_rect((100,400),(100,50),'Start',50)
    start_rect = start.give_rect()
    start.draw_button()

    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
    while a == 0:
        for event in pygame.event.get():                                        #grabs all events from the event que
            if event.type == pygame.MOUSEBUTTONDOWN:                            #Checks if these events are Mousebuttonpresses
                if exit_rect.collidepoint(pygame.mouse.get_pos()):              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                    a = 2
                    pygame.display.quit()

                elif start_rect.collidepoint(pygame.mouse.get_pos()):
                    a = 1
                    start.delete()
                    #StartButDraw = pygame.draw.rect(start_screen, (0,0,0), start_rect)
                    ChooseClassScreen.choose_class(start_screen)
