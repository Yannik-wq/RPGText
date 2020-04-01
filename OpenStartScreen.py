import pygame, ChooseClassScreen, Class_Rect, sys

def open_start_screen():
                                                         #Initialisiert das display module

    start_screen = pygame.display.set_mode(size = (1300,800))                        #Initilisiert die display surface

    exit =  Class_Rect.TextBox(start_screen,(100,600),(100,50),50,'Exit')
    exit.draw_button()

    start = Class_Rect.TextBox(start_screen,(100,400),(100,50),50,'Start')
    start.draw_button()

    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
    while a == 0:
        for event in pygame.event.get():                                        #grabs all events from the event que
            if event.type == pygame.MOUSEBUTTONDOWN:                            #Checks if these events are Mousebuttonpresses
                if exit.check_press(event) == True:              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                    a = 2
                    pygame.display.quit()
                    sys.exit(0)

                elif start.check_press(event) == True:
                    a = 1
                    start.delete()
                    ChooseClassScreen.choose_class(start_screen)
