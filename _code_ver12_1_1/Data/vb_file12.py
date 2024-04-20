from _code_ver12_1_1.Data.vb_data12 import DataConversion
import json

DC = DataConversion()


class File:
  def __init__(self):
    self.matchdata_path = r"c:\Volleyball12\matchdata.json"
    self.index_path = r"c:\Volleyball12\index.json"
    pass

  def save_data(self,match_info,set_info,set_result,play_d):

    match_d = DC.play2match(play_d)

    with open(matchdata_path) as f:
      match_data = json.load(f)
    if (data := match_data[match_data.index(list(filter(lambda d:d["match_info"]==match_info,match_data))[0])]):
      data["set_info"] = set_info
      data["set_result"] = set_result
      data["match_d"] = match_d
    else:
      new_match_data = {
        "match_info":match_info,
        "set_info":set_info,
        "set_result":set_result,
        "match_d":match_d
      }
      match_data.append(new_match_data)

    with open(matchdata_path,"w") as f:
      f.dump(match_data,f,indent=2)
    pass

  def open_data(self,match_info):
    with open(self.matchdata_path) as f:
      match_datalist = json.load(f)
    match_data = match_datalist[match_datalist.index(list(filter(lambda d:d["match_info"]==match_info,match_datalist))[0])]
    return match_data

  def search_data(self,match_infolist):
    pass

  def set_index(self,season,tournament,team,team_ab):
    self.season = season
    self.tournament = tournament
    self.team = team
    self.team_ab = team_ab
    with open(self.index_path) as f:
      index = json.load(f)
    if not (list(filter(lambda d: d["season"]==season and d["tournament"]==tournament and d["team"]==team,index))):
      new_index = {
        "season":self.season,
        "tournament":self.tournament,
        "team":self.team,
        "abbreviation":team_ab,
        "player_data":[]
      }
      index.append(new_index)
      with open(self.index_path,"w") as f:
        json.dump(index,f,indent = 2)
    pass

  def append_player(self,player_number,player_position,player_name):
    with open(self.index_path) as f:
      _index = json.load(f)
    new_index = _index[_index.index(list(filter(lambda d:d["season"]==self.season and d["tournament"]==self.tournament and d["team"]==self.team,_index))[0])]
    player_data = {
      "number":player_number,
      "position":player_position,
      "name":player_name
    }
    if not list(filter(lambda d:d==player_data,new_index["player_data"])):
      new_index["player_data"].append(player_data)
      with open(self.index_path,"w") as f:
        json.dump(_index,f,indent=2)
    pass

  def open_index(self,team):
    with open(self.index_path) as f:
      _index = json.load(f)
    _index0 = list(filter(lambda d: d["season"] == self.season and d["tournament"] == self.tournament and d["team"] == team,_index))[0]
    return _index0

self = File()
self.season = "2023-24"
self.tournament = "Italian Serie A1"
self.team = "Allianz Milano"
self.team_ab = "MIL"
self.set_index(self.season,self.tournament,self.team,self.team_ab)
player_number = 1
player_position = "OH"
player_name = "Matey Kaziyski"
self.append_player(player_number,player_position,player_name)
player_number = 14
player_position = "OH"
player_name = "Yuki Ishikawa"
self.append_player(player_number,player_position,player_name)
self.open_index(team)
