__author__ = 'Chaddle'

class Class(object):

    def __init__(self):
        self.class_table = {}
        self.class_dict = {}

    def get_class(self):
        class_name = input("Pick a class: (barbarian, bard, cleric, druid, fighter, "
                    "monk, multiclass, paladin, ranger, rogue, sorcererWizard\n")
        import re
        from bs4 import BeautifulSoup
        import urllib.request

        path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//"
        path += class_name + ".htm"

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
            self.col_heads.remove("Spells per Day1")


            for td in soup.tbody.find_all('td'):
                try:
                    self.contents.append(str(td.text).strip())
                except AttributeError:
                    self.contents.append(str(td).strip())

        except Exception as e:
            print(e)

druid = Class()
druid.get_class()
print(druid.col_heads, len(druid.col_heads), druid.contents, len(druid.contents))
# This only works with 'cleric' right now
