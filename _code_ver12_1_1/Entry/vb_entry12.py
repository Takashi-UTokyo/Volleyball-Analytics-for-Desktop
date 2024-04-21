from _code_ver12_1_1.Function import vb_option as vo
from _code_ver12_1_1.Data import vb_file as vf
from _code_ver12_1_1.Data import vb_data2 as vd2

import PySimpleGUI as sg
import pandas as pd

from _code_ver12_1_1.Data.vb_file12 import File
from _code_ver12_1_1.Function.vb_window12 import Window
from _code_ver12_1_1.Data.vb_data12 import DataConversion

DtC = DataConversion()

class Entry(Window):
  def __init__(self):
    self.set_info = []
    # 現在セットの情報
    self.set_info_ = None
    self.Nset_number = None
    self.Nserveteam = None
    self.Nfrot_number1 = None
    self.Nfrot_number2 = None
    self.Nfrotlist1 = None
    self.Nfrotlist2 = None
    self.Nsubconsition1 = None
    self.Nsubconsition2 = None

    self.set_result = []
    self.play_d = []

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

  def entry_set_info(self,set_number:str,serveteam:str,frot1:str,frot2:str,frotteam1:list,frotteam2:list):
    self.Nset_number = int(set_number)
    self.Nserveteam = int(serveteam)
    self.Nfrot_number1 = int(frot1)
    self.Nfrot_number2 = int(frot2)
    self.Nfrotlist1 = [[frotteam1[x],"0"] for x in range(0,6)]
    self.Nfrotlist2 = [[frotteam2[y],"0"] for y in range(0,6)]
    self.set_info_ = {
      "set_number":self.set_number,
      "serveteam":self.serveteam,
      "frot1":self.Nfrot_number1,
      "frot2":self.Nfrot_number2,
      "frotteam1":self.Nfrotlist1,
      "frotteam2":self.Nfrotlist2
    }
    self.set_info.append(self.set_info_)
    self.Nsubconsition1 = [0,0,0,0,0,0]
    self.Nsubcondition2 = [0,0,0,0,0,0]
  
  def entry_play_data(self,rally_number,play_data):
    play_d_ = {
      "Set":self.Nset_number,
      "Rally":int(rally_number),
      "play_data":play_data
    }
    self.play_d.append(play_d_)
    self.score_d = DtC.play2score(self.play_d)
    self.point_d = DtC.play2point(self.play_d)
    pass

  def complete_set(self):
    set_result_ = {
      "Set":self.set_number,
      "score1":self.score1,
      "score2":self.score2
    }
    self.set_result.append(set_result_)
  
  def edit_play_data(self,edit_set_number,edit_rally_number,edit_play_d_):
    edit_number = self.play_d.index(list(filter(lambda d:d["Set"]==edit_set_number and d["Rally"]==edit_rally_number,self.play_d))[0])
    self.play_d[edit_number] = edit_play_d_

class Entry_new(Entry):
  def __init__(self):
    super().__init__()
    pass

  def entry_new_0(self):
    window = self.Info_window()
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        break
      elif event == "Set":
        self.entry_match_info(values["Season"],values["Tournament"],values["Date"],values["Team1"],values["Team2"])
        window[" Continue "].update(disabled=False)
        file = File()
        try:
          self.player_index1 = file.open_index(self.season,self.tournament,self.team1)
          self.team1_ab = self.player_index1["abbreviation"]
          window["Team1ab"].update(f"Team1 : {self.team1_ab}")
        except:
          self.team1_ab = self.option("Team1 Not Found. New Create Team1","Team1 abbreviation : ")
          if self.team1_ab:
            window["Team1ab"].update(f"Team1 : {self.team1_ab}")
          else:
            window["Team1ab"].update("Not Found")
          pass
        try:
          self.player_index2 = file.open_index(self.season,self.tournament,self.team2)
          self.team2_ab = self.player_index2["abbreaviation"]
          window["Team2ab"].update(f"Team2 : {self.team2_ab}")
        except:
          self.team2_ab = self.option("Team2 Not Found. New Create Team2","Team2 abbreviation : ")
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
    window = self.Set_Info_window()
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
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
    pass

  def entry_new_2(self):
    subwindow = self.entry_sub(450,100)
    subwindow2 = self.entry_sub2(450,320)
    window = self.entry_main(600,320)
    window["Set"].update(self.set_number)
    window["Rally"].update(1)
    subwindow2["Score1"].update(0)
    subwindow2["Score2"].update(0)
    subwindow2[f"Serve{self.set_info_["serveteam"]}"].update(True)
    subwindow2["Rot1"].update(self.set_info_["frot1"])
    subwindow2["Rot2"].update(self.set_info_["frot2"])
    for i in range(0,6):
      subwindow2[f"Team1S{i+1}"].update(self.set_info_["frotteam1"][i])
      subwindow2[f"Team2S{i+1}"].update(self.set_info_["frotteam2"][i])
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        break
      elif event == "Submit":
        self.entry_play_data(values["Rally"],values["play_data"])
        score1 = list(filter(lambda d: d["Set"]==self.set_number,self.score_d))[0]["score1"]
        score2 = list(filter(lambda d: d["Set"]==self.set_number,self.score_d))[0]["score2"]
        subwindow2["Score1"].update(score1)
        subwindow2["Score2"].update(score2)
        if self.point_d[len(self.point_d)-1]["point1"]:
          subwindow2["Serve1"].update(True)
        else:
          subwindow2["Serve2"].update(True)
        pass
      elif event == " Search ":

        pass
    window.close()
    subwindow.close()
    subwindow2.close()

    
      
