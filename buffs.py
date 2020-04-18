

class Buff:
    def __init__(self, duration, strength, Character, is_active=False, b_or_d='buff'):
        self.duration = duration
        self.strength = strength

    def apply_effect(self):
        pass

    def reverse_effect(self):
        pass

    def look_if_apply(self):
        if self.b_or_d == 'debuff':
            if self.name not in Character.active_debuffs:
                Character.active_debuffs.update({self.name : self})
                self.apply_effect()
            elif self.strength > Character.active_debuffs.get(self.name).strength:
                Character.active_debuffs.get(self.name).reverse_effect()
                Character.active_debuffs.update({self.name : self})
                self.apply_effect()
            elif self.name not in Character.inactive_debuffs:
                Character.inactive_debuffs.update({self.name : [self]})
            else:
                d_list = Character.inactive_debuffs.get(self.name)
                d_list.append(self)
                d_list.sort(key=lambda x: x.strength, reverse=True)
                Character.inactive_debuffs.update({self.name : d_list})
        else:
            if self.name not in Character.active_buffs:
                Character.active_buffs.update({self.name : self})
                self.apply_effect()
            elif self.strength > Character.active_buffs.get(self.name).strength:
                Character.active_buffs.get(self.name).reverse_effect()
                Character.active_buffs.update({self.name : self})
                self.apply_effect()
            elif self.name not in Character.inactive_buffs:
                Character.inactive_buffs.update({self.name : [self]})
            else:
                b_list = Character.inactive_buffs.get(self.name)
                b_list.append(self)
                b_list.sort(key=lambda x: x.strength, reverse=True)
                Character.inactive_buffs.update({self.name : b_list})

    def check_inactive(self):
        if self.b_or_d == 'buff':
            if self.name in Character.inactive_buffs.keys():
                if Character.inactive_buffs.get(self.name) != []:
                    new_buff = Character.inactive_buffs.get(self.name).pop(0)
                    new_buff.apply_effect()
        else:
            if self.name in Character.inactive_debuffs.keys():
                if Character.inactive_debuffs.get(self.name) != []:
                    new_buff = Character.inactive_debuffs.get(self.name).pop(0)
                    new_buff.apply_effect()

    def remove_self(self):
        if self.b_or_d == 'buff':
            if self.is_active == True:
                Character.active_buffs.pop(self.name)
                self.check_inactive()
            else:
                b_list = Character.inactive_buffs.get(self.name)
                b_list.remove(self)
                Character.inactive_buffs.update({self.name : b_list})
        else:
            if self.is_active == True:
                Character.active_debuffs.pop(self.name)
                self.check_inactive()
            else:
                d_list = Character.inactive_debuffs.get(self.name)
                d_list.remove(self)
                Character.inactive_debuffs.update({self.name : d_list})

    def turn_goes_by(self):
        if self.duration > 0:
            self.duration -= 1
        else:
            remove_buff()


class Disarmed(Buff):
    def __init__(self, duration, strength, Character):
        Buff.__init__(self, duration, strength, Character)
        self.name = 'Disarmed'
        self.description = """ You deal reduced damage """
        self.b_or_d = 'debuff'

    def apply_effect(self):
        self.is_active = True
        Character.dmg_multiplier -= 0.5

    def reverse_effect(self):
        self.is_active = False
        Character.dmg_multiplier += 0.5




some_buff = Disarmed(5, 2, 4)
print(some_buff.duration)
another_buff = Disarmed(4, 3, 4)
buffs = {'Disarmed' : [some_buff, another_buff]}
buffs.pop('Disarmed')
print(buffs)
# print('Disarmed' in buffs)
# buffs = list(buffs.values())[0]
# buffs.sort(key=lambda x: x.strength, reverse=True)
# print(buffs)
