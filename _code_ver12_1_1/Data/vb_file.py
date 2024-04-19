
from _code_ver12_1_1.Function import vb_option as vo
import pandas as pd
import os  
import datetime

Season = Season_path = "2023-24"
Tournament = Tournament_path = "Italian Serie A1"
Date = date_path = "2024.3.4"
Teamf = Team1 = "Allianz Milano"
Teams = Team2 = "Sir Safety Susa Vim Perugia"
Team = 'Allianz Milano'

# チームデータの読み込み
def team_index(Season_path,Tournament_path,Team1,Team2):
  try:
    data_p = pd.read_excel(r"C:\Volleyball\Index\Team_index.xlsx", sheet_name=Tournament_path,index_col=None)
  except:
    data_p = pd.DataFrame([])
  try:
    data_p1 = data_p[(data_p["Season"].astype(str)==Season_path) & (data_p["Team"]==Team1)].reset_index(drop=True)
    data_p1["No"] = data_p1["No"].astype(int).astype(str)
    Team1ab = data_p1.at[0,"Abbreviation"]
  except:
    data_p1 = pd.DataFrame([])
    Team1ab = "<< Not Found>>"
  try:
    data_p2 = data_p[(data_p["Season"].astype(str)==Season_path) & (data_p["Team"]==Team2)].reset_index(drop=True)
    data_p2["No"] = data_p2["No"].astype(int).astype(str)
    Team2ab = data_p2.at[0,"Abbreviation"]
  except:
    data_p2 = pd.DataFrame([])
    Team2ab = "<< Not Found >>"
  return data_p,data_p1,data_p2,Team1ab,Team2ab
# データ取得
def fileopen(Season,Tournament,date,Teamf,Teams):
  try:
    Season_path =r"{}".format(Season)
    Tournament_path = r"{}".format(Tournament)
    date_path = r"{}".format(date)
    Teamf_path = r"{}".format(Teamf)
    Teams_path = r"{}".format(Teams)
    folder_path = Season_path + " " + Tournament_path
    filename_path = date_path +" "+ Teamf_path + " vs " + Teams_path + " " + "Full Scorepy.xlsx"
    path = r"C:\Volleyball"
    file_path = os.path.join(path,folder_path,filename_path)
    df = pd.read_excel(file_path, sheet_name="Full Score",index_col=None)
    df_Info = pd.read_excel(file_path,sheet_name="Info",index_col=None)
    Set_Info = []
    for x in range(0,len(df_Info)):
      Set_Info1 = {
        "Set":str(df_Info.at[x,"Set"]),
        "ServeTeam":str(df_Info.at[x,"ServeTeam"]),
        "StartRot1":str(df_Info.at[x,"StartRot1"]),
        "StartRot2":str(df_Info.at[x,"StartRot2"]),
      }
      Set_Info.append(Set_Info1)
    df_Result = pd.read_excel(file_path,sheet_name="Result",index_col=None)
    if not df_Result.empty:
      Team1 = df_Result.columns[2]
      Team2 = df_Result.columns[3]
      df_Result = df_Result.rename(columns={f"{Team1}":"Score1",f"{Team2}":"Score2"})
    Set_Result = []
    for x in range(0,len(df_Result)):
      Set_Result1 = {
        "Set":str(df_Result.at[x,"Set"]),
        "Score1":int(df_Result.at[x,"Score1"]),
        "Score2":int(df_Result.at[x,"Score2"])
      }
      Set_Result.append(Set_Result1)
    Set = len(Set_Result) - 1
    fRot1 = Set_Info[Set]["StartRot1"]
    fRot2 = Set_Info[Set]["StartRot2"]
    df_Rot = pd.read_excel(file_path,sheet_name="Rotation",index_col=0)
    df_Rot = df_Rot.fillna(0).astype(int).astype(str)
    fRotTeam01,fRotTeam02,sub_condition1,sub_condition2 = [],[],[],[]
    for i in range(0,Set+1):
      fRotTeam1,fRotTeam2 = [],[]
      for x in range(1,7):
        fRotTeam1.append([str(df_Rot.at[f"S{x}",f"Team1{i}0"]),str(df_Rot.at[f"S{x}",f"Team1{i}1"])])
        fRotTeam2.append([str(df_Rot.at[f"S{x}",f"Team2{i}0"]),str(df_Rot.at[f"S{x}",f"Team2{i}1"])])
      fRotTeam01.append(fRotTeam1)
      fRotTeam02.append(fRotTeam2)
    for x in range(1,7):
      sub_condition1.append(int(df_Rot.at[f"S{x}","sub_condition1"]))
      sub_condition2.append(int(df_Rot.at[f"S{x}","sub_condition2"]))
    df_play_d = pd.read_excel(file_path,sheet_name="play_d",index_col=None)
    play_d = []
    for i in range(0,len(df_play_d)):
      play_div = {
        'Set':str(df_play_d.at[i,"Set"]),
        'Rally':str(df_play_d.at[i,"Rally"]),
        'Motion':str(df_play_d.at[i,"Motion"]),
      }
      play_d.append(play_div)
    msg = "<< FileRead Success! >> :"
  except:
    vo.optionWin("<<File Read Failed","File Cannot Failed !>>")
  
  return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2,msg


