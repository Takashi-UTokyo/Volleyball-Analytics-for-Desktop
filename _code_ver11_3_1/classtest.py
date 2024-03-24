import pandas as pd

class calc():
    def __init__(self,score1,score2,score3) -> None:
        print("calculate class")
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        pass
    def sum(self):
        sum = self.score1 + self.score2 + self.score3 
        return sum
    def avg(self):
        avg = self.sum()/3
        return avg
    def std(self):
        std = (((self.score1 - self.avg())**2 + (self.score2 - self.avg())**2 + (self.score3 - self.avg())**2)/3)**(1/2)
        return std
