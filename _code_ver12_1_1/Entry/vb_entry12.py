from _code_ver12_1_1.Function import vb_option as vo
from _code_ver12_1_1.Data import vb_file as vf
from _code_ver12_1_1.Data import vb_data2 as vd2

import PySimpleGUI as sg
import pandas as pd

from _code_ver12_1_1.Data.vb_file12 import File
from _code_ver12_1_1.Function.vb_window12 import Window0
from _code_ver12_1_1.Data.vb_data12 import DataConversion
from _code_ver12_1_1.Function.vb_option12 import Option

DtC = DataConversion()
file = File()
option = Option()

class Entry(Window0):
  def __init__(self):
    self.set_info = []
    # 現在セットの情報
    self.Nset_info = None
    self.Nset_number = None
    self.Nserveteam = None
    self.Nrot_d = {
      "rotation1":0,
      "rotation2":0
    }
    self.Nfrot_number1 = None
    self.Nfrot_number2 = None
    self.Nfrotlist1 = None
    self.Nfrotlist2 = None
    self.Nfsubcondition1 = None
    self.Nfsubcondition2 = None
    self.Nsubcondition1 = None
    self.Nsubcondition2 = None
    self.Nrally_number = 1
    self.Nscore1 = 0
    self.Nscore2 = 0
    self.Nrot_number1 = None
    self.Nrot_number2 = None
    self.Ncalc_rot = None
    self.Nrotcondition1 = None
    self.Nrotcondition2 = None
    self.set_result = []
    self.match_d = []
    self.play_d = []
    self.point_d = []
    self.Nsub_d = []
    self.transition = False
    self.shutdown = False
    pass

  def entry_match_info(self,season:str,tournament:str,date:str,team1:str,team2:str):
    self.season = season
    self.tournament = tournament
    self.date = date
    self.team1 = team1
    self.team2 = team2
    self.match_info = {
      "season":season,
      "tournament":tournament,
      "date":date,
      "team1":team1,
      "team2":team2
    }
    pass

  def open_match_info(self,season:str,tournament:str,date:str,team1:str,team2:str):
    self.season = season
    self.tournament = tournament
    self.date = date
    self.team1 = team1
    self.team2 = team2
    self.match_info = {
      "season":season,
      "tournament":tournament,
      "date":date,
      "team1":team1,
      "team2":team2
    }
    self.match_data_ = file.open_data(self.match_info)
    file.open_index(season,tournament,team1)
    file.open_index(season,tournament,team2)
    self.set_info = self.match_data_["set_info"]
    self.set_result = self.match_data_["set_result"]
    self.match_d = self.match_data_["match_d"]
    pass

  def open_match_info2(self):
    Nset_info = self.set_info[len(self.set_info)-1]
    self.Nset_number = Nset_info["set_number"]
    self.Nserveteam = Nset_info["serveteam"]
    self.Nfrot_number1 = Nset_info["frot_number1"]
    self.Nfrot_number2 = Nset_info["frot_number2"]
    self.Nfrotlist1 = Nset_info["frotlist1"]
    self.Nfrotlist2 = Nset_info["frotlist2"]
    Nset_result = self.set_result[len(self.set_result)-1]
    self.Nscore1 = Nset_result["score1"]
    self.Nscore2 = Nset_result["score2"]
    self.Nfsubcondition1 = Nset_result["fsubcondition1"]
    self.Nfsubcondition2 = Nset_result["fsubcondition2"]
    self.Nsub_d = Nset_result["sub_d"]
    self.play_d = DtC.match2play(self.match_d)
    self.point_d = DtC.play2point(self.play_d)
    self.Nrally_number = self.play_d[len(self.play_d)-1]["Rally"]+1
    pass


  def entry_set_info(self,set_number:str,serveteam:str,frot_number1:str,frot_number2:str,frotlist1:list,frotlist2:list):
    self.Nset_number = int(set_number)
    self.Nserveteam = int(serveteam)
    self.Nfrot_number1 = int(frot_number1)
    self.Nfrot_number2 = int(frot_number2)
    for x in range(0,6):
      int(frotlist1[x])
      int(frotlist2[x])
    self.Nfrotlist1 = [[frotlist1[x],"0"] for x in range(0,6)]
    self.Nfrotlist2 = [[frotlist2[y],"0"] for y in range(0,6)]
    self.Nset_info = {
      "set_number":self.Nset_number,
      "serveteam":self.Nserveteam,
      "frot_number1":self.Nfrot_number1,
      "frot_number2":self.Nfrot_number2,
      "frotlist1":self.Nfrotlist1,
      "frotlist2":self.Nfrotlist2
      }
    self.set_info.append(self.Nset_info)
    self.Nfsubcondition1 = [0,0,0,0,0,0]
    self.Nfsubcondition2 = [0,0,0,0,0,0]
    self.Nsub_d = []
    pass

  def entry_play_data(self,rally_number,play_data):
    play_d_ = {
      "Set":self.Nset_number,
      "Rally":int(rally_number),
      "play_data":play_data
    }
    self.play_d.append(play_d_)
    self.point_d = DtC.play2point(self.play_d)
    self.Nrally_number += 1
    pass

  def complete_set(self):
    set_result_ = {
      "Set":self.Nset_number,
      "score1":self.Nscore1,
      "score2":self.Nscore2,
      "fsubcondition1":self.Nfsubcondition1,
      "fsubcondition2":self.Nfsubcondition2,
      "sub_d":self.Nsub_d
    }
    if (result :=list(filter(lambda d: d["Set"]==self.Nset_number,self.set_result))):
      self.set_result[self.set_result.index(result[0])] = set_result_
    else:
      self.set_result.append(set_result_)

  def search_play_data(self,edit_set_number,edit_rally_number):
    search_play_data = self.play_d[self.play_d.index(list(filter(lambda d: d["Set"] == edit_set_number and d["Rally"]==edit_rally_number,self.play_d))[0])]
    return search_play_data["play_data"]
  
  def edit_play_data(self,edit_set_number,edit_rally_number,edit_play_d_):
    edit_number = self.play_d.index(list(filter(lambda d:d["Set"]==edit_set_number and d["Rally"]==edit_rally_number,self.play_d))[0])
    edit_play_d = {
      "Set":edit_set_number,
      "Rally":edit_rally_number,
      "play_data":edit_play_d_
    }
    self.play_d[edit_number] = edit_play_d
    self.point_d = DtC.play2point(self.play_d)
    pass

  # アップデート : point_dの更新が必要

  def update_score(self):
    score1 = 0
    score2 = 0
    if self.point_d:
      point_d_ = list(filter(lambda d: d["Set"]==self.Nset_number,self.point_d))
      for r_number in range (0,len(point_d_)):
        score1 += point_d_[r_number]["point1"]
        score2 += point_d_[r_number]["point2"]
    self.Nscore1 = score1
    self.Nscore2 = score2
    pass

  def update_serveteam(self,subwindow2):
    if self.point_d:
      if self.point_d[len(self.point_d)-1]["point1"]:
        subwindow2["Serve1"].update(True)
      else:
        subwindow2["Serve2"].update(True)
    else:
      subwindow2[f"Serve{self.Nset_info["serveteam"]}"].update(True)
    pass

  def calc_rotation(self):
    rotation1 = 0
    rotation2 = 0
    if self.point_d:
      point_d_ = list(filter(lambda d:d["Set"]==self.Nset_number,self.point_d))
      for p_number0 in range(0,len(point_d_)):
        rally = point_d_[p_number0]["Rally"]
        if rally==1:
          if self.Nserveteam==1:
            if point_d_[p_number0]["point2"]:
              rotation2 += 1
          else:
            if point_d_[p_number0]["point1"]:
              rotation1 += 1
        else:
          if point_d_[p_number0-1]["point1"]:
            if point_d_[p_number0]["point2"]:
              rotation2 += 1
          else:
            if point_d_[p_number0]["point1"]:
              rotation1 += 1
    self.Nrot_d = {
      "rotation1":rotation1,
      "rotation2":rotation2
    }
    pass

  def update_rot_number(self):
    rot = [6,5,4,3,2,1]
    rNumber01 = rot.index(self.Nfrot_number1)
    rNumber02 = rot.index(self.Nfrot_number2)
    rNumber1 = rNumber01 + self.Nrot_d["rotation1"]
    rNumber2 = rNumber02 + self.Nrot_d["rotation2"]
    self.Nrot_number1 = rot[(rNumber1 + 6)%6]
    self.Nrot_number2 = rot[(rNumber2 + 6)%6]
    pass
  def update_rotation(self):
    self.Nrotlist1 = [self.Nfrotlist1[x-(6-self.Nrot_d["rotation1"]%6)] for x in range(0,6)]
    self.Nrotlist2 = [self.Nfrotlist2[y-(6-self.Nrot_d["rotation2"]%6)] for y in range(0,6)]
    self.Nsubcondition1 = [self.Nfsubcondition1[x-(6-self.Nrot_d["rotation1"]%6)] for x in range(0,6)]
    self.Nsubcondition2 = [self.Nfsubcondition2[y-(6-self.Nrot_d["rotation2"]%6)] for y in range(0,6)]
    pass
  def update_Nrotcondition(self):
    self.Nrotcondition1 = [self.Nrotlist1[x][self.Nsubcondition1[x]] for x in range(0,6)]
    self.Nrotcondition2 = [self.Nrotlist2[y][self.Nsubcondition2[y]] for y in range(0,6)]
    pass


  def entry_update(self,window,subwindow,subwindow2):
    # 更新事項をまとめる
    self.update_score()
    self.update_serveteam(subwindow2)
    self.calc_rotation()
    self.update_rot_number()
    self.update_rotation()
    self.update_Nrotcondition()
    window["Set"].update(self.Nset_number)
    window["Rally"].update(self.Nrally_number)
    subwindow2["Score1"].update(self.Nscore1)
    subwindow2["Score2"].update(self.Nscore2)
    subwindow2["Rot1"].update(self.Nrot_number1)
    subwindow2["Rot2"].update(self.Nrot_number2)
    for i in range(0,6):
      subwindow2[f"Team1S{i+1}"].update(self.Nrotcondition1[i])
      subwindow2[f"Team2S{i+1}"].update(self.Nrotcondition2[i])
    window["play_data"].update("")
    subwindow["-LOGpld-"].update(self.play_d)
    pass

  def main_entry_set(self):
    window = self.Set_Info_window()
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        self.shutdown = True
        break
      elif event == " Enter ":
        try:
          if values["Team1"]:
            serveteam = 1
          elif values["Team2"]:
            serveteam = 2
          self.entry_set_info(values["Set"],serveteam,values["Rot1"],values["Rot2"],[values["Team1S1"],values["Team1S2"],values["Team1S3"],values["Team1S4"],values["Team1S5"],values["Team1S6"]],[values["Team2S1"],values["Team2S2"],values["Team2S3"],values["Team2S4"],values["Team2S5"],values["Team2S6"]])
        except:
          window["msg"].update("Not Created")
          continue
        break
    window.close()
    self.Nrally_number = 1
    pass

  def main_entry_sub(self):
    window = self.substitution_window()
    window["Set"].update(self.Nset_number)
    window["Rally"].update(self.Nrally_number-1)
    rotcondition = [0,self.Nrotcondition1,self.Nrotcondition2]
    frotlist = [0,self.Nfrotlist1,self.Nfrotlist2]
    subcondition = [0,self.Nfsubcondition1,self.Nfsubcondition2]
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        break 
      elif event == "SUB1" or event == "SUB2":
        i = int(event[3:])
        if values[f"In{i}"] in rotcondition[i]:
          return option.notion("Substitution failed","Already in the court")
        if (target := list(filter(lambda d: d[0]==values[f"Out{i}"],frotlist[i]))):
          targetloc = frotlist[i].index(target[0])
          if subcondition[i][targetloc]==0:
            if frotlist[i][targetloc][1] != "0" and frotlist[i][targetloc][1] != values[f"In{i}"]:
              return option.notion("Substitution failed","Dismatch rotationlist")
            subcondition[i][targetloc] = 1
            frotlist[i][targetloc][1] = values[f"In{i}"]
          else:
            if frotlist[i][targetloc][0] != values[f"In{i}"]:
              return option.notion("Substitution failed","Dismatch rotationlist")
            else:
              subcondition[i][targetloc] = 0
        sub_d_ = {
          "Set":values["Set"],
          "Rally":values["Rally"],
          "team":i,
          "Out":values[f"Out{i}"],
          "In":values[f"In{i}"]
        }
        self.Nsub_d.append(sub_d_)
        option.notion("Substitution success","")
        pass
    window.close()

    self.Nfsubcondition1 = subcondition[1] 
    self.Nfsubcondition2 = subcondition[2]
    self.Nfrotlist1 = frotlist[1]
    self.Nfrotlist2 = frotlist[2]
    pass


  def main_entry_main(self):
    subwindow = self.entry_sub(450,100)
    subwindow2 = self.entry_sub2(450,320)
    window = self.entry_main(600,320)
    self.entry_update(window,subwindow,subwindow2)
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        self.shutdown = True
        break
      elif event == " Search ":
        try:
          search_play_data = self.search_play_data(int(values["-Set-"]),int(values["-Rally-"]))
          window["-play_data-"].update(search_play_data)
          window[" Edit "].update(disabled=False)
        except:
          option.notion("Data Not Found","Out of List")
        pass
      elif event == "Submit" or event == " Edit ":
        if event == "Submit":
          self.entry_play_data(values["Rally"],values["play_data"])
          window["Save"].update(disabled=False)
        elif event == " Edit ":
          self.edit_play_data(int(values["-Set-"]),int(values["-Rally-"]),values["-play_data-"])
          window[" Edit "].update(disabled=True)
          window["-play_data-"].update("")
        self.entry_update(window,subwindow,subwindow2)
        pass

      elif event == "SUB":
        self.main_entry_sub()
        self.entry_update(window,subwindow,subwindow2)
        pass
      elif event == "Save":
        self.complete_set()
        file.save_data(self.match_info,self.set_info,self.set_result,self.play_d)
        pass
      elif event == " Exit " or event == " Next ":
        if event == " Exit ":
          self.complete_set()
          self.transition = True
        elif event ==  " Next ":
          self.complete_set()
          self.transition=False
        break
    window.close()
    subwindow.close()
    subwindow2.close()
    pass



