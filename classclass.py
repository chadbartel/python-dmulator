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

        path = "file:///E://www.d20srd.org//srd//classes//fighter.htm"
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

        val_index = 0
        for v in self.values:
            if self.values.index(v) % 6 == 0:
                self.class_table[v] = {}
            else:
                pass


class Barbarian(Class):
    # Melee class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//barbarian.htm"
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


class Rogue(Class):
    # Melee class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//rogue.htm"
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


class Monk(Class):
    # Melee class
    def __init__(self):
        super().__init__()
    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//monk.htm"
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


class Bard(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//bard.htm"
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


class Cleric(Class):
    # Magic class
    def __init__(self):
        super().__init__()
        self.build_table()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//cleric.htm"
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

        for v in self.values:
            if self.values.index(v) % 16 == 0:
                self.class_table[v] = {}
            else:
                pass

        for k in self.class_table.keys():
            for v in self.values:
                if k == v:
                    self.values.remove(v)

        for c in self.class_table:
            # For each 15 items in values
            #   append these values to each of the
            #   15 subdicts in class_table
            pass


class Druid(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//druid.htm"
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


class Paladin(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//paladin.htm"
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


class Ranger(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//ranger.htm"
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


class Sorcerer(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//sorcererWizard.htm"
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


class Wizard(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//classes//sorcererWizard.htm"
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


cleric = Cleric()
cleric.build_table()
print(cleric.class_table, len(cleric.class_table))
print(cleric.values, len(cleric.values))
print(cleric.keys, len(cleric.keys))
