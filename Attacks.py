import pygame

class Attack:
    def __init__(self, weapondmg, attribute):
        self.weapondmg = weapondmg
        self.attribute = attribute
        self.dmg_mult = 1
        self.buff = 'None'
        #self.dmg = self.weapondmg*self.attribute*self.dmg_mult

    def set_mult(self,value):
        self.dmg_mult = value

    #def deal_dmg(self):
        #mult = self.dmg_mult
        #dmg = mult*wpn*(1+att/100)
    #    dmg= self.dmg_mult*self.weapondmg*(1+self.attribute/100)
    #    return(dmg)

    def atk_result(self):
        dmg = self.weapondmg*self.dmg_mult*(1+self.attribute/100)
        return(dmg, self.buff)

    def __del__(self):
        pass




class strike(Attack):
    def __init__(self,weapondmg,attribute):
        Attack.__init__(self,weapondmg, attribute)

    def __del__(self):
        pass

class overhead_strike(Attack):
    def __init__(self, weapondmg, attribute):
        Attack.__init__(self,weapondmg, attribute)
        self.dmg_mult = 1.3


    def __del__(self):
        pass

class disarm(Attack):
    def __init__(self, weapondmg, attribute):
        Attack.__init__(self,weapondmg, attribute)
        self.dmg_mult = 0.4
        self.buff = 'disarm'


    def __del__(self):
        pass
