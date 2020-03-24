def ChooseClass():
    import pygame, CaptRectcreate, OpenStartScreen
    pygame.init()
    pygame.font.init()
    pygame.display.init()                                                       
    screen = pygame.display.set_mode(size = (1300,1000))


        
    FighterRect = CaptRectcreate.CaptRect((600,200),(150,50),'Fighter')
    
    RogueRect = CaptRectcreate.CaptRect((400,200),(150,50),'Rogue')


    MageRect = CaptRectcreate.CaptRect((800,200),(150,50),'Mage')
    

    ExitRect = CaptRectcreate.CaptRect((100,600),(150,50),'Exit')

    
    ZurRect = CaptRectcreate.CaptRect((100,400),(150,50),'Zurück')
    

    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            
    while a == 0:
        for event in pygame.event.get():                                        
            if event.type == pygame.MOUSEBUTTONDOWN:                            
                if FighterRect.collidepoint(pygame.mouse.get_pos()):              
                    a = 0
                    #InfoFighter()                                                      
                elif RogueRect.collidepoint(pygame.mouse.get_pos()):
                    a = 0
                    #InfoRogue()
                elif MageRect.collidepoint(pygame.mouse.get_pos()):
                    a = 0
                    #InfoMage()
                elif ExitRect.collidepoint(pygame.mouse.get_pos()):              
                    a = 1
                    pygame.display.quit()
                elif ZurRect.collidepoint(pygame.mouse.get_pos()):
                    pygame.display.flip()
                    OpenStartScreen.OpenStartScreen()
                    break
            else:
                continue
