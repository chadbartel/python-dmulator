__author__ = 'Chaddle'


class Class(object):

    def __init__(self):
        self.class_table = {}
        self.class_dict = {}
        self.class_name = ''

    def get_class(self):
        self.class_name = input("Pick a class: (barbarian, bard, cleric, druid, fighter, "
                                "monk, paladin, ranger, rogue, sorcererWizard\n")
        self.class_name = self.class_name.lower().strip()
        self.build_table()


class Fighter(Class):
    # Melee class
    def __init__(self):
        super().__init__()


class Barbarian(Class):
    # Melee class
    def __init__(self):
        super().__init__()


class Rogue(Class):
    # Melee class
    def __init__(self):
        super().__init__()


class Monk(Class):
    # Melee class
    def __init__(self):
        super().__init__()


class Bard(Class):
    # Magic class
    def __init__(self):
        super().__init__()


class Cleric(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//"
        path += self.class_name + ".htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []

        for th in soup.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for td in soup.tbody.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for k in self.keys:
            if k == "Spells per Day1":
                self.keys.remove(k)
            if k == "Level":
                self.keys.remove(k)

        val_index = 0
        for v in self.values:
            if self.values.index(v) % 16 == 0:
                self.class_table[v] = {}
                index = self.class_table.index(v)
            else:
                for i in range(1, 20):
                    self.class_table[i] = {}
            val_index += 1

class Druid(Class):
    # Magic class
    def __init__(self):
        super().__init__()


class Paladin(Class):
    # Magic class
    def __init__(self):
        super().__init__()


class Ranger(Class):
    # Magic class
    def __init__(self):
        super().__init__()


class Sorcerer(Class):
    # Magic class
    def __init__(self):
        super().__init__()


class Wizard(Class):
    # Magic class
    def __init__(self):
        super().__init__()

cleric = Cleric()
cleric.get_class()
print(cleric.keys, cleric.values)
