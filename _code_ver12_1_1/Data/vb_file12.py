from Data.vb_data12 import DataConversion
import json

DC = DataConversion()

matchdata_path = r"c:\Volleyball12\matchdata.json"
index_path = r"c:\Volleyball12\index.json"

class File:
  def __init__():
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
    with open(matchdata_path) as f:
      match_datalist = json.load(f)
    match_data = match_datalist[match_datalist.index(list(filter(lambda d:d["match_info"]==match_info,match_datalist))[0])]
    return match_data

  def search_data(self,match_infolist):
    pass

  def set_index(self,season,tournament,team):
    self.season = season
    self.tournament = tournament
    self.team = team
    with open(index_path) as f:
      index = json.load(f)
    new_index = {
      "season":self.season,
      "tournament":self.tournament,
      "team":self.team,
      "player_data":[]
    }
    index.append(new_index)
    with open(index_path,"w") as f:
      json.dump(index,f,indent = 2)

  def append_player(player_number,player_position,player_name):
    with open(index_path) as f:
      _index = json.load(f)
    new_index = _index[_index.index(list(filter(lambda d:d["season"]==self.season and d["tournament"]==self.tournament and d["team"]==self.team,_index))[0])]
    player_data = {
      "number":player_number,
      "position":player_position,
      "name":player_name
    }
    new_index["player_data"].append(player_data)
    with open(index_path,"w") as f:
      json.dump(_index,f,indent=2)
    pass

  def open_index(self,season,tournament,team):
    with open(index_path) as f:
      _index = json.load(f)
    return _index

self = File()
self.season = "2023-24"
self.tournament = "Italian Serie A1"
self.team = "Allianz Milano"
player_number = 1
player_position = "OH"
player_name = "Matey Kaziyski"

