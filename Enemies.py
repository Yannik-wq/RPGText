import numpy, math,classes, random


class Enemy:
    def __init__(self, vitality, strength, dexterity, intelligence, luck, resilience, arcane_resistance, weapondmg, att1, a1_per, att2,a2_per,att3,a3_per, att4, a4_per):

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


    def initiative(self):
        return(self.dexterity/10)


    def choose_att(self):
        attack_list = [self.att1, self.att2, self.att3,self.att4]

        return(numpy.random.choice(attack_list,size=None,replace=True, p=[self.a1_per,self.a2_per,self.a3_per,self.a4_per]))


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
                        att1 = 'Bite',
                        a1_per = 0.8,
                        att2 = 'RunAround',
                        a2_per = 0.2,
                        att3 = None,
                        a3_per = 0,
                        att4 = None,
                        a4_per = 0)

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
                        att1 = 'Bite',
                        a1_per = 0.7,
                        att2 = 'Blind',
                        a2_per = 0.3,
                        att3 = None,
                        a3_per = 0,
                        att4 = None,
                        a4_per = 0)


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
                        att1 = 'Bite',
                        a1_per = 0.7,
                        att2 = 'FanOut',
                        a2_per = 0.3,
                        att3 = None,
                        a3_per = 0,
                        att4 = None,
                        a4_per = 0
                        )

#mutant_rat =      Enemy(20,25,40,5,15,10,5,30, "bite", 0.8, "hit_run", 0.2, "none", 0, "none", 0)
#red_glowing_rat = Enemy(30,30,45,15,15,10,10,40, "bite", 70, "blind",30,"none",0,"none",0)
#swarmofrats =     Enemy(35,40,50,5,15,10,5,30, "fan out",30, "swarm_attack", 70,"none",0,"none",0)






class MonsterAttack:
    def __init__(self, enemy):
                                self.weapondmg = enemy.weapondmg
                                self.dmg_mult = 1
                                self.attribute = 0
                                self.buff = None
                                self.buffstr = 1
                                self.debuff = None
                                self.debuffstr = 1

    def set_mult(self,value):
        self.dmg_mult = value

    def atk_result(self):
        dmg = self.weapondmg*self.dmg_mult*(1+self.attribute/100)
        return(dmg, self.buff, self.buffstr, self.debuff, self.debuffstr)

    def __del__(self):
        pass






class Bite(MonsterAttack):
    def __init__(self, enemy):
        MonsterAttack.__init__(self,enemy)
        self.attribute = enemy.strength


class Blind(MonsterAttack):
    def __init__(self, enemy):
        MonsterAttack.__init__(self,enemy)
        self.debuff = 'blind'
        self.debuffstr = math.floor(2+enemy.intelligence/50)
        self.dmg_mult = 0

class RunAround(MonsterAttack):
    def __init__(self, enemy):
        MonsterAttack.__init__(self,enemy)
        self.dmg_mult = 0
        self.buffstr = math.floor(2+ enemy.dexterity/50)
        self.buff = 'hard_to_hit'







def fight(enemy):
    player = classes.jack
    fight = 1
    while fight==1:
        e_ini = enemy.initiative()
        p_ini = player.base_initiative
        while enemy.currenthealth > 0 and player.health >0:
            from numpy.random import choice
            if e_ini and p_ini == 0:
                break
            elif choice([enemy,player],1,[e_ini,p_ini]) == player:
                p_ini = 0
                pass#Do player Ataack, then do enemy atack
            else:
                e_ini = 0
                pass#Do Enemy attack then do player attack
        fight = 0
