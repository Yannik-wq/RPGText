

class CharacterClass:
    # Initializer / Instance Attributes
    def __init__(self, base_strength, base_intelligence, base_dexterity, base_vitality, base_luck, base_resilience, base_arcane_resistance):
        self.base_strength = base_strength
        self.base_intelligence = base_intelligence
        self.base_dexterity = base_dexterity
        self.base_vitality = base_vitality
        self.base_luck = base_luck
        self.base_resilience = base_resilience
        self.base_arcane_resistance = base_arcane_resistance


fighter = CharacterClass(
    base_strength = 40,
    base_intelligence = 30,
    base_dexterity = 35,
    base_vitality = 40,
    base_luck = 30,
    base_resilience = 40,
    base_arcane_resistance = 35
                        )

mage = CharacterClass(
    base_strength = 30,
    base_intelligence = 50,
    base_dexterity = 35,
    base_vitality = 30,
    base_luck = 30,
    base_resilience = 30,
    base_arcane_resistance = 45
                        )

rogue = CharacterClass(
    base_strength = 35,
    base_intelligence = 35,
    base_dexterity = 45,
    base_vitality = 35,
    base_luck = 35,
    base_resilience = 30,
    base_arcane_resistance = 35
                        )

print(rogue.base_luck)
