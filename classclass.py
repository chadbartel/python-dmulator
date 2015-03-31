__author__ = 'Chaddle'


class Class(object):

    def __init__(self):
        self.class_table = {}
        self.class_dict = {}
        self.class_name = ''

    def get_class(self):
        self.class_name = input("Pick a class: (barbarian, bard, cleric, druid, fighter, "
                                "monk, paladin, ranger, rogue, sorcerer, wizard\n")
        self.class_name = self.class_name.lower().strip()


class Fighter(Class):
    # Melee class
    def __init__(self):
        super().__init__()
        self.build_table()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//fighter.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []

        for th in soup.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for td in soup.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        count = 0
        for c in iter(self.class_table.keys()):
            for k in iter(self.keys):
                self.class_table[c][k] = self.values[count]
                count += 1

class Barbarian(Class):
    # Melee class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//barbarian.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []

        for th in soup.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for td in soup.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        count = 0
        for c in iter(self.class_table.keys()):
            for k in iter(self.keys):
                self.class_table[c][k] = self.values[count]
                count += 1


class Rogue(Class):
    # Melee class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//rogue.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []

        for th in soup.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for td in soup.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        count = 0
        for c in iter(self.class_table.keys()):
            for k in iter(self.keys):
                self.class_table[c][k] = self.values[count]
                count += 1


class Monk(Class):
    # Melee class
    def __init__(self):
        super().__init__()
    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//monk.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []

        for th in soup.thead.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for td in soup.tbody.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        count = 0
        for c in iter(self.class_table.keys()):
            for k in iter(self.keys):
                self.class_table[c][k] = self.values[count]
                count += 1


class Bard(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//bard.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []

        for th in soup.thead.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for td in soup.tbody.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        for k in self.keys:
            if k == "Spells Known":
                self.keys.remove(k)
            else:
                pass

        for k in self.keys:
            if k == "Spells per Day":
                self.keys.remove(k)
            else:
                pass

        level_list = ['0', '1st', '2nd', '3rd', '4th', '5th', '6th']
        count = 0
        for c in iter(self.class_table.keys()):
            self.class_table[c]['Spells per Day'] = {}
            self.class_table[c]['Spells Known'] = {}
            subcount = 0
            for k in iter(self.keys):
                if k in level_list and subcount < 8:
                    self.class_table[c]['Spells per Day'][k] = self.values[count]
                    subcount += 1
                    count += 1
                elif k in level_list and subcount >= 8:
                    self.class_table[c]['Spells Known'][k] = self.values[count]
                    subcount += 1
                    count += 1
                else:
                    self.class_table[c][k] = self.values[count]
                    count += 1


class Cleric(Class):
    # Magic class
    def __init__(self):
        super().__init__()
        self.build_table()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//cleric.htm"
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
            elif k == "Level":
                self.keys.remove(k)
            else:
                pass

        for i in range(1, 21):
            self.class_table[i] = {}

        # This gives you a dict of integers [1, 20]
        self.dict_keys = []
        for v in self.values:
            if self.values.index(v) % 16 == 0:
                self.dict_keys.append(v)
            else:
                pass

        temp_vals = iter(self.values)
        for v in temp_vals:
            if v in self.dict_keys:
                self.values.remove(v)
            else:
                pass

        count = 0
        for c in iter(self.class_table.keys()):
            for k in iter(self.keys):
                self.class_table[c][k] = self.values[count]
                count += 1


class Druid(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//druid.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []


class Paladin(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//paladin.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []


class Ranger(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//ranger.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []


class Sorcerer(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//sorcererWizard.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []


class Wizard(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//sorcererWizard.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []



bard = Bard()
bard.build_table()
print(bard.class_table[1])
