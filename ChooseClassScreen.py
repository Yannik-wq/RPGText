import pygame, Class_Rect, OpenStartScreen, InfoFighter



def choose_class(screen):

    #zscreen = pygame.display.set_mode(size = (1300,1000))
    #screen = pygame.display.set_mode(size = (1300,1000))
    #pygame.display.flip()


    #fighter_rect = CaptRectcreate.capt_rect((600,200),(150,50),'Fighter',50)
    fighter =  Class_Rect.TextBox(screen,(600,200),(150,50),50,'Fighter')
    fighter_rect = fighter.give_rect()
    fighter.draw_button()

    #rogue_rect = CaptRectcreate.capt_rect((400,200),(150,50),'Rogue',50)
    rogue =  Class_Rect.TextBox(screen,(400,200),(150,50),50,'Rogue')
    rogue_rect = rogue.give_rect()
    rogue.draw_button()

    #mage_rect = CaptRectcreate.capt_rect((800,200),(150,50),'Mage',50)
    mage =  Class_Rect.TextBox(screen,(800,200),(150,50),50,'Mage')
    mage_rect = mage.give_rect()
    mage.draw_button()

    #exit_rect = CaptRectcreate.capt_rect((100,600),(150,50),'Exit',50)
    exit =  Class_Rect.TextBox(screen,(100,600),(100,50),50,'Exit')
    exit_rect = exit.give_rect()
    exit.draw_button()

    #zur_rect = CaptRectcreate.capt_rect((300,600),(150,50),'Zurück',50)
    zur =  Class_Rect.TextBox(screen,(300,600),(150,50),50,'Zurück')
    zur_rect = zur.give_rect()
    zur.draw_button()

    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    while a == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fighter_rect.collidepoint(pygame.mouse.get_pos()):
                    a = 0
                    fighter.delete()
                    rogue.delete()
                    mage.delete()
                    InfoFighter.info_fighter(screen,exit,zur)
                elif rogue_rect.collidepoint(pygame.mouse.get_pos()):
                    a = 0
                    #InfoRogue()
                elif mage_rect.collidepoint(pygame.mouse.get_pos()):
                    a = 0
                    #InfoMage()
                elif exit_rect.collidepoint(pygame.mouse.get_pos()):
                    a = 1
                    pygame.display.quit()
                elif zur_rect.collidepoint(pygame.mouse.get_pos()):
                    #pygame.display.flip()
                    a = 1
                    zur.delete()
                    fighter.delete()
                    rogue.delete()
                    mage.delete()
                    OpenStartScreen.open_start_screen()
