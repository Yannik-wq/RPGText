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
    text1 = enemy.name + '     Health: ' +str(round(enemy_health,0))
    opp_button =  R.TextBox(screen,(600,100),(600,50),50,text1)
    opp_button.draw_button()
    text2 = player.class_name + '     Health:' + str(round(player_health,0))
    player_button = R.TextBox(screen,(100,500),(450,50),50,text2)
    player_button.draw_button()
    enemy_debuff_count = 0
    enemy_buff_count = 0
    player_buff_count = 0
    player_debuff_count = 0
    enemy_debuff_window = R.TextBox(screen,(200,200),(700,300),50,'')
    enemy_debuff_field = R.TextBox(screen,(900,160),(70,30),20,('Debuffs('+str(enemy_debuff_count)+')'))
    enemy_debuff_field.draw_button()
    enemy_buff_window = R.TextBox(screen,(200,200),(700,300),50,'')
    enemy_buff_field = R.TextBox(screen,(1000,160),(70,30),20,('Buffs('+str(enemy_buff_count)+')'))
    enemy_buff_field.draw_button()
    player_debuff_window = R.TextBox(screen,(200,200),(700,300),50,'')
    player_debuff_field = R.TextBox(screen,(100,560),(70,30),20,('Debuffs('+str(player_debuff_count)+')'))
    player_debuff_field.draw_button()
    player_buff_window = R.TextBox(screen,(200,200),(700,300),50,'')
    player_buff_field = R.TextBox(screen,(200,560),(70,30),20,('Buffs('+str(player_buff_count)+')'))
    player_buff_field.draw_button()
    enemy_debuff_rect = enemy_debuff_field.give_rect()
    exit.draw_button()
    player.attack1 = Attacks.Strike(player.weapondmg,player.base_strength,enemy)
    player.attack2 = Attacks.OverheadStrike(player.weapondmg,player.base_strength,enemy)
    player.attack3 = Attacks.Disarm(player.weapondmg,player.base_strength,enemy)
    player.attack4 = Attacks.Strike(player.weapondmg,player.base_strength,enemy)
    attack1_button = R.TextBox(screen,(700,600),(150,30),25,player.attack1.name)
    attack2_button = R.TextBox(screen,(900,600),(150,30),25,player.attack2.name)       #
    attack3_button = R.TextBox(screen,(700,500),(150,30),25,player.attack3.name)
    attack4_button = R.TextBox(screen,(900,500),(150,30),25,player.attack4.name)
    attack1_button.draw_button()
    attack2_button.draw_button()
    attack3_button.draw_button()
    attack4_button.draw_button()
    while player_health >0 and enemy_health >0:
        a = 0

        enemy_debuff_count = 0
        enemy_buff_count = 0
        player_buff_count = 0
        player_debuff_count = 0

        enemy_debuff_info = """
        Currently active negative status effects on your enemy
        """
        for x in enemy.active_debuffs:
            enemy_debuff_count +=1
            enemy_debuff = enemy.active_debuffs.get(x)
            enemy_debuff_info =(enemy_debuff_info
            + x + """:""" + enemy_debuff.description)
        enemy_debuff_field = R.TextBox(screen,(900,160),(70,30),20,('Debuffs('+str(enemy_debuff_count)+')'))
        enemy_debuff_field.draw_button()

        enemy_buff_info = """
        Currently active positive status effects on your enemy
        """
        for x in enemy.active_buffs:
            enemy_buff_count +=1
            enemy_debuff = enemy.active_buffs.get(x)
            enemy_buff_info =(enemy_buff_info
            + x + """:""" + enemy_buff.description)
        enemy_buff_field = R.TextBox(screen,(1000,160),(70,30),20,('Buffs('+str(enemy_buff_count)+')'))
        enemy_buff_field.draw_button()

        player_debuff_info = """
        Currently active negative status effects on you
        """
        for x in player.active_debuffs:
            player_debuff_count +=1
            player_debuff = player.active_debuffs.get(x)
            player_debuff_info =(player_debuff_info
            + x + """:""" + player_debuff.description)
        player_debuff_field = R.TextBox(screen,(100,560),(70,30),20,('Debuffs('+str(player_debuff_count)+')'))
        player_debuff_field.draw_button()

        player_buff_info = """
        Currently active positive status effects on you"""
        for x in player.active_buffs:
            player_buff_count +=1
            player_buff = player.active_buffs.get(x)
            player_buff_info =(player_buff_info
            + x + """:""" + player_buff.description)
        player_buff_field = R.TextBox(screen,(200,560),(70,30),20,('Buffs('+str(player_buff_count)+')'))
        player_buff_field.draw_button()

        enemy_debuff_open = 0
        enemy_buff_open = 0
        player_debuff_open = 0
        player_buff_open = 0


        while a == 0:
            x = pygame.mouse.get_pos()
            if enemy_debuff_field.give_rect().collidepoint(x):
                if enemy_debuff_open == 0 and enemy_debuff_count !=0:
                    enemy_debuff_open = 1
                    enemy_buff_open = 0
                    player_debuff_open = 0
                    player_buff_open = 0
                    enemy_debuff_window.draw_button()
                    enemy_debuff_window.draw_multi_line(enemy_debuff_info)
            elif enemy_buff_field.give_rect().collidepoint(x):
                if enemy_buff_open == 0 and enemy_buff_count !=0:
                    enemy_buff_open = 1
                    enemy_debuff_open = 0
                    player_debuff_open = 0
                    player_buff_open = 0
                    enemy_buff_window.draw_button()
                    enemy_buff_window.draw_multi_line(enemy_buff_info)
            elif player_buff_field.give_rect().collidepoint(x) :
                if player_buff_open == 0 and player_buff_count !=0:
                    player_buff_open = 1
                    enemy_debuff_open = 0
                    enemy_buff_open = 0
                    player_debuff_open = 0
                    player_buff_window.draw_button()
                    player_buff_window.draw_multi_line(player_buff_info)
            elif player_debuff_field.give_rect().collidepoint(x):
                if player_debuff_open == 0 and player_debuff_count !=0:
                    player_debuff_open = 1
                    enemy_debuff_open = 0
                    enemy_buff_open = 0
                    player_buff_open = 0
                    player_debuff_window.draw_button()
                    player_debuff_window.draw_multi_line(player_debuff_info)
            else:
                if player_buff_open ==1:
                    player_buff_window.delete()
                    player_buff_open = 0
                elif player_debuff_info ==1:
                    player_debuff_window.delete()
                    player_debuff_open = 0
                elif enemy_buff_open ==1:
                    enemy_buff_open = 0
                    enemy_buff_window.delete()
                elif enemy_debuff_open == 1:
                    enemy_debuff_open = 0
                    enemy_buff_window.delete()
                else:
                    pass

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
                    else:
                        a = 0
                pygame.event.clear()

        e_ini = enemy.initiative()/(enemy.initiative()+player.base_initiative)
        p_ini = player.base_initiative/(player.base_initiative+enemy.initiative())
        c = 2
        while player_health >0 and enemy_health >0 and c != 0:
            d = numpy.random.choice((player, enemy),size=None,replace=False, p=[p_ini, e_ini])
            if d == player:
                c -= 1
                p_ini = 0
                e_ini = 1
                enemy_health -= attack.atk_result()
                text1 = enemy.name + '     Health: ' +str(round(enemy_health,0))
                opp_button =  R.TextBox(screen,(600,100),(600,50),50,text1)
                opp_button.draw_button()
            else:
                c-= 1
                e_ini = 0
                p_ini = 1
                dmg, buff = enemy.choose_att()
                if buff != None:
                    pass
                player_health -= dmg
                text2 = player.class_name + '     Health:' + str(round(player_health,0))
                player_button = R.TextBox(screen,(100,500),(450,50),50,text2)
                player_button.draw_button()

        for x in enemy.every_buff_or_debuff:
            x.turn_goes_by()




#player = c.PlayerCharacter(c.Fighter)

#fight(E.MutantRat, player)
