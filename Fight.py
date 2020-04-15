import sys
import pygame
import ptext
import numpy
import Enemies
import Attacks
import classes
import Class_Rect

R = Class_Rect
c = classes
E = Enemies
A = Attacks



def fight(enemy, player, screen, exit):
    en = E.OpponentActOne(enemy)
    player_health = player.hitpoints
    enemy_health = en.starthealth
    text1 = en.name + '     Health: ' +str(enemy_health)
    opp =  R.TextBox(screen,(600,100),(500,50),50,text1)
    text2 = player.class_name + '     Health:' + str(player_health)
    play = R.TextBox(screen,(100,500),(500,50),50,text2)
    play.draw_button()
    opp.draw_button()
    exit.draw_button()
    a1 = A.Strike(player.weapondmg, player.base_strength)
    attack1 = R.TextBox(screen,(700,600),(100,30),30,a1.name)
    a2 =A.OverheadStrike(player.weapondmg,player.base_strength)
    attack2 = R.TextBox(screen,(900,600),(100,30),30,a2.name)
    a3 = A.Disarm(player.weapondmg,player.base_dexterity)
    attack3 = R.TextBox(screen,(700,500),(100,30),30,a3.name)
    a4 = A.Strike(player.weapondmg, player.base_strength)
    attack4 = R.TextBox(screen,(900,500),(100,30),30,a4.name)
    attack1.draw_button()
    attack2.draw_button()
    attack3.draw_button()
    attack4.draw_button()

    while player_health >0 and enemy_health >0:
        a = 0
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
        while a == 0:
            for event in pygame.event.get():                                        #grabs all events from the event queue
                if event.type == pygame.MOUSEBUTTONDOWN:                            #Checks if these events are Mousebuttonpresses
                    if exit.check_press(event):              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                        pygame.display.quit()
                        sys.exit(0)
                    elif attack1.check_press(event):
                        a = 1
                        attack = a1
                    elif attack2.check_press(event):
                        a = 2
                        attack = a2
                    elif attack3.check_press(event):
                        a = 3
                        attack = a3
                    elif attack4.check_press(event):
                        a = 4
                        attack = a4

                    e_ini = en.initiative()/(en.initiative()+player.base_initiative)
                    p_ini = player.base_initiative/(player.base_initiative+en.initiative())
                    c = 2

                    while player_health >0 and enemy_health >0 and c != 0:
                        d = numpy.random.choice((player, enemy),size=None,replace=False, p=[p_ini, e_ini])
                        if d == player:
                            c -= 1
                            p_ini = 0
                            e_ini = 1
                            enemy_health -= attack.atk_result()
                            text1 = en.name + '     Health: ' +str(enemy_health)
                            opp =  R.TextBox(screen,(600,100),(500,50),50,text1)
                            opp.draw_button()
                        else:
                            c-= 1
                            e_ini = 0
                            p_ini = 1
                            dmg = en.choose_att()
                            player_health -= dmg
                            text2 = player.class_name + '     Health:' + str(player_health)
                            play = R.TextBox(screen,(100,500),(500,50),50,text2)
                            play.draw_button()



#player = c.PlayerCharacter(c.Fighter)

#fight(E.MutantRat, player)
