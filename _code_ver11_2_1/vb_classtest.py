import pandas as pd


class Tstats1():
    def __init__(self,df,set,slot,number,action,result):
        print("Tstats1 class")
        self.df = df
        self.set = set
        self.slot = slot
        self.number = number
        self.action = action
        self.result = result
        pass
    def action1(self):
        if self.set =="":
            if self.slot =="":
                if self.number == "":
                    if self.result == "":
                        return len(self.df[(self.df["action1"] == self.action)])
                    elif self.result == "effective":
                        return len(self.df[(self.df["action1"] == self.action)& (self.df["result2"].isin(["c","o"]))])
                    else:
                        return len(self.df[(self.df["action1"] == self.action) & (self.df["result1"] == self.result)])
                else:
                    if self.result == "":
                        return len(self.df[(self.df["No.1"] == self.number) & (self.df["action1"] == self.action)])
                    elif self.result == "effective":
                        return len(self.df[(self.df["No.1"] == self.number) & (self.df["action1"] == self.action) & (self.df["result2"].isin(["c","o"]))])
                    else:
                        return len(self.df[(self.df["No.1"] == self.number) & (self.df["action1"] == self.action) & (self.df["result1"] == self.result)])
            else:
                if self.number == "":
                    if self.result == "":
                        return len(self.df[(self.df["pre1"] == self.slot) & (self.df["action1"] == self.action)])
                    elif self.result == "effective":
                       return len(self.df[(self.df["pre1"] == self.slot) & (self.df["action1"] == self.action) & (self.df["result2"].isin(["c","o"]))])
                    else:
                        return len(self.df[(self.df["pre1"] == self.slot) & (self.df["action1"] == self.action) & (self.df["result1"] == self.result)])

                else:
                    if self.result == "":
                        return len(self.df[(self.df["pre1"] == self.slot) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action)])
                    elif self.result =="effective":
                        return len(self.df[(self.df["pre1"] == self.slot) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action) & (self.df["result2"].isin(["c","o"]))])
                    else:
                        return len(self.df[(self.df["pre1"] == self.slot) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action) & (self.df["result1"] == self.result)])
        else:
            if self.slot =="":
                if self.number == "":
                    if self.result == "":
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["action1"] == self.action)])
                    elif self.result == "effective":
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["action1"] == self.action)& (self.df["result2"].isin(["c","o"]))])
                    else:
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["action1"] == self.action) & (self.df["result1"] == self.result)])
                else:
                    if self.result == "":
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action)])
                    elif self.result == "effective":
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action) & (self.df["result2"].isin(["c","o"]))])
                    else:
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action) & (self.df["result1"] == self.result)])
            else:
                if self.number == "":
                    if self.result == "":
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["pre1"] == self.slot) & (self.df["action1"] == self.action)])
                    elif self.result == "effective":
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["pre1"] == self.slot) & (self.df["action1"] == self.action) & (self.df["result2"].isin(["c","o"]))])
                    else:
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["pre1"] == self.slot) & (self.df["action1"] == self.action) & (self.df["result1"] == self.result)])
                else:
                    if self.result == "":
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["pre1"] == self.slot) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action)])
                    elif self.result =="effective":
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["pre1"] == self.slot) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action) & (self.df["result2"].isin(["c","o"]))])        
                    else:
                        return len(self.df[(self.df["Set"] == self.set) & (self.df["pre1"] == self.slot) & (self.df["No.1"] == self.number) & (self.df["action1"] == self.action) & (self.df["result1"] == self.result)])

act = Tstats1(df,"","","","a","p")
act.__init__(df,"","","","a","p")
act.action1()
