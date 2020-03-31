import pygame, ChooseClassScreen, Class_Rect

def info_classes(screen,exit,zur,id):
    confirm = Class_Rect.TextBox(screen,(500,600),(150,50),50,'Confirm')
    confirm.draw_button()
    if id == 1:
        fighter = Class_Rect.TextBox(screen,(50,80),(800,400),50,'   Fighter Overview')
        fighter_rect = fighter.give_rect()
        exit.draw_button()
        zur.draw_button()
        fighter.draw_button()
        text = """



        The fighter is a strong melee fighter with high health and good defense. He excells in physical
        combat, brute force approaches and enduring damage. The fighter fairs fairly well in social
        interactions, mostly due to his, at least in his own and allied kingdoms, high social standing.
        His education mostly focused on the history of armed conflicts, on-the-fly construction of
        makeshift battlements like barricades and simple siege engines. He is also educated in the ways
        of court, speaking to authorities, and leading less experienced warriors or peasants into battle
        or supervising them in other projects. Furthermore he can usually tell the state and quality of
        armor weapons and other non-magical equipment in a matter of seconds. The fighter usually
        struggles when it comes to mechanical as well as political or magical understanding. Also
        using stealth,trapping or deceiving doesn't fit most fighters code of honor, which is why they
        aren't very adept at it when they do try.

        In Combat the fighter focuses on direct physical damage and stunning, disarming or out-maneuvering his
        enemy to get an advantage. His armor prevents him from a decent amount of most damage
        sources. Only magical damage is a real threat to him as well as being vastly outnummbered"""

        fighter.draw_multi_line(text)

        a = 0
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        while a == 0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit.check_press(event):
                        a = 1
                        pygame.display.quit()
                    elif zur.check_press(event):
                        fighter.delete()
                        confirm.delete()
                        a = 1
                        ChooseClassScreen.choose_class(screen)
                    elif confirm.check_press(event):
                    #set_class_fighter()
                        a=1
                        pygame.display.quit()

    elif id == 2:
        rogue = Class_Rect.TextBox(screen,(50,50),(300,300),50,'Rogue')
        rogue_rect = rogue.give_rect()
        exit.draw_button()
        zur.draw_button()
        rogue.draw_button()

        a = 0
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        while a == 0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit.give_rect().collidepoint(pygame.mouse.get_pos()):
                        a = 1
                        pygame.display.quit()
                    elif zur.check_press(event):
                        rogue.delete()
                        confirm.delete()
                        a = 1
                        ChooseClassScreen.choose_class(screen)
                    elif confirm.check_press(event):
                        #set_class_fighter()
                        a=1
                        pygame.display.quit()

    elif id == 3:
        mage = Class_Rect.TextBox(screen,(50,50),(300,300),50,'Mage')
        mage_rect = mage.give_rect()
        exit.draw_button()
        zur.draw_button()
        mage.draw_button()

        a = 0
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        while a == 0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit.check_press(event):
                        a = 1
                        pygame.display.quit()
                    elif zur.check_press(event):
                        mage.delete()
                        confirm.delete()
                        a = 1
                        ChooseClassScreen.choose_class(screen)
                    elif confirm.check_press(event):
                        #set_class_fighter()
                        a=1
                        pygame.display.quit()
