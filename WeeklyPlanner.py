import numpy as np
import pandas as pd
import ExerciseReader as ER
import datetime as dt
from FileChecker import FileChecker
# from openpyxl import Workbook,load_workbook
# from openpyxl.styles import Font
# import xlsxwriter

# data = pd.read_csv('./ExerciseList.csv')

from config import configurator

configData = configurator()
print(configData.sectionToDict('DEFAULT')['types'])
strTypes = configData.sectionToDict('DEFAULT')['types'].translate({ord(i): None for i in "[]' "})
exTypes = strTypes.split(',')
print(exTypes)
PUSH = exTypes[0]
PULL = exTypes[1]
LEGS = exTypes[2]

class WeeklyPlanner():
    def __init__(self,data,strat=PUSH,addDays=7):
        self.strat = strat
        self.last_date = configData.sectionToDict(self.strat)['last_date']

        self.last_date = dt.datetime.strptime(self.last_date,'%d-%m-%Y')
        print(self.last_date)
        ExerciseList = ER.ExerciseReader(data)
        print(dt.datetime.today())
        print(type(dt.datetime.today()))
        days = dt.datetime.today() + dt.timedelta(days=addDays)
        date_list = pd.date_range(start= self.last_date, end=days).strftime("%d-%m-%Y").tolist()
        print(date_list)

        exName = 'Exercise - '+self.strat
        if exName not in date_list:

            date_list = [exName] + date_list

        self.data = pd.DataFrame(columns=date_list)


        self.data[exName] = ExerciseList.getDataFrame()[self.strat]

        self.exName = exName
        # print(ExerciseList.getPull())

        self.csvFilePath = './Planners/CSV/Planner -.csv'.replace('-','- '+ self.strat)
        self.excelFilePath = './Planners/Excel/Planner -.xlsx'.replace('-','- '+self.strat)


    def changeFontSize(self,font=9):
        # wb = pd.xlsxwriter.Workbook('./Planners/Excel/Planner -.xlsx'.replace('-','- '+self.strat),encoding = 'ascii')
        # ws = wb['sheet1']

        writer = pd.ExcelWriter('./Planners/Excel/Planner -.xlsx'.replace('-','- '+self.strat), engine='xlsxwriter')
        self.data.to_excel(writer, sheet_name='Sheet1',index=False)
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Add some cell formats.
        format1 = workbook.add_format({'font_size': font,
                                       # 'text_wrap': True,
                                       'align': 'top',

                                       })

        header_format = workbook.add_format({
            'bold': True,
            'font_size': font,
            'text_wrap': True,
            'valign': 'top',
            'fg_color': '#D7E4BC',
            'border': 1})



        for row in range(0,len(self.data)+1):
            worksheet.set_row(row,cell_format=format1)



        for col_num, value in enumerate(self.data.columns.values):
            worksheet.write(0, col_num, value, header_format)


            # Set the format but not the column width.
        worksheet.set_column(0,0,width=20)
        worksheet.freeze_panes(1, 1)

        # Close the Pandas Excel writer and output the Excel file.
        writer.close()

    def deleteColumn(self, columnname: str):
        if columnname in self.data.columns:
            self.data = self.data.drop(columns=[columnname])
            self.UpdateExerciseListFile()

    def UpdateWeeklyPlannerFile(self,Force=False):
        csvExists = FileChecker(self.csvFilePath)
        if csvExists.exists and not(Force):
            recentPlanner = pd.read_csv(self.csvFilePath)
            self.data = self.data.drop(columns=recentPlanner.columns,errors='ignore')
            self.data = pd.concat([recentPlanner, self.data], axis=1)

        self.data.to_csv(self.csvFilePath, index=False)


    def getExcel(self,Force=False):
        excelExists = FileChecker(self.excelFilePath)
        if excelExists.exists and not(Force):

            recentPlanner = pd.read_excel(self.excelFilePath)
            exList = self.data[self.exName]

            self.data = self.data.drop(columns=recentPlanner.columns,errors='ignore')
            self.data = pd.concat([recentPlanner,self.data],axis=1)
            indexes = exList.index[~exList.isin(self.data[self.exName])]
            indexes2 = self.data[self.exName].index[~self.data[self.exName].isin(exList)]
            self.data = self.data.drop(indexes2).reset_index(drop=True)

            for added, ind in enumerate(indexes):

                self.data.iloc[ind:, 1:-1] = self.data.iloc[ind:, 1:-1].shift(1, axis=0)
            self.data[self.exName].update(exList)


            # self.data = recentPlanner.join(self.data,how='left')
        self.data.to_excel(self.excelFilePath, index=False)
        self.UpdateWeeklyPlannerFile(Force=True)
        self.changeFontSize()
        configData.refreshExerciseConfig()

    def exploreHeaders(self):

        for col_title in self.data.columns:
            print(col_title)

    def exploreDataFrame(self):
        print(self.data)

    def getDataFrame(self):
        return self.data





if __name__ == '__main__':
    WP = WeeklyPlanner(ER.data,PULL)
    WP.getExcel()
    WP = WeeklyPlanner(ER.data, PUSH)
    WP.getExcel()
    WP = WeeklyPlanner(ER.data, LEGS)
    WP.getExcel()