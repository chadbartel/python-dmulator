__author__ = "Chaddle"

import masterclass

class Player(masterclass.Master):

    def __init__(self):
        super().__init__(self)
        self.ability_scores = []
        self.class_dict = {}
        self.ability_dict = {}

    def roll_abilities(self):

        self.ability_scores = []
        for i in range(6):

            results = []
            for j in range(4):
                from random import randint
                temp = randint(1, 6)
                results.append(temp)

            self.ability_scores.append(sum(results))
            return results

        return self.ability_scores

    def choose_class(self):
        self.get_class()

    def get_class(self):
        self.class_name = ''
        self.class_name = input("Pick a class, any class: (barbarian, bar, cleric, druid, fighter, "
                    "monk, multiclass, paladin, ranger, rogue, sorcererWizard\n")
        import re
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//"
        path += self.class_name + ".htm"
        try:
            page = urllib.request.urlopen(path)
            soup = BeautifulSoup(page.read())
            keys = []
            values = []

        except:
            pass
        
        return None