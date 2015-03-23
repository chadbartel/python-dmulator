__author__ = 'Chaddle'


class Master(object):

    def __init__(self, name):
        self.name = str(name).strip()
        self.master_dict = {}

    def generate_child(self):
        pass

    def attack(self, other):
        import random
        if random.randint(1, 20) >= other.dict['armorClass']:
            damage = self.master_dict['attack']
            return damage
        else:
            pass

    # This method doesn't seem to work
    def saving_throw(self, save_type):
        import random
        try:
            if str(save_type).capitalize() == 'Fort':
                save = random.randint(1, 20) + int(self.master_dict['saves']['Fort'])
                return save
            elif str(save_type).capitalize() == 'Ref':
                save = random.randint(1, 20) + int(self.master_dict['saves']['Ref'])
                return save
            elif str(save_type).capitalize() == 'Will':
                save = random.randint(1, 20) + int(self.master_dict['saves']['Will'])
                return save
        except LookupError as e:
            print(e)

    def skill_check(self, skill_name):
        pass
