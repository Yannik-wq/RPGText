import pygame
import sys
import Class_Rect
import ChooseClassScreen

def open_start_screen(screen, exit):
                                                         #Initialisiert das display module
    exit.draw_button()
    start = Class_Rect.TextBox(screen,(100,400),(100,50),50,'Start')
    start.draw_button()

    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
    while a == 0:
        for event in pygame.event.get():                                        #grabs all events from the event queue
            if event.type == pygame.MOUSEBUTTONDOWN:                            #Checks if these events are Mousebuttonpresses
                if exit.check_press(event):              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                    a = 2
                    pygame.display.quit()
                    sys.exit(0)
                elif start.check_press(event):
                    a = 1
                    start.delete()

    id = ChooseClassScreen.choose_class(screen, exit)
    return (id)
