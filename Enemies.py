import numpy


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

    def upd_stat(self, attribute, value):
        if attribute == dex:
            self.currentdex += value
        elif attribute == stre:
            self.currentstr += value
        elif attribute == inte:
            self.currentint += value
        elif attribute == res:
            self.currentres += value
        elif attribute == arc_res:
            self.currentarc_res += value
        elif attribute == hp:
            self.currenthealth += value
        elif attribute == wpndmg:
            self.currentwpndmg += value


#    def __getattribute__(self, name):
#        pass


    def initiative(self):
        return(self.dexterity/10)


    def choose_att(self):
        attack_list = [self.att1, self.att2, self.att3,self.att4]

        return(numpy.random.choice(attack_list,size=None,replace=True, p=[self.a1_per,self.a2_per,self.a3_per,self.a4_per]), self.currentwpndmg)



mutant_rat =      Enemy(20,25,40,5,15,10,5,30, "bite", 0.8, "hit_run", 0.2, "none", 0, "none", 0)
red_glowing_rat = Enemy(30,30,45,15,15,10,10,40, "bite", 70, "blind",30,"none",0,"none",0)
swarmofrats =     Enemy(35,40,50,5,15,10,5,30, "fan out",30, "swarm_attack", 70,"none",0,"none",0)






class MonsterAttack:
    def __init__(self, enemy):
        self.weapondmg = enemy.weapondmg
        self.dmg_mult = 1
        self.attribute = 0
        self.buff = None
    def set_mult(self,value):
        self.dmg_mult = value

    def atk_result(self):
        dmg = self.weapondmg*self.dmg_mult*(1+self.attribute/100)
        return(dmg, self.buff)

    def __del__(self):
        pass






class bite(MonsterAttack):
    def __init__(self, enemy):
        MonsterAttack.__init__(self,enemy)
        self.attribute = enemy.strength


A = bite(red_glowing_rat)

print(A.atk_result())




def fight(enemy):
    e_ini = enemy.initiative()
    #p_ini =PlayerClass.Player.get_ini()
    #en_ini = Enemies.enemy.get_ini()
    #pl_ini = classes.Player.get_ini()
    print(e_ini)

#fight(mutant_rat)
