import numpy as np
import pandas as pd

data = pd.read_csv('./ExerciseList.csv')


class ExerciseReader():
    def __init__(self, data):
        self.data = data

        print(type(data))


    def deleteColumn(self, columnname: str):
        if columnname in self.data.columns:
            self.data = self.data.drop(columns=[columnname])
            self.UpdateExerciseListFile()

    def UpdateExerciseListFile(self):
        self.data.to_csv('ExerciseList.csv',index=False)


    def exploreHeaders(self):

        for col_title in self.data.columns:
            print(col_title)

    def exploreDataFrame(self):
        print(self.data)


    def getDataFrame(self):
        return self.data
    def getPush(self):
        return self.data['Push']
    def getPull(self):
        return self.data['Pull']
    def getLegs(self):
        return self.data['Legs']






if __name__ == '__main__':

    ER = ExerciseReader(data)
    ER.exploreHeaders()
    ER.exploreDataFrame()


