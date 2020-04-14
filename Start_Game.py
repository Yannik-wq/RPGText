import pygame
import sys
import ptext
import Class_Rect
import classes
import Fight
import Enemies
#import TextRPG
f = Fight


CT = Class_Rect.TextBox
#
def start_game(player,screen,exit):
    #player = TextRPG.player
    text = 'You chose to play as a ' + player.class_name
    type = CT(screen,(200,200),(500,300),50,text)
    stats = CT(screen,(200,200),(400,400),50,'')
    go = CT(screen,(300,600),(300,50),50,'Start Adventure')
    type.draw_button()
    exit.draw_button()
    go.draw_button()
    text =("""


        Your starting stats are:

        Health = """ + str(player.hitpoints) +
        """
        Strength = """ + str(player.base_strength)+
        """
        Dexterity = """ + str(player.base_dexterity)+
        """
        Intelligence = """ + str(player.base_intelligence)+
        """
        Luck = """ + str(player.base_luck)+
        """
        Resilience = """ + str(player.base_resilience)+
        """
        Arcane Resistance = """ + str(player.base_arcane_resistance)+
        """
        Dodge = """ + str(player.dodge)+
        """
        Initiative = """ + str(player.base_initiative)
        )

    stats.draw_multi_line(text)
    a = 0
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    while a == 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.check_press(event):
                    a = 1
                    pygame.display.quit()
                elif go.check_press(event):
                    go.delete()
                    stats.delete()
                    type.delete()

                    f.fight(Enemies.RedGlowingRat,player, screen, exit)