self = Entry_new()

self.entry_new_0()
self.entry_new_1()
self.entry_new_2()

self.set_info_
self.play_d
self.score_d

DtC.play2command(self.play_d)
DtC.play2trans(self.play_d)
DtC.play2point(self.play_d)

# 1-1新規で入力
if __name__ != "__main__":
  def entry_df():
    Set_Info = []
    Set_Result = []
    Season_path,Tournament_path,date_path,Team1,Team2 = Entry_Info()
    Set = 0
    play_d = []
    df = []
    fRotTeam01,fRotTeam02 = [],[]
    while True:
      Set_Info1,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,fRot1,fRot2 = entry_set(Team1,Team2)
      Set_Info.append(Set_Info1)
      fRotTeam01.append(fRotTeam1)
      fRotTeam02.append(fRotTeam2)
      Set_Result1,play_d,df,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,fRot1,fRot2,boot = entry_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
      Set_Result.append(Set_Result1)
      fRotTeam01[Set] = fRotTeam1
      fRotTeam02[Set] = fRotTeam2
      if boot == True:
        break
      else:
        Set += 1
        pass
    Set
    return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2


  # 1-2取得して入力
  def entry2_df():
    Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2 = entry2_file()
    Set_Result1,play_d,df,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,fRot1,fRot2,boot,event = entry2_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
    Set_Result[Set] = Set_Result1
    fRotTeam01[Set] = fRotTeam1
    fRotTeam02[Set] = fRotTeam2
    if event == " Next ":
      Set += 1
      while True:
        Set_Info1,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,fRot1,fRot2 = entry_set(Team1,Team2)
        Set_Info.append(Set_Info1)
        fRotTeam01.append(fRotTeam1)
        fRotTeam02.append(fRotTeam2)
        Set_Result1,play_d,df,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,fRot1,fRot2,boot = entry_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
        Set_Result.append(Set_Result1)
        fRotTeam01[Set] = fRotTeam1
        fRotTeam02[Set] = fRotTeam2
        if boot == True:
          break
        else:
          Set += 1
          pass

    

    return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2


  # 試合情報入力

  # 
  # セット情報入力
    # スタートローテとメンバーから全ローテ作成

  # データ入力
  # 入力方法  12/s//18;8/r/a/32,11/t//51,1/a/p/65
  def entry_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2):
    data_p,data_p1,data_p2,Team1ab,Team2ab = vf.team_index(Season_path,Tournament_path,Team1,Team2)
    fRotTeam1 = fRotTeam01[Set]
    fRotTeam2 = fRotTeam02[Set]  
    subwindow = entry_sub(450,100)
    subwindow2 = entry_sub2(Team1ab,Team2ab,450,320)
    window = entry_main(600,320)
    window["Set"].update(Set_Info[Set]["Set"])
    window["Rally"].update("1")
    df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
    subwindow["-LOG-"].update(df_content)
    frotation1,frotation2 = [],[]
    if Set_Info[Set]["ServeTeam"] == "1":
      subwindow2["Serve1"].update(True)
    elif Set_Info[Set]["ServeTeam"] == "2":
      subwindow2["Serve2"].update(True)
    for i in range(0,len(sub_condition1)):
      frotation1.append(fRotTeam1[i][sub_condition1[i]])
      frotation2.append(fRotTeam2[i][sub_condition2[i]])
    for i in range(0,6):
      subwindow2[f"Team1S{i+1}"].update(frotation1[i])
      subwindow2[f"Team2S{i+1}"].update(frotation2[i])
    subwindow2["Rot1"].update(fRot1)
    subwindow2["Rot2"].update(fRot2)
    boot = False
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        res = vo.checkWin("Exit","<< Exit ? >>")
        if res == "OK":
          boot = True
          break
        elif res == "NO":
          pass
      elif event == " Exit ":
        res = vo.checkWin("Exit","<< Exit ? >>")
        if res == "OK":
          boot = True
          break
        elif res == "NO":
          pass
      elif event == "Submit":
        try:
          value = {
          "Set":values["Set"],
          "Rally":values["Rally"],
          "Motion":values["Motion"]
          }
          play_d.append(value)      
          df = vd2.makedf_PlD(play_d)
        except:
          vo.error_window("<< Data Cannot Entered >>")
          del(play_d[len(play_d)-1]) 
          pass
        else:
          window["Motion"].update("")
          window["Rally"].update(int(values["Rally"])+1)
          subwindow["-LOGpld-"].update(play_d)
          df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
          subwindow["-LOG-"].update(df_content)
          RotTeam_1,sRot1 = vd2.Rotation(frotation1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
          RotTeam_2,sRot2 = vd2.Rotation(frotation2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
          for i in range(0,6):
            subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
            subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
          subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
          subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
          subwindow2["Rot1"].update(sRot1)
          subwindow2["Rot2"].update(sRot2)
          Team = vd2.score_Team(values["Set"],values["Rally"],df)
          if Team == "Team1":
            subwindow2["Serve1"].update(True)
          elif Team == "Team2":
            subwindow2["Serve2"].update(True)
          window["Save"].update(disabled=False)
        pass
      elif event == "SUB":
        try:
          play_d,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,frotation1,frotation2 = pop_sub(values["Set"],values["Rally"],Team1ab,Team2ab,play_d,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,frotation1,frotation2)
          df = vd2.makedf_PlD(play_d)
          df_content = [[df.iat[y,x] for x in range(0,len(df.columns))] for y in range(0,len(df))]
          subwindow["-LOG-"].update(df_content)
          subwindow["-LOGpld-"].update(play_d)
          RotTeam_1,sRot1 = vd2.Rotation(frotation1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
          RotTeam_2,sRot2 = vd2.Rotation(frotation2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
          for i in range(0,6):
            subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
            subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
          subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
          subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
          subwindow2["Rot1"].update(sRot1)
          subwindow2["Rot2"].update(sRot2)
          pass
        except:
          pass
      elif event == " Search ":
        try:
          search = play_d[play_d.index(list(filter(lambda d : d["Set"]==values["-Set-"] and d["Rally"]==values["-Rally-"] ,play_d))[0])]
          window["-Motion-"].update(search["Motion"])
          window[" Edit "].update(disabled=False)
        except:
          vo.errorWin("<< Motion Not Found >>")  
        pass
      elif event == " Edit ":
        try:
          edition = {
            "Set":values["-Set-"],
            "Rally":values["-Rally-"],
            "Motion":values["-Motion-"]
          }
          play_d[play_d.index(search)] = edition
          subwindow["-LOGpld-"].update(play_d)
          df = vd2.makedf_PlD(play_d)
        except:
          vo.errorWin("<< Data Cannot Entered >>")
          del(play_d[len(play_d)-1])
          pass
        else:
          df.reset_index(drop=True,inplace=True)
          df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
          subwindow["-LOG-"].update(df_content)
          window[" Edit "].update(disabled=True)
          window["-Motion-"].update("")
          RotTeam_1,sRot1 = vd2.Rotation(frotation1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
          RotTeam_2,sRot2 = vd2.Rotation(frotation2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
          for i in range(0,6):
            subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
            subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
          subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
          subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
          subwindow2["Rot1"].update(sRot1)
          subwindow2["Rot2"].update(sRot2)
          Team = vd2.score_Team(values["Set"],str(int(values["Rally"])-1),df)
          if Team == "Team1":
            subwindow2["Serve1"].update(True)
          elif Team == "Team2":
            subwindow2["Serve2"].update(True)
          window["Save"].update(disabled=False)
      elif event == "Save":
        Set_Result1 = {
          "Set":Set_Info[Set]["Set"],
          "Score1":vd2.score_data(Set_Info[Set]["Set"],df)[0],
          "Score2":vd2.score_data(Set_Info[Set]["Set"],df)[1],
        }      
        try:
          Set_Result[Set] = Set_Result1
        except:
          Set_Result.append(Set_Result1)
        fRotTeam01[Set] = fRotTeam1
        fRotTeam02[Set] = fRotTeam2
        vf.filesave(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
        window["Save"].update(disabled=True)
        pass
      elif event == " Next " :
        res = vo.checkWin("<< You try to finish this set >>","<< To Next Set ? >>")
        if res == "OK":
          boot = False
          break
        elif res == "NO":
          pass
    Set_Result1 = {
      "Set":Set_Info[Set]["Set"],
      "Score1":vd2.score_data(values["Set"],df)[0],
      "Score2":vd2.score_data(values["Set"],df)[1],
    }
    window.close()
    subwindow.close()
    subwindow2.close()
    if event == " Next " :
      boot = False
    return Set_Result1,play_d,df,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,fRot1,fRot2,boot

  # 保存データを取得
  def entry2_file():
    window = entry2_searchwindow()
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED or event == " Continue ":
        break
      elif event == " Search ":
        try:
          Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2,msg = vf.fileopen(values["Season"],values["Tournament"],values["Date"],values["Teamf"],values["Teams"])
          data_p,data_p1,data_p2,Team1ab,Team2ab = vf.team_index(Season_path,Tournament_path,Team1,Team2)
          window["reading"].update(msg)
          if msg == "<< FileRead Success! >> :":
            window[" Continue "].update(disabled=False)
            window["Team1"].update(f"Team1 : {Team1}")
            window["Team2"].update(f"Team2 : {Team2}")
            window["Team1ab"].update(f" : {Team1ab}")
            window["Team2ab"].update(f" : {Team2ab}")
        except:
            vo.errorWin("<< File Not Found >>")
            pass
    window.close()
    return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2

  # 保存データに続きから入力
  def entry2_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d1,df1,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2):
    data_p,data_p1,data_p2,Team1ab,Team2ab = vf.team_index(Season_path,Tournament_path,Team1,Team2)
    fRotTeam1 = fRotTeam01[Set]
    fRotTeam2 = fRotTeam02[Set]  
    df = df1
    play_d = play_d1
    subwindow = entry_sub(450,100)
    subwindow2 = entry_sub2(Team1ab,Team2ab,450,320)
    window = entry_main(600,320)
    df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
    df_head = [df.columns.values[z] for z in range(0,len(df.columns))]
    subwindow["-LOG-"].update(df_content)
    subwindow["-LOGpld-"].update(play_d)
    window["Set"].update(df.at[len(df)-1,"Set"])
    window["Rally"].update(df.at[len(df)-1,"Rally"]+1)
    frotation1,frotation2 = [],[]
    for i in range(0,len(sub_condition1)):
      frotation1.append(fRotTeam1[i][sub_condition1[i]])
      frotation2.append(fRotTeam2[i][sub_condition2[i]])
    RotTeam_1,sRot1 = vd2.Rotation(frotation1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],df.at[len(df)-1,"Set"],df.at[len(df)-1,"Rally"],df)[0])
    RotTeam_2,sRot2 = vd2.Rotation(frotation2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],df.at[len(df)-1,"Set"],df.at[len(df)-1,"Rally"],df)[1])
    for i in range(0,6):
      subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
      subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
    subwindow2["Score1"].update(vd2.score_data(df.at[len(df)-1,"Set"],df)[0])
    subwindow2["Score2"].update(vd2.score_data(df.at[len(df)-1,"Set"],df)[1])
    subwindow2["Rot1"].update(sRot1)
    subwindow2["Rot2"].update(sRot2)

    Team = vd2.score_Team(df.at[len(df)-1,"Set"],df.at[len(df)-1,"Rally"],df)
    if Team == "Team1":
      subwindow2["Serve1"].update(True)
    elif Team == "Team2":
      subwindow2["Serve2"].update(True)
    boot = False
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        res = vo.checkWin("Exit","<< Exit ? >>")
        if res == "OK":
          boot = True
          break
        elif res == "NO":
          pass
      elif event == " Exit ":
        res = vo.checkWin("Exit","<< Exit ? >>")
        if res == "OK":
          boot = True
          break
        elif res == "NO":
          pass
      elif event == "Submit":
        try:
          value = {
          "Set":values["Set"],
          "Rally":values["Rally"],
          "Motion":values["Motion"]
          }
          play_d.append(value)
          df = vd2.makedf_PlD(play_d)
        except:
          vo.error_window("<< Data Cannot Entered >>")
          del(play_d[len(play_d)-1])
          pass
        else:
          window["Motion"].update("")
          window["Rally"].update(int(values["Rally"])+1)
          df_content = [[df.iat[y,x] for x in range(0,len(df.columns))] for y in range(0,len(df))]
          subwindow["-LOGpld-"].update(play_d)
          subwindow["-LOG-"].update(df_content)
          frotation1,frotation2 = [],[]
          for i in range(0,len(sub_condition1)):
            frotation1.append(fRotTeam1[i][sub_condition1[i]])
            frotation2.append(fRotTeam2[i][sub_condition2[i]])
          RotTeam_1,sRot1 = vd2.Rotation(frotation1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
          RotTeam_2,sRot2 = vd2.Rotation(frotation2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
          for i in range(0,6):
            subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
            subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
          subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
          subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
          subwindow2["Rot1"].update(sRot1)
          subwindow2["Rot2"].update(sRot2)

          Score1 = vd2.score_data(values["Set"],df)[0]
          Score2= vd2.score_data(values["Set"],df)[1]
          Team = vd2.score_Team(values["Set"],values["Rally"],df)
          if Team == "Team1":
            subwindow2["Serve1"].update(True)
          elif Team == "Team2":
            subwindow2["Serve2"].update(True)
          window["Save"].update(disabled=False)
        pass
      elif event == "SUB":
        try:
          play_d,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,frotation1,frotation2 = pop_sub(values["Set"],values["Rally"],Team1ab,Team2ab,play_d,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,frotation1,frotation2)
          df = vd2.makedf_PlD(play_d)
          df_content = [[df.iat[y,x] for x in range(0,len(df.columns))] for y in range(0,len(df))]
          subwindow["-LOG-"].update(df_content)
          subwindow["-LOGpld-"].update(play_d)
          RotTeam_1,sRot1 = vd2.Rotation(frotation1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
          RotTeam_2,sRot2 = vd2.Rotation(frotation2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
          for i in range(0,6):
            subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
            subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
          subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
          subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
          subwindow2["Rot1"].update(sRot1)
          subwindow2["Rot2"].update(sRot2)
          pass
        except:
          pass      
      elif event == " Search ":
        try:
          search = play_d[play_d.index(list(filter(lambda d : d["Set"]==values["-Set-"] and d["Rally"]==values["-Rally-"] ,play_d))[0])]
          window["-Motion-"].update(search["Motion"])
          window[" Edit "].update(disabled=False)
        except:
          vo.errorWin("<< Motion Not Found >>")  
      elif event == " Edit ":
        try:
          edition = {
            "Set":values["-Set-"],
            "Rally":values["-Rally-"],
            "Motion":values["-Motion-"]
          }
          play_d[play_d.index(search)] = edition
          subwindow["-LOGpld-"].update(play_d)
          df = vd2.makedf_PlD(play_d)
        except:
          vo.errorWin("<< Data Cannot Entered >>")
          del(play_d[len(play_d)-1])
          pass
        else:
          df.reset_index(drop=True,inplace=True)
          df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
          subwindow["-LOG-"].update(df_content)
          window[" Edit "].update(disabled=True)
          window["-Motion-"].update("")
          RotTeam_1,sRot1 = vd2.Rotation(frotation1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
          RotTeam_2,sRot2 = vd2.Rotation(frotation2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
          for i in range(0,6):
            subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
            subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
          subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
          subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
          subwindow2["Rot1"].update(sRot1)
          subwindow2["Rot2"].update(sRot2)
          Team = vd2.score_Team(values["Set"],str(int(values["Rally"])-1),df)
          if Team == "Team1":
            subwindow2["Serve1"].update(True)
          elif Team == "Team2":
            subwindow2["Serve2"].update(True)
          window["Save"].update(disabled=False)
      elif event == "Save":
        try:
          Set_Result1 = {
            "Set":Set_Info[Set]["Set"],
            "Score1":vd2.score_data(values["Set"],df)[0],
            "Score2":vd2.score_data(values["Set"],df)[1],
          }
        except:
          Set_Result1 = {
            "Set":Set_Info[Set]["Set"],
            "Score1":Score1,
            "Score2":Score2,
          }
        Set_Result[Set] = Set_Result1
        fRotTeam01[Set] = fRotTeam1
        fRotTeam02[Set] = fRotTeam2
        vf.filesave(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
        window["Save"].update(disabled=True)
        pass
      elif event == " Next " :
        res = vo.checkWin("<< You try to finish this set >>","<< To Next Set ? >>")
        if res == "OK":
          boot = False
          break
        elif res == "NO":
          pass
    try:
      Set_Result1 = {
        "Set":Set_Info[Set]["Set"],
        "Score1":vd2.score_data(values["Set"],df)[0],
        "Score2":vd2.score_data(values["Set"],df)[1],
      }
    except:
      Set_Result1 = {
        "Set":Set_Info[Set]["Set"],
        "Score1":Score1,
        "Score2":Score2,
      }
    
    window.close()
    subwindow.close()
    subwindow2.close()
    if event == " Next " :
      boot = False
    window.close()
    subwindow.close()
    return Set_Result1,play_d,df,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,fRot1,fRot2,boot,event


  # 機能：交代機能
  def pop_sub(Set,Rally,Team1ab,Team2ab,play_d,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,frotation1,frotation2):
    window = pop_substitute_window(Team1ab,Team2ab)
    window["Set"].update(Set)
    window["Rally"].update(int(Rally)-1)
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        break
      elif event == "SUB1":
        df_frotation1 = pd.DataFrame([[0,1,2,3,4,5]],columns=frotation1)
        fNumber = df_frotation1.at[0,values["Out1"]]
        In1 = int(values["In1"])
        Out1 = str(values["Out1"])
        _sub1 = {
          "Set":values["Set"],
          "Rally":values["Rally"],
          "Motion":f"{In1}/SUB//{Out1}"
        }
        try:
          search = play_d[play_d.index(list(filter(lambda d : d["Set"]==values["Set"] and d["Rally"]==values["Rally"] ,play_d))[0])]
        except:
          vo.errorWin("<< ReEnter ! >>")
          continue
        if sub_condition1[fNumber] == 0:
          if fRotTeam1[fNumber][1] != values["In1"] and fRotTeam1[fNumber][1] != "0":
            res = vo.checkWin("<< Substitution Warning : Mismatch number >>", "You really want to substitute ?")
            if res == "NO":
              continue
          fRotTeam1[fNumber][1] = values["In1"]
          sub_condition1[fNumber] = 1
          play_d1 = []
          for i in range(0,len(play_d)):
            play_d1.append(play_d[i])
            if i == play_d.index(search):
              play_d1.append(_sub1)
          play_d = play_d1
          vo.checkWin("<< Substitution >>","Success !")
        elif sub_condition1[fNumber] == 1:
          if fRotTeam1[fNumber][0] == values["In1"]:
            sub_condition1[fNumber] = 0
            play_d1 = []
            for i in range(0,len(play_d)):
              play_d1.append(play_d[i])
              if i == play_d.index(search):
                play_d1.append(_sub1)
            play_d = play_d1
            vo.checkWin("<< Substitution >>","Success !")
          else:
            res = vo.checkWin("<< Substitution Warning : Mismatch number >>", "You really want to substitute ?")
            if res == "OK":
              fRotTeam1[fNumber][0] = values["In1"]
              sub_condition1[fNumber] = 0
              play_d1 = []
              for i in range(0,len(play_d)):
                play_d1.append(play_d[i])
                if i == play_d.index(search):
                  play_d1.append(_sub1)
              play_d = play_d1
              vo.checkWin("<< Substitution >>","Success !")
        pass
      elif event == "SUB2":
        df_frotation2 = pd.DataFrame([[0,1,2,3,4,5]],columns=frotation2)
        fNumber = df_frotation2.at[0,values["Out2"]]
        In2 = int(values["In2"])
        Out2 = str(values["Out2"])
        _sub2 = {
          "Set":values["Set"],
          "Rally":values["Rally"],
          "Motion":f";{In2}/SUB//{Out2}"
        }
        try:
          search = play_d[play_d.index(list(filter(lambda d : d["Set"]==values["Set"] and d["Rally"]==values["Rally"] ,play_d))[0])]
        except:
          vo.errorWin("<< ReEnter ! >>")
          continue
        if sub_condition2[fNumber] == 0:
          if fRotTeam2[fNumber][1] != values["In2"] and fRotTeam2[fNumber][1] != "0":
            res = vo.checkWin("<< Substitution Warning : Mismatch number >>", "You really want to substitute ?")
            if res == "NO":
              continue
          fRotTeam2[fNumber][1] = values["In2"]
          sub_condition2[fNumber] = 1
          play_d1 = []
          for i in range(0,len(play_d)):
            play_d1.append(play_d[i])
            if i == play_d.index(search):
              play_d1.append(_sub2)
          play_d = play_d1
          vo.checkWin("<< Substitution >>","Success !")
        elif sub_condition2[fNumber] == 1:
          if fRotTeam2[fNumber][0] == values["In2"]:
            sub_condition2[fNumber] = 0
            play_d1 = []
            for i in range(0,len(play_d)):
              play_d1.append(play_d[i])
              if i == play_d.index(search):
                play_d1.append(_sub2)
            play_d = play_d1
            vo.checkWin("<< Substitution >>","Success !")
          else:
            res = vo.checkWin("<< Substitution Warning : Mismatch number >>", "You really want to substitute ?")
            if res == "OK":
              fRotTeam2[fNumber][0] = values["In1"]
              sub_condition1[fNumber] = 0
              play_d1 = []
              for i in range(0,len(play_d)):
                play_d1.append(play_d[i])
                if i == play_d.index(search):
                  play_d1.append(_sub2)
              play_d = play_d1
              vo.checkWin("<< Substitution >>","Success !")
        pass       
      frotation1,frotation2 = [],[]
      for i in range(0,len(sub_condition1)):
        frotation1.append(fRotTeam1[i][sub_condition1[i]])
        frotation2.append(fRotTeam2[i][sub_condition2[i]]) 
    window.close()
    play_d,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,frotation1,frotation2
    return play_d,sub_condition1,sub_condition2,fRotTeam1,fRotTeam2,frotation1,frotation2




  # ウィンドウ

  # 試合情報入力ウィンドウ


  # セット情報入力ウィンドウ

  # 保存データ検索画面
  def entry2_searchwindow(x=None,y=None):
    main_layout = [[sg.Text("Season : "),sg.Input(key="Season")],[sg.Text("Tournament : "),sg.Input(key="Tournament")],[sg.Text("Date : "),sg.Input(key="Date")],[sg.Text("Teamf : "),sg.Input(key="Teamf")],[sg.Text("Teams : "),sg.Input(key="Teams")],[sg.Button(" Search ")],[sg.Button(" Continue ",disabled=True)],[sg.Text(key="reading")],[sg.Text(key="filename")],[sg.Text(key="Team1"),sg.Text(key="Team1ab")],[sg.Text(key="Team2"),sg.Text(key="Team2ab")],[sg.Text(key="index")],[sg.Text(key="pld_Team1")],[sg.Text(key="pld_Team2")]]
    return sg.Window("File Read",main_layout,finalize=True,size=(500,500),location=(x,y))

  # 選手交代機能画面
  def pop_substitute_window(Team1ab,Team2ab,x=None,y=None):
    layout = [
      [sg.Text(f"{Team1ab}"),sg.Text("Set : "),sg.Input(key="Set",size=(2,1)),sg.Text("Rally : "),sg.Input(key="Rally",size=(2,1)),sg.Text(f"{Team2ab}")],
      [sg.Text("Out : No."),sg.Input(key="Out1",size=(2,1)),sg.Text("          "),sg.Text("Out : No."),sg.Input(key="Out2",size=(2,1))],
      [sg.Text("In : No."),sg.Input(key="In1",size=(2,1)),sg.Text("          "),sg.Text("In : No."),sg.Input(key="In2",size=(2,1))],
      [sg.Button("SUB",key="SUB1"),sg.Text("             "),sg.Button("SUB",key="SUB2")]
    ]
    return sg.Window("Substitution Option",layout,finalize=True,size=(300,200),location=(x,y))


