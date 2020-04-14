import pygame
import sys
import ptext
import OpenStartScreen
import Start_Game
import classes
import Class_Rect

r = Class_Rect
c = classes
sg = Start_Game
os = OpenStartScreen

pygame.init()
pygame.display.init()
pygame.display.set_caption('Rats Everywhere')
pygame.font.init()
screen = pygame.display.set_mode(size = (1300,800))
exit =  r.TextBox(screen,(100,600),(100,50),50,'Exit')



id = os.open_start_screen(screen, exit);

if id == 1:
    player = c.PlayerCharacter(c.Fighter)
elif id == 2:
    player = c.PlayerCharacter(c.Rogue)
elif id == 3:
    player = c.PlayerCharacter(c.Mage)

sg.start_game(player,screen, exit)
