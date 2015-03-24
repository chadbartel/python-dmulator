__author__ = "Chaddle"

import masterclass

class Player(masterclass.Master):

    def __init__(self):
        super().__init__(self)
        self.ability_scores = []
        self.class_dict = {}
        self.ability_dict = {}
        self.ability_scores = []

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
        pass

chad = Player()
chad.roll_abilities()
print(chad.ability_scores)
