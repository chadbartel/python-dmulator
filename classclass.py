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
        class_list = ["barbarian", "bard", "cleric", "druid", "fighter", "monk",
                      "paladin", "ranger", "rogue", "sorcerer", "wizard"]

        if self.class_name not in class_list:
            print("This isn't a class?")
        else:
            self.build_table()

    def build_table(self):
        # Each class will be hard-coded as a sub-class of this
        # super class.
        # This method will get all the table data for each class.
        from bs4 import BeautifulSoup
        import urllib.request

        if self.class_name == "sorcerer" or self.class_name == "wizard":
            path = "file:///E://www.d20srd.org//srd//classes//sorcererWizard"
        else:
            path = "file:///E://www.d20srd.org//srd//classes//"
            path += self.class_name + ".htm"

        try:
            page = urllib.request.urlopen(path)
            soup = BeautifulSoup(page.read())
            self.col_heads = []
            self.contents = []

            for th in soup.find_all('th'):
                try:
                    self.col_heads.append(str(th.text).strip())
                except AttributeError:
                    self.col_heads.append(str(th).strip())

            for td in soup.tbody.find_all('td'):
                try:
                    self.contents.append(str(td.text).strip())
                except AttributeError:
                    self.contents.append(str(td).strip())

        except Exception as e:
            print(e)


class Fighter(Class):

    def __init__(self):
        super().__init__()


class Barbarian(Class):

    def __init__(self):
        super().__init__()


class Rogue(Class):

    def __init__(self):
        super().__init__()