class Entry_new(Entry):
  def __init__(self):
    super().__init__()
    pass

  def entry_new_0(self):
    window = self.Info_window()
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        self.shutdown = True
        break
      elif event == "Set":
        self.entry_match_info(values["Season"],values["Tournament"],values["Date"],values["Team1"],values["Team2"])
        window[" Continue "].update(disabled=False)
        try:
          self.player_index1 = file.open_index(self.season,self.tournament,self.team1)
          self.team1_ab = self.player_index1["abbreviation"]
          window["Team1ab"].update(f"Team1 : {self.team1_ab}")
        except:
          self.team1_ab = option.option("Team1 Not Found. New Create Team1","Team1 abbreviation : ")
          if self.team1_ab:
            window["Team1ab"].update(f"Team1 : {self.team1_ab}")
          else:
            window["Team1ab"].update("Not Found")
          pass
        try:
          self.player_index2 = file.open_index(self.season,self.tournament,self.team2)
          self.team2_ab = self.player_index2["abbreviation"]
          window["Team2ab"].update(f"Team2 : {self.team2_ab}")
        except:
          self.team2_ab = option.option("Team2 Not Found. New Create Team2","Team2 abbreviation : ")
          if self.team2_ab:
            window["Team2ab"].update(f"Team2 : {self.team2_ab}")
          else:
            window["Team2ab"].update("Not Found")
          pass
        pass
      elif event == " Continue ":
        break
    window.close()
    pass

  def entry_new_1(self):
    while self.transition==False:
      self.main_entry_set()
      if self.shutdown:
        break
      self.main_entry_main()
    pass

  def exe(self):
    self.entry_new_0()
    if self.shutdown:
      return
    self.entry_new_1()




