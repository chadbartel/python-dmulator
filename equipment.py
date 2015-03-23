__author__ = 'Chaddle'

class Armor(object):
    import re
    from bs4 import BeautifulSoup
    import urllib.request

    path = "file:///.../equipment/armor.htm"

    page = urllib.request.urlopen(path)
    soup = BeautifulSoup(page.read())
    col_heads = ['Cost', 'Armor/Shield Bonus', 'Maximum Dex Bonus', 'Armor Check Penalty',
                 'Arcane Spell Failure Chance', 'Speed30', 'Speed20', 'Weight']

    def __init__(self, name):
        self.name = str(name).strip()
        self.armor_dict = {}

    def get_stats(self):
        equip_table = []
        for line in self.soup.table.tbody.find_all('td'):
            equip_table.append(str(line.text).strip())

        armors_list = []
        for i in range(len(equip_table)):
            try:
                if i % 9 == 0 and self.name == equip_table[i]:
                    armors_list.append(equip_table[i])
            except Exception as e:
                print(e)

        armor_dict = {}
        for a in armors_list:
            armor_dict[a] = {}
            index = equip_table.index(a)
            for h in self.col_heads:
                armor_dict[a][h] = equip_table[index+1]
                index += 1
        self.armor_dict = armor_dict[self.name]

breastplate = Armor("Breastplate")
breastplate.get_stats()
print(breastplate.armor_dict["Cost"])
