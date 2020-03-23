def ChooseClass():
    import pygame
    pygame.init()
    pygame.font.init()
    pygame.display.init()                                                       
    screen = pygame.display.set_mode(size = (1300,800))

    f = pygame.font.Font(None, 50)

    FighterRect = pygame.Rect(600, 200, 150, 50)                                   
    FighterColor = pygame.Color(150, 50, 100, 255)
    
    FighterButDraw = pygame.draw.rect(screen, FighterColor, FighterRect)                                                   

    FighterText = f.render('Fighter', True, (255,255,100))                              
    screen.blit(FighterText, FighterRect, area=None, special_flags=0)



    

    RogueRect = pygame.Rect(400, 200, 150, 50)
    RogueColor = pygame.Color(150, 50, 100, 255)
    
    RogueButDraw = pygame.draw.rect(screen, RogueColor, RogueRect)

    RogueText = f.render('Rogue', True, (255,255,100))                              
    screen.blit(RogueText, RogueRect, area=None, special_flags=0)


    

    MageRect = pygame.Rect(800, 200, 150, 50)                                   
    MageColor = pygame.Color(150, 50, 100, 255)
    
    MageButDraw = pygame.draw.rect(screen, MageColor, MageRect)

    MageText = f.render('Mage', True, (255,255,100))                              
    screen.blit(MageText, MageRect, area=None, special_flags=0)

    RectUps = (FighterRect, RogueRect, MageRect)
    pygame.display.update(RectUps)
