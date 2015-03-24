__author__ = 'Chaddle'

class_name = input("Pick a class: (barbarian, bar, cleric, druid, fighter, "
            "monk, multiclass, paladin, ranger, rogue, sorcererWizard\n")
import re
from bs4 import BeautifulSoup
import urllib.request

path = "file:///C://Users//Chaddle//PycharmProjects//www.d20srd.org//srd//classes//"
path += class_name + ".htm"

try:
    page = urllib.request.urlopen(path)
    soup = BeautifulSoup(page.read())
    keys = []
    values = []

    for h in soup.find_all('h5'):
        try:
            values.append(str(h.text).strip())
        except AttributeError:
            values.append(str(h).strip())

except Exception as e:
    print(e)
