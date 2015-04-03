__author__ = "Chaddle"

import masterclass

class Player(masterclass.Master):

    def __init__(self):
        super().__init__(self)
        self.ability_scores = []
        self.class_dict = {}
        self.ability_dict = {}
        self.ability_scores = []
        self.class_name = ''

    def roll_abilities(self):
        if self.ability_scores != []:
            pass
        else:
            for i in range(6):

                results = []
                for j in range(4):

                    from random import randint
                    temp = randint(1, 6)
                    results.append(temp)

                results.remove(min(results))
                self.ability_scores.append(sum(results))

    def get_class(self):
        self.class_lookup()
        self.create_class()

    def class_lookup(self):
        class_list = ['barbarian', 'bard', 'cleric', 'druid', 'fighter',
                      'monk', 'paladin', 'ranger', 'rogue', 'sorcerer',
                      'wizard']
        self.class_name = input("Pick a class:\n"
                                "barbarian,\n"
                                "bard,\n"
                                "cleric,\n"
                                "druid,\n"
                                "fighter,\n"
                                "monk,\n"
                                "paladin,\n"
                                "ranger,\n"
                                "rogue,\n"
                                "sorcerer,\n"
                                "wizard\n\n")
        self.class_name = self.class_name.strip()
        if self.class_name not in class_list:
            print("This is not a valid class. Please try again.")
            self.class_lookup()
        else:
            return self.class_name

    def create_class(self):
        pass