class Entry_exi(Entry):
  def __init__(self):
    super().__init__()
    pass
  def entry_exi_0(self):
    window = self.Info_window2()
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        self.shutdown = True
        break
      elif event == "Search":
        try:
          self.open_match_info(values["Season"],values["Tournament"],values["Date"],values["Team1"],values["Team2"])
          self.open_match_info2()
          window[" Continue "].update(disabled=False)
          window["FileFound"].update("Data Found !")
          try:
            self.player_index1 = file.open_index(values["Season"],values["Tournament"],values["Team1"])
            self.team1_ab = self.player_index1["abbreviation"]
            window["Team1ab"].update(f"Team1 : {self.team1_ab}")
          except:
            self.team1_ab = option.option("Team1 Not Found. New Create Team1","Team1 abbreviation : ")
            if self.team1_ab:
              window["Team1ab"].update(f"Team1 : {self.team1_ab}")
            else:
              window["Team1ab"].update("Team1 : Not Found")
            pass
          try:
            self.player_index2 = file.open_index(values["Season"],values["Tournament"],values["Team2"])
            self.team2_ab = self.player_index2["abbreviation"]
            window["Team2ab"].update(f"Team2 : {self.team2_ab}")
          except:
            self.team2_ab = option.option("Team2 Not Found. New Create Team2","Team2 abbreviation : ")
            if self.team2_ab:
              window["Team2ab"].update(f"Team2 : {self.team2_ab}")
            else:
              window["Team2ab"].update("Team2 : Not Found")
            pass
        except:
          window[" Continue "].update(disabled=True)
          window["Team1ab"].update("")
          window["Team2ab"].update("")
          window["FileFound"].update("Data Not Found")

        pass
      elif event == " Continue ":
        break
    window.close()
    pass

  def entry_exi_1(self):
    self.main_entry_main()
    while self.transition==False:
      self.main_entry_set()
      if self.shutdown:
        break
      self.main_entry_main()
    pass

  def exe(self):
    self.entry_exi_0()
    if self.shutdown:
      return
    self.entry_exi_1()