# 入力データ保存
def filesave(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2):
  data_p,data_p1,data_p2,Team1ab,Team2ab = team_index(Season_path,Tournament_path,Team1,Team2)
  
  try:
    df_play_d = pd.DataFrame(play_d)
    df_Info = pd.DataFrame(Set_Info)
    df_Result = pd.DataFrame(Set_Result)
    df_Result = df_Result.rename(columns={"Score1":f"{Team1}","Score2":f"{Team2}"})
    df_Rot01,df_Rot02 = pd.DataFrame([]),pd.DataFrame([])
    for i in range(0,Set+1):
      df_Rot1 = pd.DataFrame(fRotTeam01[i],index=["S1","S2","S3","S4","S5","S6"],columns=[f"Team1{i}0",f"Team1{i}1"])
      df_Rot2 = pd.DataFrame(fRotTeam02[i],index=["S1","S2","S3","S4","S5","S6"],columns=[f"Team2{i}0",f"Team2{i}1"])
      df_Rot01 = pd.concat([df_Rot01,df_Rot1],axis=1)
      df_Rot02 = pd.concat([df_Rot02,df_Rot2],axis=1)
    df_Rot = pd.concat([df_Rot01,df_Rot02],axis=1)
    df_sub1 = pd.DataFrame(sub_condition1,index=["S1","S2","S3","S4","S5","S6"],columns=["sub_condition1"])
    df_sub2 = pd.DataFrame(sub_condition2,index=["S1","S2","S3","S4","S5","S6"],columns=["sub_condition2"])
    df_sub = pd.concat([df_sub1,df_sub2],axis=1)
    df_Rot = pd.concat([df_Rot,df_sub],axis=1)
    Teamsort = [Team1,Team2]
    Teamsort.sort()
    Teamf_path = Teamsort[0]
    Teams_path = Teamsort[1]
    folder_path = Season_path + " " + Tournament_path
    filename_path = date_path + " " + Teamf_path + " vs " + Teams_path + " " + "Full scorepy.xlsx"
    path = r"C:\Volleyball"
    file_path = os.path.join(path,folder_path,filename_path)
  except:
    vo.errorWin("<< Path cannot made >>")
  try:
    with pd.ExcelWriter(file_path) as writer:
      df_Info.to_excel(writer,sheet_name="Info",index=False) 
      df_Result.to_excel(writer,sheet_name="Result",index=True)
      df_play_d.to_excel(writer,sheet_name="play_d",index=False)
      df_Rot.to_excel(writer,sheet_name="Rotation",index=True)     
      df.to_excel(writer,sheet_name="Full Score",index=False)
    vo.optionWin(" File Save Option ","<< File Saved ! >>")
  except:
    vo.errorWin("<< File Cannot Saved >>")

