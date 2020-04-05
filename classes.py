import numpy as np

class CharacterClass:
    # Initializer / Instance Attributes
    def __init__(self, base_strength, base_intelligence, base_dexterity, base_vitality, base_luck, base_resilience, base_arcane_resistance, class_name):
        self.base_strength = base_strength
        self.base_intelligence = base_intelligence
        self.base_dexterity = base_dexterity
        self.base_vitality = base_vitality
        self.base_luck = base_luck
        self.base_resilience = base_resilience
        self.base_arcane_resistance = base_arcane_resistance
        self.class_name = class_name




class Fighter(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(
                                self,
                                base_strength = 40,
                                base_intelligence = 30,
                                base_dexterity = 35,
                                base_vitality = 40,
                                base_luck = 30,
                                base_resilience = 40,
                                base_arcane_resistance = 35,
                                class_name = 'Fighter'
                                )


class Mage(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(
                                self,
                                base_strength = 30,
                                base_intelligence = 50,
                                base_dexterity = 35,
                                base_vitality = 30,
                                base_luck = 30,
                                base_resilience = 30,
                                base_arcane_resistance = 45,
                                class_name = 'Mage'
                                )

class Rogue(CharacterClass):
    def __init__(self):
        CharacterClass.__init__(
                                self,
                                base_strength = 35,
                                base_intelligence = 35,
                                base_dexterity = 45,
                                base_vitality = 35,
                                base_luck = 35,
                                base_resilience = 30,
                                base_arcane_resistance = 35,
                                class_name = 'Rogue'
                                )


class PlayerCharacter(Fighter, Rogue, Mage):
    def __init__(self, player_class, skillpoint_allocation=None):
        player_class.__init__(self)
        self.hitpoints = 200 + 5*self.base_vitality
        self.dodge = self.base_dexterity/10 #maybe use logistic function
        self.base_initiative = self.base_dexterity/10
        #self.physical_armor = np.sum([gear.physical_armor for x in equipment_list])
        #self.physical_defense = self.physical_armor * (1+self.base_resilience/100)
        #self.magic_defense = self.magical_armor * (1+self.base_arcane_resistance/100)
        #self.physical_damage = self.weapon_damage * (1+self.base_strength/100)
        #self.magic_damage = self.weapon_damage * (1+self.base_intelligence/100)


    def update_attributes(): #gearchange, combat, etc.
        pass
    def update_other(): #maybe social standing, knowledge, etc. due to quests
        pass


jack = PlayerCharacter(Fighter)
print(jack.hitpoints)
