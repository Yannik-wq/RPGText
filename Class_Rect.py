import pygame

class Rectangle:
    def __init__(self, screen, pos, dimension):
        self.position = pos
        self.dimension = dimension
        self.screen = screen
        self.rect = pygame.Rect(self.position, self.dimension)

    def give_rect(self):
        return(self.rect)

    def draw(self):
        draw_color = pygame.Color(150, 50, 100, 255)
        pygame.draw.rect(self.screen, draw_color, self.rect)
        pygame.display.update(self.rect)

    def delete(self):
        delcolor = pygame.Color(0,0,0,255)
        pygame.draw.rect(self.screen, delcolor, self.rect)
        pygame.display.update(self.rect)
        return(self.rect)

class TextBox(Rectangle):
    def __init__(self, screen, pos, dimension,fontsize,text):
        Rectangle.__init__(self, screen, pos, dimension)
        self.fontsize = 50
        self.fontcolor = pygame.Color(0,0,0,255)
        self.text = text

    def draw_button(self):
        Rectangle.draw(self)
        f = pygame.font.Font(None, self.fontsize)
        caption = f.render(self.text, True, (255,255,100))
        self.screen.blit(caption, self.rect, area=None, special_flags=0)
        pygame.display.update(self.rect)
        return(self.rect)
