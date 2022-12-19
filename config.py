import configparser
import datetime as dt
from FileChecker import FileChecker
import pandas as pd
# from WeeklyPlanner import PUSH,PULL,LEGS

baseline = {
            'last_updated': dt.datetime.today(),
            'types': ['Push', 'Pull', 'Legs']

        }

class configurator():
    def __init__(self):
        self.config = configparser.ConfigParser()

        self.filename = 'exercise.ini'


        configFC = FileChecker(self.filename)
        if not(configFC.exists):

            self.config['DEFAULT'] = baseline
        else:
            self.config.read(self.filename)
        self.exTypes = baseline['types']



    def writeToConfig(self):




        with open(self.filename, 'w+') as configfile:

            self.config.write(configfile)
    def addToConfig(self,diction : dict):

        for key,value in diction.items():

            self.config[key]=value
        self.writeToConfig()

    def removeFromConfig(self,sect):

        with open(self.filename, "r") as configfile:
            self.config.read_file(configfile)

        print(self.config.sections())
        self.config.remove_section(sect)
        print(self.config.sections())

        with open(self.filename, "w") as configfile:
            self.config.write(configfile)

        # this just verifies that [b] section is still there
        with open(self.filename, "r") as configfile:
            print(configfile.read())


    def changeConfig(self,key,value):
        self.config[key]=value

    def refreshExerciseConfig(self,modify = True):
        self.config['DEFAULT'] = baseline

        for type in self.exTypes:
            self.config[type] = {
                'last_date': pd.read_excel('Planners/Excel/Planner -.xlsx'.replace('-','- '+type)).columns[-1],
                'type': type

            }
        if modify:
            self.writeToConfig()
    def sectionToDict(self,sect):

        return self.config[sect]
    def resetConfig(self):
        for sect in self.config.sections():
            self.removeFromConfig(sect)
        print(baseline)
        self.config['DEFAULT'] = baseline
        self.refreshExerciseConfig()




if __name__ == '__main__':
    cfig = configurator()
    cfig.resetConfig()