class Enemy:
    def __init__(self, vit, stre, dex, inte, lck, res, arc_res, weapondmg):
        self.vitality = vit
        self.strength = stre
        self.dexterity = dex
        self.intelligence = inte
        self.luck  = lck
        self.resilience = res
        self.arcane_resistance = arc_res
        self.starthealth = (100+self.vitality*5)
        self.currenthealth = self.starthealth
        self.weapondmg = weapondmg

    #def attributes(self):
      #print(self.vitality,self.starthealth)


    def losehealth(self, wert):
        self.currenthealth -= wert
        return(self.currenthealth)


    def gainhealth(self, wert):
        self.currenthealth += wert
        return (self.currenthealth)


    def dealdmg(self):
        dmg = self.weapondmg*(1+self.strength/100)
        return(dmg)


    def __del__(self):
        print('Gelöscht')
