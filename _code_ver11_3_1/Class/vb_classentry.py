import pandas as pd


class Entry_match:
  def __init__(self) -> None:
    print("Entry")
    self.season = ""
    self.tournament = ""
    self.date = ""
    self.Team1 = ""
    self.team2 = ""

  def make_match_info(self):
    self.season = input("Season?")
    self.tournament = input("Tournament?")
    self.date = input("Date?")
    self.Team1 = input("Team1?")
    self.Team2 = input("Team2?")

  def team_info(self):
    team_index = pd.read_excel(r"C:\Volleyball\Index\Team_index.xlsx",sheet_name=self.tournament)
    self.data_team1 = team_index[(team_index["Season"]==self.season)&(team_index["Team"]==self.Team1)]
    self.data_team2 = team_index[(team_index["Season"]==self.season)&(team_index["Team"]==self.Team2)]

class Entry_set():
  def __init__(self):
    self.set = ""

if __name__ == "__main__":
  entry = Entry_match()
  entry.make_match_info()
  entry.team_info()
  entry_set = Entry_set()
  entry_set.season
  