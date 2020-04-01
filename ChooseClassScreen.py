import pygame, Class_Rect, OpenStartScreen, InfoClass, sys



def choose_class(screen):


    fighter =  Class_Rect.TextBox(screen,(600,200),(150,50),50,'Fighter')
    fighter.draw_button()

    rogue =  Class_Rect.TextBox(screen,(400,200),(150,50),50,'Rogue')
    rogue.draw_button()

    mage =  Class_Rect.TextBox(screen,(800,200),(150,50),50,'Mage')
    mage.draw_button()

    exit =  Class_Rect.TextBox(screen,(100,600),(100,50),50,'Exit')
    exit.draw_button()

    #zur_rect = CaptRectcreate.capt_rect((300,600),(150,50),'Zurück',50)
    zur =  Class_Rect.TextBox(screen,(300,600),(150,50),50,'Zurück')
    zur.draw_button()

    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    while a == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
        #event.type == pygame.MOUSEBUTTONDOWN:
                if fighter.check_press(event):
                    a = 1
                    fighter.delete()
                    rogue.delete()
                    mage.delete()
                    InfoClass.info_classes(screen, exit, zur,a)
                elif rogue.check_press(event):
                    a = 2
                    fighter.delete()
                    rogue.delete()
                    mage.delete()
                    InfoClass.info_classes(screen, exit, zur,a)
                elif mage.check_press(event):
                    a = 3
                    fighter.delete()
                    rogue.delete()
                    mage.delete()
                    InfoClass.info_classes(screen, exit, zur,a)
                elif exit.check_press(event):
                    a = 4
                    pygame.display.quit()
                    sys.exit(0)

                elif zur.check_press(event):
                    zur.delete()
                    fighter.delete()
                    rogue.delete()
                    mage.delete()
                    OpenStartScreen.open_start_screen()
                    break
