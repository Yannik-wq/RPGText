

class Buff:
    def __init__(self, name, duration, strength, description, is_active=False):
        self.name = name
        self.duration = duration
        self.strength = strength
        self.description = description

    def check_inactive_buffs(self, Character):
        durations = []
        same_names = [buff for buff in Character.inactive_buffs if buff.name == self.name]
        for buff in Character.inactive_buffs:
            if self.name == buff.name:
                durations.append(buff.duration)
        if durations != []:
            max_duration = max(durations)
            indices = [index for index, duration in enumerate(durations) if duration == max_duration]
            if len(indices) == 1:
                pass

    def remove_buff(self, Character):
        if self.is_active == True:
            Character.active_buffs.remove(self.name)
            self.check_inactive_buffs(Character)
        else:
            Character.inactive_buffs.remove(self.name)

    def turn_goes_by(self):
        if self.duration > 0:
            self.duration -= 1
        else:
            remove_buff()


class Disarmed(Buff):
    def __init__(self, duration, strength):
        Buff.__init__(self, duration, strength)
        self.name = 'Disarmed'
        self.description = """ You deal reduced damage """
    def apply_disarmed(self, Character):
        if self.name not in Character.buff_list:
            Character.dmg_multiplier -= 0.5
            Character.active_buffs.append(self.name)
        else:
            pass
