import numpy, math,classes, random

random.seed()

class Enemy:
    def __init__(self, vitality, strength, dexterity, intelligence, luck, resilience, arcane_resistance, weapondmg,name):

                            self.vitality  =  vitality
                            self.currentvitality = vitality
                            self.strength  =  strength
                            self.currentstrength = strength
                            self.dexterity  =  dexterity
                            self.currentdexterity = dexterity
                            self.evade = dexterity/10
                            self.currentevade = dexterity/10
                            self.intelligence  = intelligence
                            self.currentintelligence = intelligence
                            self.luck  =  luck
                            self.resilience  =  resilience
                            self.currentresilience = resilience
                            self.arcane_resistance  =  arcane_resistance
                            self.currentarcane_resistance = arcane_resistance
                            self.starthealth  =  (100+self.vitality*5)
                            self.currenthealth  =  self.starthealth
                            self.weapondmg  =  weapondmg
                            self.currentwpndmg = weapondmg
                            self.name = name
    #def attributes(self):

      #print(self.vitality,self.starthealth)

    def upd_stat(self, attribute, value):
        if attribute == dexterity:
            self.currentdexterity += value
        elif attribute == strength:
            self.currentstr += value
        elif attribute == intelligence:
            self.currentint += value
        elif attribute == resilience:
            self.currentres += value
        elif attribute == arcane_resistance:
            self.currentarcane_resistance += value
        elif attribute == hp:
            self.currenthealth += value
        elif attribute == wpndmg:
            self.currentwpndmg += value


#    def __getattribute__(self, name):
#        pass




class MutantRat(Enemy):
    def __init__(self):
        Enemy.__init__(self,
                        vitality =20,
                        strength = 25,
                        dexterity = 40,
                        intelligence =5,
                        luck = 15,
                        resilience = 10,
                        arcane_resistance = 5,
                        weapondmg = 30,
                        name = 'Mutant rat')
        att1 = Bite(self),
        a1_per = 0.8,
        att2 = 'RunAround',
        a2_per = 0.2,
        att3 = None,
        a3_per = 0,
        att4 = None,
        a4_per = 0,



class RedGlowingRat(Enemy):
    def __init__(self):
        Enemy.__init__(self,
                        vitality =30,
                        strength = 30,
                        dexterity = 45,
                        intelligence =15,
                        luck = 15,
                        resilience = 10,
                        arcane_resistance = 10,
                        weapondmg = 40,
                        name ='Red glowing rat'
                        )
        self.att1 = Bite(self),
        self.a1_per = 70,
        self.att2 = Blind(self),
        self.a2_per = 30,
        self.att3 = None,
        self.a3_per = 0,
        self.att4 = None,
        self.a4_per = 0,



class SwarmOfRats(Enemy):
    def __init__(self):
        Enemy.__init__(
                        self,
                        vitality =35,
                        strength = 40,
                        dexterity = 50,
                        intelligence =5,
                        luck = 15,
                        resilience = 10,
                        arcane_resistance = 5,
                        weapondmg = 30,
                        name = 'Swarm of rats')
        self.att1 = Bite(self),
        a1_per = 0.7,
        att2 = 'FanOut',
        a2_per = 0.3,
        att3 = None,
        a3_per = 0,
        att4 = None,
        a4_per = 0,



class OpponentActOne(MutantRat, SwarmOfRats, RedGlowingRat):
    def __init__(self, enemy):
        enemy.__init__(self)


    def initiative(self):
        return(self.dexterity/10)


    def choose_att(self):
        a = random.randint(1,100)
        if a <= self.a1_per[0]:
            d = self.att1[0].atk_result(self)
            return(d)
        elif a > self.a1_per[0] and a <= (self.a2_per[0]+ self.a1_per[0]):
            d = self.att2[0].atk_result(self)
            return(d)

        #attack_list = [self.att1, self.att2, self.att3,self.att4]

        #return(numpy.random.choice(attack_list,size=None,replace=True, p=[self.a1_per,self.a2_per,self.a3_per,self.a4_per]))

#mutant_rat =      Enemy(20,25,40,5,15,10,5,30, "bite", 0.8, "hit_run", 0.2, "none", 0, "none", 0)
#red_glowing_rat = Enemy(30,30,45,15,15,10,10,40, "bite", 70, "blind",30,"none",0,"none",0)
#swarmofrats =     Enemy(35,40,50,5,15,10,5,30, "fan out",30, "swarm_attack", 70,"none",0,"none",0)






class MonsterAttack:
    def __init__(self, enemy):
                                #self.weapondmg = enemy.weapondmg
                                self.dmg_mult = 1
                                self.attribute = 0
                                self.buff = None
                                self.buffstr = 1
                                self.debuff = None
                                self.debuffstr = 1

    def set_mult(self,value):
        self.dmg_mult = value

    def atk_result(self, enemy):
        dmg = enemy.weapondmg*self.dmg_mult*(1+self.attribute/100)
        return (dmg)#, self.buff, self.buffstr, self.debuff, self.debuffstr;

    def __del__(self):
        pass






class Bite(MonsterAttack):
    def __init__(self, enemy):
        MonsterAttack.__init__(self,enemy)
        self.attribute = enemy.strength
        self.name = 'Bite'

class Blind(MonsterAttack):
    def __init__(self, enemy):
        MonsterAttack.__init__(self,enemy)
        self.debuff = 'blind'
        self.debuffstr = math.floor(2+enemy.intelligence/50)
        self.dmg_mult = 0
        self.name = 'Blind'
class RunAround(MonsterAttack):
    def __init__(self, enemy):
        MonsterAttack.__init__(self,enemy)
        self.dmg_mult = 0
        self.buffstr = math.floor(2+ enemy.dexterity/50)
        self.buff = 'hard_to_hit'
        self.name = 'Hard to hit'






#b = OpponentActOne(RedGlowingRat)
#d = b.choose_att()

#print(d)
