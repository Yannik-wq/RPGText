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



def fight(opponent, player, screen, exit):
    enemy = E.OpponentActOne(opponent)
    player_health = player.hitpoints
    enemy_health = enemy.starthealth
    text1 = enemy.name + '     Health: ' +str(enemy_health)
    opp_button =  R.TextBox(screen,(600,100),(500,50),50,text1)
    text2 = player.class_name + '     Health:' + str(player_health)
    player_button = R.TextBox(screen,(100,500),(500,50),50,text2)
    enemy_stat_window = R.TextBox(screen,(200,200),(600,300),50,'Enemy Status Effects')
    enemy_status_field = R.TextBox(screen,(100,430),(100,50),20,'Debuffs')
    enemy_status_field.draw_button()
    player_button.draw_button()
    opp_button.draw_button()
    exit.draw_button()
    player.attack1 = Attacks.Strike(player.weapondmg,player.base_strength,enemy)
    player.attack2 = Attacks.OverheadStrike(player.weapondmg,player.base_strength,enemy)
    player.attack3 = Attacks.Disarm(player.weapondmg,player.base_strength,enemy)
    player.attack4 = Attacks.Strike(player.weapondmg,player.base_strength,enemy)
    attack1_button = R.TextBox(screen,(700,600),(100,30),30,player.attack1.name)
    attack2_button = R.TextBox(screen,(900,600),(100,30),30,player.attack2.name)       #
    attack3_button = R.TextBox(screen,(700,500),(100,30),30,player.attack3.name)
    attack4_button = R.TextBox(screen,(900,500),(100,30),30,player.attack4.name)

    attack1_button.draw_button()
    attack2_button.draw_button()
    attack3_button.draw_button()
    attack4_button.draw_button()
    debuff_open = 0
    while player_health >0 and enemy_health >0:
        a = 0
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
        while a == 0:
            for event in pygame.event.get():                                        #grabs all events from the event queue
                if event.type == pygame.MOUSEBUTTONDOWN:                            #Checks if these events are Mousebuttonpresses
                    if exit.check_press(event):              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                        pygame.display.quit()
                        sys.exit(0)
                    elif attack1_button.check_press(event):
                        a = 1
                        attack = player.attack1
                    elif attack2_button.check_press(event):
                        a = 2
                        attack = player.attack2
                    elif attack3_button.check_press(event):
                        a = 3
                        attack = player.attack3
                    elif attack4_button.check_press(event):
                        a = 4
                        attack = player.attack4
                    elif enemy_status_field.check_press(event):
                        a = 0
                        if debuff_open == 0:
                            enemy_stat_window.draw_button()
                            status_text = '            '
                            for x in enemy.active_debuffs:
                                status = enemy.active_debuffs.get(x)
                                status_text =(
                                """


These are all the negative afflicions currently active on the enemy
"""
+status_text + x + """:""" + status.description)

                                enemy_stat_window.draw_multi_line(status_text)

                            debuff_open = 1
                        else:
                            enemy_stat_window.delete()
                            debuff_open = 0
                    else:
                        a = 0


        e_ini = enemy.initiative()/(enemy.initiative()+player.base_initiative)
        p_ini = player.base_initiative/(player.base_initiative+enemy.initiative())
        enemy_status_field = R.TextBox(screen,(100,430),(100,50),20,'Debuffs')
        enemy_status_field.draw_button()
                    #for x in enemy.active_debuffs:


        c = 2
        while player_health >0 and enemy_health >0 and c != 0:


            d = numpy.random.choice((player, enemy),size=None,replace=False, p=[p_ini, e_ini])
            if d == player:
                c -= 1
                p_ini = 0
                e_ini = 1
                enemy_health -= attack.atk_result()
                text1 = enemy.name + '     Health: ' +str(enemy_health)
                opp_button =  R.TextBox(screen,(600,100),(500,50),50,text1)
                opp_button.draw_button()
            else:
                c-= 1
                e_ini = 0
                p_ini = 1
                dmg, buff = enemy.choose_att()
                if buff != None:
                    pass
                player_health -= dmg
                text2 = player.class_name + '     Health:' + str(player_health)
                player_button = R.TextBox(screen,(100,500),(500,50),50,text2)
                player_button.draw_button()

        for x in enemy.every_buff_or_debuff:
                        #print(x.name, x.duration)
            x.turn_goes_by()
                        #print(x.name, x.duration)
                        #print (enemy.active_debuffs)



#player = c.PlayerCharacter(c.Fighter)

#fight(E.MutantRat, player)