# 入力データの試合情報の保存
def fileInfosave(Season_path,Tournament_path,date_path,Team1,Team2,Set_Result):
  try:
    file_path = r"C:\Volleyball\Index\file_index.xlsx"
    df_data = pd.read_excel(file_path,sheet_name="data")
    Teamsort = [Team1,Team2]
    Teamsort.sort()
    Teamf_path = Teamsort[0]
    Teams_path = Teamsort[1]
    Result = [0,0]
    for result in Set_Result:
      if result["Score1"] > result["Score2"]:
        Result[0] += 1
      elif result["Score2"] > result["Score1"]:
        Result[1] += 1
    if Team1 != Teamf_path:
      Result0,Result1 = Result[0],Result[1]
      Result = [Result1,Result0]
    df_check = df_data[(df_data["Season"] == Season_path) & (df_data["Tournament"] == Tournament_path) & (df_data["date"] == date_path) & (df_data["Teamf"] == Teamf_path) & (df_data["Teams"] == Teams_path)]
    if not df_data.empty:
      if not df_check.empty:
        msg = vo.checkWin("Data Already Made","You Want to Update ?")
        if msg == "NO":
          return vo.optionWin("File Info Not Created","<< Pass File Info >>")
      else:
        msg = "GO"
    dt_now = datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')
  except:
    vo.errorWin("<< Data Cannot Made >>")
  else:
    if msg == "GO":
      try:
        df_file = pd.DataFrame([[Season_path,Tournament_path,date_path,Teamf_path,Teams_path,Result[0],Result[1],dt_now]],columns=df_data.columns)    
        df_data = pd.concat([df_data,df_file],axis=0)
        with pd.ExcelWriter(file_path) as writer:
          df_data.to_excel(writer,sheet_name="data",index=False) 
        vo.optionWin("<< File save Success >>","<< File Saved ! >>")
      except:
        vo.errorWin("<< File Cannot Saved >>")
    elif msg == "OK":
      try:
        df_file = pd.DataFrame([[Season_path,Tournament_path,date_path,Teamf_path,Teams_path,Result[0],Result[1],dt_now]],columns=df_data.columns)    
        df_data.at[df_data[(df_data["Season"]==Season_path) & (df_data["Tournament"] == Tournament_path) & (df_data["date"] == date_path) & (df_data["Teamf"] == Teamf_path) & (df_data["Teams"] == Teams_path)].index[0],"Resultf"] = df_file.at[0,"Resultf"]
        df_data.at[df_data[(df_data["Season"]==Season_path) & (df_data["Tournament"] == Tournament_path) & (df_data["date"] == date_path) & (df_data["Teamf"] == Teamf_path) & (df_data["Teams"] == Teams_path)].index[0],"Results"] = df_file.at[0,"Results"]
        df_data.at[df_data[(df_data["Season"]==Season_path) & (df_data["Tournament"] == Tournament_path) & (df_data["date"] == date_path) & (df_data["Teamf"] == Teamf_path) & (df_data["Teams"] == Teams_path)].index[0],"Edition"] = df_file.at[0,"Edition"]
        with pd.ExcelWriter(file_path) as writer:
          df_data.to_excel(writer,sheet_name="data",index=False) 
        vo.optionWin("<< File save Success >>","<< File Saved ! >>")
      except:
        vo.errorWin("<< File Cannot Saved >>")

# プレイヤーデータの保存
def playerInfosave(Season_path,Tournament_path,date_path,Team1,Team2):
  data_p,data_p1,data_p2,Team1ab,Team2ab = team_index(Season_path,Tournament_path,Team1,Team2)
  
# 検索に関する処理

# プレイヤーデータの読み込み

# チームデータの読み込み
def team_search_option(Team):
  file_data = pd.read_excel(r"C:\Volleyball\Index\file_index.xlsx",sheet_name="data",index_col=None)
  df_search = file_data[(file_data["Teamf"] == Team) | (file_data["Teams"] == Team)].reset_index(drop=True)
  return df_search

def team_search(Team,filelist):
  df_all = pd.DataFrame([])
  for file in filelist:
    Season = file["season"]
    Tournament = file["tournament"]
    date = file["date"]
    Teamf = file["teamf"]
    Teams = file["teams"]
    Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2,msg = fileopen(Season,Tournament,date,Teamf,Teams)
    if Team2 == Team:
      df = df.reindex(columns=["Set","Rally","No.2","pre2","action2","result2","zone2","No.1","action1","result1","zone1"])
      df = df.rename(columns={'No.2':'No.1','pre2':'pre1','action2':'action1','result2':'result1','zone2':'zone1','No.1':'No.2','pre1':'pre2','action1':'action2','result1':'result2','zone1':'zone2'})
    df_all = pd.concat([df_all,df],axis=0)
    df_all.reset_index(drop=True,inplace=True)
  return df_all

# 該当情報から試合ファイルの読み込み
