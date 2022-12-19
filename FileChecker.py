from os.path import exists

class FileChecker():
    def __init__(self,filepath):
        self.filepath = filepath
        self.exists = self.checker()

    def checker(self):
        return exists(self.filepath)

    def status(self):
        if (self.exists):
            print(filepath + ' - Exists')
            return self.exists
        print(filepath + ' - Does not Exists')
        return self.exists

if __name__ == '__main__':
    strat = "PUSH"
    filepath = './Planners/CSV/Planner -.csv'.replace('-','- '+ strat)
    FC = FileChecker(filepath)
    FC.status()