class Index(Window0):
  def __init__(self):
    self.season = None
    self.tournament = None
    self.team = None

    self.Nplayer_number = 0
    self.Nplayer_position = None
    self.Nplayer_name = None
    self.player_index = None
    pass

  def edition_index(self):
    window = self.index_window()
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED or event == "Exit":
        break
      elif event == "Search":
        self.player_index = file.open_index(values["season"],values["tournament"],values["team"])
        if self.player_index:
          try:
            self.season = values["season"]
            self.tournament = values["tournament"]
            self.team = values["team"]
            self.team_ab = self.player_index["abbreviation"]
            player_data = self.player_index["player_data"]
            index_content = [[player_data[y]["number"],player_data[y]["position"],player_data[y]["name"]] for y in range(len(player_data))]
            window["index_table"].update(index_content)
            file.set_index(self.season,self.tournament,self.team,self.team_ab)
            window["team_ab"].update(self.team_ab)
          except:
            option.notion("Something Wrong")
        else:
          res = option.check("Team Not Found","New Create ?")
          if res == "OK":
            team_ab = option.option("New Team Abbreviation","Team_ab : ")
            file.create_index(values["season"],values["tournament"],values["team"],team_ab)
            self.season = values["season"]
            self.tournament = values["tournament"]
            self.team = values["team"]
            self.team_ab = team_ab
            file.set_index(self.season,self.tournament,self.team,self.team_ab)
            window["team_ab"].update(self.team_ab)
        pass
      elif event == "Submit":
        try:
          self.Nplayer_number = int(values["player_number"])
          self.Nplayer_position = values["player_position"]
          self.Nplayer_name = values["player_name"]
        except:
          pass
        try:
          file.append_player(self.Nplayer_number,self.Nplayer_position,self.Nplayer_name)
          self.player_index = file.player_index
          player_data = self.player_index["player_data"]
          index_content = [[player_data[y]["number"],player_data[y]["position"],player_data[y]["name"]] for y in range(len(player_data))]
          window["index_table"].update(index_content)
          window["player_number"].update()
          window["player_name"].update()
        except:
          option.notion("Player info failed")
          pass
        pass
      elif event == "Delete":
        delete = player_data[values["index_table"][0]]
        file.delete_player(delete["number"],delete["position"],delete["name"])
        self.player_index = file.player_index
        player_data = self.player_index["player_data"]
        index_content = [[int(player_data[y]["number"]),player_data[y]["position"],player_data[y]["name"]] for y in range(len(player_data))]
        window["index_table"].update(index_content)
        pass
    window.close()
    pass

  def exe(self):
    self.edition_index()
    pass


exi = Entry_exi()
exi.exe()
searchset = None
searchrally = None
list(filter(lambda d:d["Set"]==searchset and d["Rally"]==searchrally,exi.play_d))[0]["play_data"]

# list(filter(lambda d:d["Set"]==searchset and d["Rally"]==searchrally,exi.play_d))[0]["play_data"] = ""
file.save_data(exi.match_info,exi.set_info,exi.set_result,exi.play_d)
DtC.play2command(exi.play_d)

log = DtC.play2log(exi.play_d,exi)
for log_ in log:
  print(log_)