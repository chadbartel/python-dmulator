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
                                "1. barbarian,\n"
                                "2. bard,\n"
                                "3. cleric,\n"
                                "4. druid,\n"
                                "5. fighter,\n"
                                "6. monk,\n"
                                "7. paladin,\n"
                                "8. ranger,\n"
                                "9. rogue,\n"
                                "10. sorcerer, or\n"
                                "11. wizard\n\n")
        self.class_name = self.class_name.strip()
        if self.class_name not in class_list:
            print("This is not a valid class. Please try again.")
            self.class_lookup()
        else:
            return self.class_name

    def create_class(self):
        if self.class_name == "barbarian":
            from classclass import Barbarian
            self.name = Barbarian()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "bard":
            from classclass import Bard
            self.name = Bard()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "cleric":
            from classclass import Cleric
            self.name = Cleric()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "druid":
            from classclass import Druid
            self.name = Druid()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "fighter":
            from classclass import Fighter
            self.name = Fighter()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "monk":
            from classclass import Monk
            self.name = Monk()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "paladin":
            from classclass import Paladin
            self.name = Paladin()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "ranger":
            from classclass import Ranger
            self.name = Ranger()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "rogue":
            from classclass import Rogue
            self.name = Rogue()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "sorcerer":
            from classclass import Sorcerer
            self.name = Sorcerer()
            self.name.build_table()
            self.class_dict = self.name.class_table
        elif self.class_name == "wizard":
            from classclass import Wizard
            self.name = Wizard()
            self.name.build_table()
            self.class_dict = self.name.class_table
        else:
            raise Exception



chad = Player()
chad.get_class()
print(chad.class_dict)
