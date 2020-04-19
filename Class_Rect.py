import pygame,ptext


#erstellt ein Rechteck auf dem Display 'screen' linke obere Ecke hat die Positon pos x/y Wert.
#Dimension ist die größe des Rechtecks
class Rectangle:
    def __init__(self, screen, pos, dimension):
        self.position = pos
        self.dimension = dimension
        self.screen = screen
        self.rect = pygame.Rect(self.position, self.dimension)

#returnt die Position und maße des Rechtecks
    def give_rect(self):
        return(self.rect)

#zeichnet das Rechteck auf den Hintergrund mit der Farbe draw_color und
#updatet den Bildschrim an der Position des Rechtecks
    def draw(self):
        draw_color = pygame.Color('orange')
        pygame.draw.rect(self.screen, draw_color, self.rect)
        pygame.display.update(self.rect)

#Löscht das Rechteckt und füllt es mit der Farbe delcolor aus und updatet screen
    def delete(self):
        delcolor = pygame.Color(0,0,0,255)
        pygame.draw.rect(self.screen, delcolor, self.rect)
        pygame.display.update(self.rect)
        return(self.rect)


#Erstellt ein Rechteck mit einzeiligem Text, mit der Schriftgröße fontsize und Farbe fontcolor
class TextBox(Rectangle):
    def __init__(self, screen, pos, dimension,fontsize,text):
        Rectangle.__init__(self, screen, pos, dimension)
        self.fontsize = fontsize
        self.fontcolor = pygame.Color('darkred')
        self.text = text

#zeichnet das Textfeld und updatet an der Positon
    def draw_button(self):
        Rectangle.draw(self)
        f = pygame.font.Font(None, self.fontsize)
        caption = f.render(self.text, True, self.fontcolor)
        self.screen.blit(caption, self.rect, area=None, special_flags=0)
        pygame.display.update(self.rect)
        return(self.rect)


#Erstellt ein Textfeld mit multiline text
# Text muss im Format """ text """ sein

    def draw_multi_line(self,text):
        ptext.draw(text,self.position )
        pygame.display.flip()


#überprüft ob der Button gedrückt wird



    def check_press(self,event):
        #pygame.event.get()
        #if event.type == pygame.MOUSEBUTTONDOWN:
        return(Rectangle.give_rect(self).collidepoint(pygame.mouse.get_pos()))





def check_button_press(button_list):
    a = 0
    while a == 0:
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)                            #Only mousebutton presses are filled into the event queue, everything else is droped.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in button_list:                                      #grabs all events from the event queue
                    if button.check_press(event):              #Checks wether position of the mouse when clicked is within the 'Firstrect' rectangle
                        a = 1
                        return(button)



#class Dialogue(TextBox):
#    def
