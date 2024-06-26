from _code_ver12_1_1.Data.vb_data12 import DataConversion
import json
from _code_ver12_1_1.Function.vb_option12 import Option

DtC = DataConversion()
option = Option()



class File:
  def __init__(self):
    self.matchdata_path = r"c:\Volleyball12\matchdata.json"
    self.index_path = r"c:\Volleyball12\index.json"

    self.season = None
    self.tournament = None
    self.team = None
    self.team_ab = None
    self.player_index = None
    pass

  def set_index(self,season,tournament,team,team_ab):
    self.season = season
    self.tournament = tournament
    self.team = team
    self.team_ab = team_ab
    pass

  def save_data(self,match_info,set_info,set_result,play_d):

    match_d = DtC.play2match(play_d)

    with open(self.matchdata_path) as f:
      match_data = json.load(f)
    if (data0 := list(filter(lambda d:d["match_info"]==match_info,match_data))):
      data = match_data[match_data.index(data0[0])]
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

    with open(self.matchdata_path,"w") as f:
      json.dump(match_data,f,indent=2)
    pass

  def open_data(self,match_info):
    with open(self.matchdata_path) as f:
      match_datalist = json.load(f)
    if (datalist := list(filter(lambda d:d ["match_info"]==match_info,match_datalist))):
      match_data = match_datalist[match_datalist.index(datalist[0])]
      return match_data

  def search_data(self,match_infolist):
    pass

  def create_index(self,season,tournament,team,team_ab):
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
    player_index = _index[_index.index(list(filter(lambda d:d["season"]==self.season and d["tournament"]==self.tournament and d["team"]==self.team,_index))[0])]
    player_data = {
      "number":player_number,
      "position":player_position,
      "name":player_name
    }
    if not (check := list(filter(lambda d:d["number"]==player_data["number"] or d["name"]==player_data["name"],player_index["player_data"]))):
      player_index["player_data"].append(player_data)
    else:
      res = option.check("Player Already Existed","Update ?")
      if res == "OK":
        player_index["player_data"][player_index["player_data"].index(check[0])] = player_data
      else:
        return
    self.player_index = player_index
    with open(self.index_path,"w") as f:
      json.dump(_index,f,indent=2)
    pass

  def delete_player(self,player_number,player_position,player_name):
    with open(self.index_path) as f:
      _index = json.load(f)
    player_index = _index[_index.index(list(filter(lambda d:d["season"]==self.season and d["tournament"]==self.tournament and d["team"]==self.team,_index))[0])]
    player_data = player_index["player_data"]
    del_player_data = {
      "number":player_number,
      "position":player_position,
      "name":player_name
    }
    player_data.remove(del_player_data)
    self.player_index = player_index
    with open(self.index_path,"w") as f:
      json.dump(_index,f,indent=2)
    pass

  def open_index(self,season,tournament,team):
    with open(self.index_path) as f:
      _index = json.load(f)
    if (check := list(filter(lambda d: d["season"]==season and d["tournament"]==tournament and d["team"]==team,_index))):
      _index0 = check[0]
      return _index0
    

self = File()
