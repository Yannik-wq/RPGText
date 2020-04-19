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
        self.weapondmg = 15
        #self.physical_armor = np.sum([gear.physical_armor for x in equipment_list])
        #self.physical_defense = self.physical_armor * (1+self.base_resilience/100)
        #self.magic_defense = self.magical_armor * (1+self.base_arcane_resistance/100)
        #self.physical_damage = self.weapon_damage * (1+self.base_strength/100)
        #self.magic_damage = self.weapon_damage * (1+self.base_intelligence/100)


    def update_attributes(): #gearchange, combat, etc.
        pass
    def update_other(): #maybe social standing, knowledge, etc. due to quests
        pass


class Background:
    def __init__(self):
        self.martial_arts = 5
        self.monster_lore = 5
        self.nature = 5
        self.magical_creatures = 5
        self.persuasion =5
        self.demonology = 5
        self.deception = 5
        self.intimidation = 5
        self.disciplin = 5
        self.arcane_knowledge = 5
        self.history = 5
        self.races_n_cultures = 5
        self.craftsmanship = 5
        self.acrobatics = 5
        self.ettiquette = 5
        self.social_standing = 0
        self.languages = 5
        self.music_n_art = 5
        self.religion = 5
        self.reflexes = 5
        self.construction = 5
        self.engineering = 5
        self.perception = 5
        self.riding = 5
        self.medicin = 5
        self.ritualism = 5


    def talent_check(self, Character, check):
        value = getattr(Character, check)
        return(np.random.choice(('Success', 'Failure'),size=None,replace=True, p=[value/100, (100-value)/100]))


class Knight(Background):
    def __init__ (self):
        Background.__init__(self)
        self.riding += 5

Player = Knight()
print(Player.riding)
print(Player.talent_check(Player,'riding'))

#jack = PlayerCharacter(Fighter)
#print(jack.hitpoints)
