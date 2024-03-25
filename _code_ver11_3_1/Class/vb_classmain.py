from _code_ver11_3_1.Class import Entry


class Main:
  def __init__(self):
    pass
  
  def main_start(self):
    pass
  
  def main_entry(self):
    pass

  def main_entry_info(self):
    season = input("Season?")
    tournament = input("Tournament?")
    date = input("Date?")
    Team1 = input("Team1?")
    Team2 = input("Team2?")
    return season,tournament,date,Team1,Team2

  def main_search(self):
    pass

if __name__ == "__main__":
  main = Main()
  mode = input("Mode?")
  season = input("Season?")
  tournament = input("Tournament?")
  date = input("Date?")
  Team1 = input("Team1?")
  Team2 = input("Team2?")
  entry = Entry(season,tournament,date,Team1,Team2)

