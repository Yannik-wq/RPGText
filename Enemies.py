import random


class Enemy:
    def __init__(self, vit, stre, dex, inte, lck, res, arc_res, weapondmg, att1, a1_per, att2,a2_per,att3,a3_per, att4, a4_per):
        self.vitality  =  vit
        self.currentvit = vit
        self.strength  =  stre
        self.currentstr = stre
        self.dexterity  =  dex
        self.currentdex = dex
        self.evade = dex/10
        self.currentevade = dex/10
        self.intelligence  = inte
        self.currentint = inte
        self.luck  =  lck
        self.resilience  =  res
        self.currentres = res
        self.arcane_resistance  =  arc_res
        self.currentarc_res = arc_res
        self.starthealth  =  (100+self.vitality*5)
        self.currenthealth  =  self.starthealth
        self.weapondmg  =  weapondmg
        self.currentwpndmg = weapondmg
        self.att1  =  att1
        self.a1_per = a1_per
        self.att2  =  att2
        self.a2_per = a2_per
        self.att3  =  att3
        self.a3_per = a3_per
        self.att4  =  att4
        self.a4_per = a4_per

    #def attributes(self):
      #print(self.vitality,self.starthealth)

    def get_ini(self):
        return(self.dexterity/10)



    def losehealth(self, value):
        self.currenthealth -= value
        return(self.currenthealth)



    def gainhealth(self, wert):
        self.currenthealth += value
        return (self.currenthealth)



    def upd_str(self,value,type):
        if type == '+':
            self.currentstr += value
        else:
            self.currentstr -= value
        return(self.currentstr)



    def upd_dex(self,value,type):
        if type == '+':
            self.currentdex += value
        else:
            self.currentdex -= value
        return(self.currentdex)



    def upd_int(self,value,type):
        if type == '+':
            self.currentint += value
        else:
            self.currentint -= value
        return(self.currentint)



    def upd_evade(self,value,type):
        if type == '+':
            self.currentevade += value
        else:
            self.currentevade -= value
        return(self.currentevade)



    def choose_att(self):
        move = "none"
        while move == "none":
            rand = random.randint(1,100)
            if rand <= self.a1_per:
                move = self.att1
            elif rand > self.a1_per and rand <= self.a1_per + self.a2_per:
                move = self. att2
            elif rand > self.a1_per + self.a2_per and rand <= self.a1_per + self.a2_per + self.a3_per:
                move = self. att3
            elif rand > self.a1_per + self.a2_per + self.a3_per and rand <=self.a1_per + self.a2_per + self.a3_per + self.a4_per:
                move = self. att4
        return (move, self.currentwpndmg)




mutant_rat = Enemy(20,25,40,5,15,10,5,30, "bite", 80, "hit_run", 20, "none", 0, "none", 0 )
red_glowing_rat = Enemy(30,30,45,15,15,10,40, "bite", 70, "blind",30,"none",0,"none",0)
swarmofrats = Enemy(35,40,50,5,15,10,5,30, "fan out",30, "swarm_attack", 70,"none",0,"none",0 )
