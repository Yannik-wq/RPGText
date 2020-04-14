import pygame
import ChooseClassScreen
import Class_Rect
import Start_Game
import classes
cr = Class_Rect
c = classes
C = ChooseClassScreen



def info_fighter(screen,exit,zur):
    confirm = cr.TextBox(screen,(500,600),(150,50),50,'Confirm')
    confirm.draw_button()
    zur.draw_button()
    exit.draw_button()
    fighter = cr.TextBox(screen,(50,80),(800,400),50,'   Fighter Overview')
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

        In Combat the fighter focuses on direct physical damage and stunning, disarming or
        out-maneuvering his enemy to get an advantage. His armor prevents him from a decent amount
        of most damage sources. Only magical damage is a real threat to him as well as being vastly
        outnummbered"""

    fighter.draw_multi_line(text)

    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    while a == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.check_press(event):
                    a = 1
                    pygame.display.quit()
                elif confirm.check_press(event):
                    fighter.delete()
                    confirm.delete()
                    zur.delete()
                    return(1)
                    a=1
                elif zur.check_press(event):
                    a = 1
                    fighter.delete()
                    confirm.delete()
                    zur.delete()
                    d = C.choose_class(screen, exit)
                    return(d)


def info_rogue(screen,exit,zur):
    confirm = cr.TextBox(screen,(500,600),(150,50),50,'Confirm')
    confirm.draw_button()
    zur.draw_button()
    exit.draw_button()
    rogue = cr.TextBox(screen,(50,80),(800,400),50,'   Rogue Overview')
    rogue.draw_button()

    text = """



        A Rogue is a nimble and very dexterous combatant. In battle he focuses on avoiding enemy
        hits while often using poisons, backstabs or ranged weapons to deal with an opponenet
        as quick as possible. Rogues are also adept in using traps or misdirections to get an
        advantage. Extended fights usually mean trouble for a rogue since he usually doesn't
        wear protective armor and therefor takes considerable damage when he does get hit.

        Most rogues have a solid understanding of mechanical aspects and have the ability to
        improvise.They are often experienced at pickpocketing, extortion and deception and posses
        a high perception. These abilities serve them very well when it comes to negotiations,
        acquiring money, spotting ambushes or traps and setting up such. Due to their nature
        rogues struggle in honest social interactions and usually don't accept and respect
        authorities or laws.
         """

    rogue.draw_multi_line(text)


    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    while a == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.give_rect().collidepoint(pygame.mouse.get_pos()):
                    a = 1
                    pygame.display.quit()
                elif confirm.check_press(event):
                    rogue.delete()
                    confirm.delete()
                    zur.delete()
                    return(2)
                    a =1
                elif zur.check_press(event):
                    a = 1
                    rogue.delete()
                    confirm.delete()
                    zur.delete()
                    d = C.choose_class(screen, exit)
                    return(d)

def info_mage(screen,exit,zur):
    confirm = cr.TextBox(screen,(500,600),(150,50),50,'Confirm')
    confirm.draw_button()
    zur.draw_button()
    exit.draw_button()
    mage = cr.TextBox(screen,(50,50),(300,300),50,'Mage')
    mage.draw_button()
    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    while a == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.check_press(event):
                    a = 1
                    pygame.display.quit()
                elif confirm.check_press(event):
                    mage.delete()
                    confirm.delete()
                    zur.delete()
                    return(3)
                    a =1
                elif zur.check_press(event):
                    a = 1
                    mage.delete()
                    confirm.delete()
                    zur.delete()
                    d = C.choose_class(screen, exit)
                    return(d)

#    return (id)
