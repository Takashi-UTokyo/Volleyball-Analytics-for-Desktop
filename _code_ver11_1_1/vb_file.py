
from _code_ver11_1_1 import vb_option as vo
import pandas as pd
import os  
import PySimpleGUI as sg

# プレイヤーデータの読み込み
def team_index(Season_path,Tournament_path,Team1,Team2):
  try:
    data_p = pd.read_excel(r"C:\Volleyball\Index\Team_index.xlsx", sheet_name=Tournament_path,index_col=None)
  except:
    data_p = pd.DataFrame([])
  try:
    data_p1 = data_p[(data_p["Season"].astype(str)==Season_path) & (data_p["Team"]==Team1)].reset_index(drop=True)
    data_p1["No"] = data_p1["No"].astype(str)
    Team1ab = data_p1.at[0,"Abbreviation"]
  except:
    data_p1 = pd.DataFrame([])
    Team1ab = "<< Not Found>>"
  try:
    data_p2 = data_p[(data_p["Season"].astype(str)==Season_path) & (data_p["Team"]==Team2)].reset_index(drop=True)
    data_p2["No"] = data_p2["No"].astype(str)
    Team2ab = data_p2.at[0,"Abbreviation"]
  except:
    data_p2 = pd.DataFrame([])
    Team2ab = "<< Not Found >>"
  return data_p,data_p1,data_p2,Team1ab,Team2ab


# データ取得
def fileopen(Season,Tournament,Date,Teamf,Teams):
  try:
    Season_path =r"{}".format(Season)
    Tournament_path = r"{}".format(Tournament)
    date_path = r"{}".format(Date)
    Teamf_path = r"{}".format(Teamf)
    Teams_path = r"{}".format(Teams)
    folder_path = Season_path + " " + Tournament_path
    filename_path = date_path +" "+ Teamf_path + " vs " + Teams_path + " " + "Full Scorepy.xlsx"
    path = r"C:\Volleyball"
    file_path = os.path.join(path,folder_path,filename_path)
    df = pd.read_excel(file_path, sheet_name="Full Score",index_col=None)
    df_Info = pd.read_excel(file_path,sheet_name="Info",index_col=None)
    df_play_d = pd.read_excel(file_path,sheet_name="play_d",index_col=None)
    play_d = []
    for i in range(0,len(df_play_d)):
      play_div = {
        'Set':df_play_d.at[i,"Set"],
        'Rally':df_play_d.at[i,"Rally"],
        'Motion':df_play_d.at[i,"Motion"]
      }
      play_d.append(play_div)
    Team1ab = df_Info.columns[1]
    Team2ab = df_Info.columns[2]
    msg = "<< FileRead Success! >> :"
    df_Team1 = df[df.columns[range(2,8)]]
    df_Team2 = df[df.columns[range(8,14)]]
    df_Rally = df[df.columns[range(0,2)]]
    df_Team1 = pd.concat([df_Rally,df_Team1],axis=1)
    df_Team2 = pd.concat([df_Rally,df_Team2],axis=1)
  except:
    msg = "<< FileRead Failed! - RE-ENTER >>"
  try:
    data_p = pd.read_excel(r"C:\Volleyball\Player_index\Player_index.xlsx", sheet_name=Tournament_path,index_col=None)
    index = "<< Player Index Success ! >> "
  except:
    index = "<< Player Index Failed -- Not Found >>"
  try:
    data_p1 = data_p[(data_p["Season"].astype(str)==Season_path) & (data_p["Abbreviation"]==Team1ab)].reset_index(drop=True)
    Team1 = data_p1.at[0,"Team"]
  except:
    Team1 = "<< Not Found >>"
  try:
    data_p2 = data_p[(data_p["Season"]==Season_path) & (data_p["Abbreviation"]==Team2ab)].reset_index(drop=True)
    Team2 = data_p2.at[0,"Team"]
  except:
    Team2 = "<< Not Found>>"
  return Season_path,Tournament_path,date_path,Team1,Team2,play_d,df,df_Team1,df_Team2,msg,index



# 入力データ保存
def filesave(Season_path,Tournament_path,date_path,Team1,Team2,play_d,df):
  data_p,data_p1,data_p2,Team1ab,Team2ab, = vo.team_index(Season_path,Tournament_path,Team1,Team2)
  Set = 1
  Score_Team1 = 0
  Score_Team2 = 0
  try:
    Info = {
      "Set":Set,
      f"{Team1ab}":Score_Team1,
      f"{Team2ab}":Score_Team2,
    }
    df_play_d = pd.DataFrame(play_d)
    df_Info = pd.DataFrame(Info,index=[0])
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
      df_play_d.to_excel(writer,sheet_name="play_d",index=False)     
      df.to_excel(writer,sheet_name="Full Score",index=False)
    vo.optionWin(" File Save Option ","<< File Saved ! >>")
  except:
    vo.errorWin("<< File Cannot Saved >>")




# 検索に関する処理


