import Enemies

class Buff:
    def __init__(self, duration, strength, Character, b_or_d='buff'):
        self.duration = duration
        self.strength = strength
        self.applied_on = Character
        self.is_active = False
        Character.every_buff_or_debuff.append(self)

    def apply_effect(self):
        pass

    def reverse_effect(self):
        pass

    def look_if_apply(self):
        if self.b_or_d == 'debuff':
            if self.name not in self.applied_on.active_debuffs:
                self.applied_on.active_debuffs.update({self.name : self})
                self.apply_effect()
            elif self.strength > self.applied_on.active_debuffs.get(self.name).strength:
                self.applied_on.active_debuffs.get(self.name).reverse_effect()
                self.applied_on.active_debuffs.update({self.name : self})
                self.apply_effect()
            elif self.name not in self.applied_on.inactive_debuffs:
                self.applied_on.inactive_debuffs.update({self.name : [self]})
            else:
                d_list = self.applied_on.inactive_debuffs.get(self.name)
                d_list.append(self)
                d_list.sort(key=lambda x: x.strength, reverse=True)
                self.applied_on.inactive_debuffs.update({self.name : d_list})
        else:
            if self.name not in self.applied_on.active_buffs:
                self.applied_on.active_buffs.update({self.name : self})
                self.apply_effect()
            elif self.strength > self.applied_on.active_buffs.get(self.name).strength:
                self.applied_on.active_buffs.get(self.name).reverse_effect()
                self.applied_on.active_buffs.update({self.name : self})
                self.apply_effect()
            elif self.name not in self.applied_on.inactive_buffs:
                self.applied_on.inactive_buffs.update({self.name : [self]})
            else:
                b_list = self.applied_on.inactive_buffs.get(self.name)
                b_list.append(self)
                b_list.sort(key=lambda x: x.strength, reverse=True)
                self.applied_on.inactive_buffs.update({self.name : b_list})

    def check_inactive(self):
        if self.b_or_d == 'buff':
            if self.name in self.applied_on.inactive_buffs.keys():
                if self.applied_on.inactive_buffs.get(self.name) != []:
                    new_buff = self.applied_on.inactive_buffs.get(self.name).pop(0)
                    new_buff.apply_effect()
        else:
            if self.name in self.applied_on.inactive_debuffs.keys():
                if self.applied_on.inactive_debuffs.get(self.name) != []:
                    new_buff = self.applied_on.inactive_debuffs.get(self.name).pop(0)
                    new_buff.apply_effect()

    def remove_self(self):
        if self.b_or_d == 'buff':
            if self.is_active == True:
                self.applied_on.active_buffs.pop(self.name)
                self.check_inactive()
                self.reverse_effect()
            else:
                b_list = self.applied_on.inactive_buffs.get(self.name)
                b_list.remove(self)
                self.applied_on.inactive_buffs.update({self.name : b_list})
        else:
            if self.is_active == True:
                self.applied_on.active_debuffs.pop(self.name)
                self.check_inactive()
                self.reverse_effect()
            else:
                d_list = self.applied_on.inactive_debuffs.get(self.name)
                d_list.remove(self)
                self.applied_on.inactive_debuffs.update({self.name : d_list})
        self.applied_on.every_buff_or_debuff.remove(self)

    def turn_goes_by(self):
        if self.duration > 0:
            self.duration -= 1
        else:
            self.remove_self()


class Disarmed(Buff):
    def __init__(self, duration, strength, Character):
        Buff.__init__(self, duration, strength, Character)
        self.name = 'Disarmed'
        self.description = """ Character deals reduced damage """
        self.b_or_d = 'debuff'


    def apply_effect(self):
        self.is_active = True
        self.applied_on.weapondmg = (0.5*self.applied_on.weapondmg)

    def reverse_effect(self):
        self.is_active = False
        self.applied_on.weapondmg = (2*self.applied_on.weapondmg)



#enemy = Enemies.OpponentActOne(Enemies.RedGlowingRat)
#print(enemy.weapondmg)
#some_buff = Disarmed(5, 2, enemy)
#print(some_buff.description)
#some_buff.apply_effect()
#print(enemy.weapondmg)
