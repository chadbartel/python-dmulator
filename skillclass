__author__ = 'Chaddle'

class Skill(object):

    def __init__(self, name):
        self.name = name.strip().lower()
        self.class_file = ''
        self.rank = 0.0

    def get_class(self):
        import os

        class_dir = ''
        for file in os.listdir("C:\\...\\skills\\"):
            if file == str(self.name + ".htm"):
                class_dir = str(file).strip()

        self.class_file = class_dir

    def get_stats(self):
        self.get_class()


skill = Skill("bluff")
skill.get_stats()
print(skill.class_file)
