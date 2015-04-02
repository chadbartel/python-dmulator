__author__ = 'Chaddle'


class Class(object):

    def __init__(self):
        self.class_table = {}
        self.class_dict = {}
        self.class_name = ''


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

        path = "file:///C://Users//v-chbart//PycharmProjects//www.d20srd.org//srd//classes//bard.htm"
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
                if k in level_list and subcount < 7:
                    self.class_table[c]['Spells per Day'][k] = self.values[count]
                    subcount += 1
                    count += 1
                elif k in level_list and subcount >= 7:
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

        path = "file:///C://Users//v-chbart//PycharmProjects//www.d20srd.org//srd//classes//druid.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []

        for th in soup.tbody.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for k in self.keys:
            if k == "Spells per Day":
                self.keys.remove(k)
            else:
                pass

        for td in soup.tbody.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        level_list = ['0', '1st', '2nd', '3rd', '4th',
                      '5th', '6th', '7th', '8th', '9th']

        count = 0
        for c in iter(self.class_table.keys()):
            self.class_table[c]['Spells per Day'] = {}
            for k in iter(self.keys):
                if k in level_list:
                    self.class_table[c]['Spells per Day'][k] = self.values[count]
                    count += 1
                else:
                    self.class_table[c][k] = self.values[count]
                    count += 1


class Paladin(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//v-chbart//PycharmProjects//www.d20srd.org//srd//classes//paladin.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.keys = []
        self.values = []

        for th in soup.tbody.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for k in self.keys:
            if k == "Spells per Day":
                self.keys.remove(k)
            else:
                pass

        for td in soup.tbody.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        level_list = ['1st', '2nd', '3rd', '4th']

        count = 0
        for c in iter(self.class_table.keys()):
            self.class_table[c]['Spells per Day'] = {}
            for k in iter(self.keys):
                if k in level_list:
                    self.class_table[c]['Spells per Day'][k] = self.values[count]
                    count += 1
                else:
                    self.class_table[c][k] = self.values[count]
                    count += 1


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

        for th in soup.tbody.find_all('th'):
            try:
                self.keys.append(str(th.text).strip())
            except AttributeError:
                self.keys.append(str(th).strip())

        for k in self.keys:
            if k == "Spells per Day":
                self.keys.remove(k)
            else:
                pass

        for td in soup.tbody.find_all('td'):
            try:
                self.values.append(str(td.text).strip())
            except AttributeError:
                self.values.append(str(td).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        level_list = ['1st', '2nd', '3rd', '4th']

        count = 0
        for c in iter(self.class_table.keys()):
            self.class_table[c]['Spells per Day'] = {}
            for k in iter(self.keys):
                if k in level_list:
                    self.class_table[c]['Spells per Day'][k] = self.values[count]
                    count += 1
                else:
                    self.class_table[c][k] = self.values[count]
                    count += 1


class Sorcerer(Class):
    # Magic class
    def __init__(self):
        super().__init__()

    def build_table(self):
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//v-chbart//PycharmProjects//www.d20srd.org//srd//classes//sorcererWizard.htm"
        page = urllib.request.urlopen(path)
        soup = BeautifulSoup(page.read())
        self.table_keys = {}
        self.table_values = {}
        self.sorc_tables = {}
        self.table_ids = ['tableTheSorcerer', 'tableSorcererSpellsKnown']
        level_list = ['0', '1st', '2nd', '3rd', '4th',
                      '5th', '6th', '7th', '8th', '9th']

        for table in soup.find_all("table"):
            id = table['id']
            if id in self.table_ids:
                self.sorc_tables[id] = table
            else:
                pass

        for table in self.sorc_tables.values():
            table_soup = BeautifulSoup(str(table))
            id = table['id']
            self.table_keys[id] = []
            for th in table_soup.find_all("th"):
                if str(th.text).strip() == "Spells Known":
                    pass
                elif str(th.text).strip() == "Spells per Day":
                    pass
                else:
                    self.table_keys[id].append(str(th.text).strip())

        for table in self.sorc_tables.values():
            table_soup = BeautifulSoup(str(table))
            id = table['id']
            self.table_values[id] = []
            for td in table_soup.find_all("td"):
                self.table_values[id].append(str(td.text).strip())

        for i in range(1, 21):
            self.class_table[i] = {}

        for c in self.class_table.keys():
            self.class_table[c] = {}
            for k in self.table_keys.keys():
                self.class_table[c][k] = {}

        # Create sub-sub-dicts here
        # this is where the values will be zipped
        # to their corresponding key in 'class_table'

        for i in range(1, 21):
            # This is just two keys:
            # 'tableTheSorcerer' and 'tableSorcererSpellsKnown'
            for c in self.class_table[i].keys():
                # Each of these sub-dicts contains a list
                # We need to iterate through each list
                # and set them equal to their own empty values
                for k in self.table_keys[c]:
                    self.class_table[i][c][k] = ''

        # Iterate from 1 through 20
        for i in self.class_table.keys():
            # 'tableTheSorcerer' and 'tableSorcererSpellsKnown'
            count = 0
            for c in self.class_table[i].keys():
                # Iterate through keys in:
                # 'tableTheSorcerer' and 'tableSorcererSpellsKnown'
                for k in self.class_table[i][c].keys():
                    self.class_table[i][c][k] = self.table_values[c][count]
                    count += 1


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
        self.table_keys = {}
        self.table_values = {}
        self.wiz_tables = {}
        self.table_ids = ['tableTheWizard']

        for table in soup.find_all("table"):
            id = table['id']
            if id in self.table_ids:
                self.wiz_tables[id] = table
            else:
                pass

        for table in self.wiz_tables.values():
            table_soup = BeautifulSoup(str(table))
            id = table['id']
            self.table_keys[id] = []
            for td in table_soup.find_all("th"):
                self.table_keys[id].append(str(td.text).strip())

        for table in self.wiz_tables.values():
            table_soup = BeautifulSoup(str(table))
            id = table['id']
            self.table_values[id] = []
            for td in table_soup.find_all("td"):
                self.table_values[id].append(str(td.text).strip())



sorc = Sorcerer()
sorc.build_table()
print(sorc.table_keys)
print(sorc.table_values['tableTheSorcerer'],
      len(sorc.table_values['tableTheSorcerer']))
print(sorc.table_values['tableSorcererSpellsKnown'],
      len(sorc.table_values['tableSorcererSpellsKnown']))
print(sorc.class_table)
print(sorc.table_values['tableTheSorcerer'][0])
