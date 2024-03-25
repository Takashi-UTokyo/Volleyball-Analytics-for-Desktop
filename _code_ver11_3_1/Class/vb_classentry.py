

class Entry:
  def __init___(self,season,tournament,date,Team1,Team2) -> None:
    print("Entry")
    self.season = season
    self.tournament = tournament
    self.date = date
    self.Team1 = Team1
    self.team2 = Team2
  
  def make_set_info(self):
    pass

entry = Entry("2023","World Olympic Qualification","202.11.17","Japan","Slovenia")
entry.__init__()
entry.__init__("2023","World Olympic Qualification","202.11.17","Japan","Slovenia")