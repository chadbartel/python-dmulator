__author__ = 'Chaddle'


class Master(object):

    def __init__(self, name):
        self.name = str(name).strip()
        self.master_dict = {}

    def attack(self, other):
        from random import randint
        if randint(1, 20) >= other.dict['armorClass']:
            damage = self.master_dict['attack']
            return damage
        else:
            pass

    # This method doesn't seem to work
    def saving_throw(self, save_type):
        from random import randint
        try:
            if str(save_type).capitalize() == 'Fort':
                save = randint(1, 20) + int(self.master_dict['saves']['Fort'])
                return save
            elif str(save_type).capitalize() == 'Ref':
                save = randint(1, 20) + int(self.master_dict['saves']['Ref'])
                return save
            elif str(save_type).capitalize() == 'Will':
                save = randint(1, 20) + int(self.master_dict['saves']['Will'])
                return save
        except Exception as e:
            print(e)
