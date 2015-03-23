__author__ = 'Chaddle'

import masterclass

class Monster(masterclass.Master):

    def __init__(self, monster_name):
        super().__init__(self)
        self.monster_name = monster_name.strip().lower()

    def get_monster(self):
        # Set all properties here like the Class
        import re
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///E://www.d20srd.org//srd//monsters//"
        path += self.monster_name + ".htm"
        try:
            page = urllib.request.urlopen(path)
            soup = BeautifulSoup(page.read())
            keys = []
            values = []

            for td in soup.find_all('td'):
                try:
                    values.append(str(td.text).strip())
                except AttributeError:
                    values.append(str(td).strip())

            count = 0
            for th in soup.find_all('a', {"href": re.compile("intro.htm#")}):
                keys.append(str(th.get('href')))
                keys[count] = keys[count].replace("intro.htm#", "").strip()
                count += 1

            self.master_dict = dict(zip(keys, values))

            # One way to make a nested dict
            abilities = self.master_dict.get('abilities')
            if abilities:
                self.master_dict['abilities'] = {m.group(1).capitalize(): int(m.group(2))
                                              for m in re.finditer(r'(\w+) (\d+)', abilities)}

            saves = self.master_dict.get('saves')
            if saves:
                self.master_dict['saves'] = {m.group(1): int(m.group(2))
                                          for m in re.finditer(r'(\w+) (\+\d|\-\d)+', saves)}

            organization = self.master_dict.get('organization')
            if organization:
                self.master_dict['organization'] = {m.group(1).capitalize(): m.group(2)
                    for m in re.finditer(r'(\w+) \(([^)]+)\)',
                                         organization)}
        except LookupError as e:
            print(e)

        # Here is where you would generate the new class
        # The class would be named after the monster name
        # It will inherit from the 'Monster' class
