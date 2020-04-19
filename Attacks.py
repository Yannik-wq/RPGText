import pygame, Enemies

class Attack:
    def __init__(self, weapondmg, attribute):
        self.weapondmg = 10
        self.attribute = attribute
        self.dmg_mult = 1
        self.buff = 'None'
        #self.dmg = self.weapondmg*self.attribute*self.dmg_mult

    def set_mult(self,value):
        self.dmg_mult = value

    def atk_result(self):
        dmg = self.weapondmg*self.dmg_mult*(1+self.attribute/100)
        return(dmg)

    def __del__(self):
        pass




class Strike(Attack):
    def __init__(self,weapondmg,attribute):
        Attack.__init__(self,weapondmg, attribute)
        self.name = "Strike"

    def __del__(self):
        pass

class OverheadStrike(Attack):
    def __init__(self, weapondmg, attribute):
        Attack.__init__(self,weapondmg, attribute)
        self.dmg_mult = 1.3
        self.buff = "exposed"
        self.name = "Overhead Strike"
    def __del__(self):
        pass

class Disarm(Attack):
    def __init__(self, weapondmg, attribute):
        Attack.__init__(self,weapondmg, attribute)
        self.dmg_mult = 0.4
        self.buff = 'disarm'
        self.name = "Disarm"

    def __del__(self):
        pass
