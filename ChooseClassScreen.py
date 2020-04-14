import pygame
import sys
import Class_Rect
import OpenStartScreen
import InfoClass
ct = Class_Rect
os = OpenStartScreen
ic = InfoClass
def choose_class(screen, exit):

    fighter =  ct.TextBox(screen,(600,200),(150,50),50,'Fighter')
    fighter.draw_button()

    rogue =  ct.TextBox(screen,(400,200),(150,50),50,'Rogue')
    rogue.draw_button()

    mage =  ct.TextBox(screen,(800,200),(150,50),50,'Mage')
    mage.draw_button()

    exit.draw_button()

    zur =  ct.TextBox(screen,(300,600),(150,50),50,'Zurück')

    def delete():
        fighter.delete()
        rogue.delete()
        mage.delete()



    id = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    while id not in[1,2,3]:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fighter.check_press(event):
                    a = 1
                    delete()
                    id = ic.info_fighter(screen, exit, zur)
                elif rogue.check_press(event):
                    a = 2
                    delete()
                    id = ic.info_rogue(screen, exit, zur)
                elif mage.check_press(event):
                    a = 3
                    delete()
                    id = ic.info_mage(screen, exit, zur)
                elif exit.check_press(event):
                    a = 4
                    pygame.display.quit()
                    sys.exit(0)
    return(id)
