# vb_entryの入力途中の情報取得用

import pandas as pd
import numpy as np


# play_dからdf_Team1,df_Team2の作成
def makedf_MoD12(play_d):
  play_df = pd.DataFrame(play_d)
  PlD1,PlD2 = [],[]
  df_PlD1,df_PlD2 = pd.DataFrame(PlD1),pd.DataFrame(PlD2)
  x = 0
  for x in range(0,len(play_df)):
    motion_d = play_df["Motion"][x].split(",")
    MoD1 = []
    MoD2 = []
    for i in range(0,len(motion_d)):
      if i%2 == 0:
          MoD1.append(motion_d[i])
      elif i%2 == 1:
        MoD2.append(motion_d[i])
    df_MoD1 = pd.DataFrame(MoD1,columns=["Motion1"])
    df_MoD2 = pd.DataFrame(MoD2,columns=["Motion2"])
    i = 6
    for i in range(0,len(df_MoD1)):
      action1 = df_MoD1.at[i,"Motion1"].split("/")
      try:
        pre1 = str(df_MoD1.at[i-1,"Motion1"].split("/")[3])
      except:
        pre1 = np.nan
      try:
        df_MoD1.at[i,"No.1"] = str(action1[0])
      except:
        df_MoD1.at[i,"No.1"] = np.nan
      df_MoD1.at[i,"pre1"] = pre1
      try:
        df_MoD1.at[i,"action1"] = str(action1[1])
      except:
        df_MoD1.at[i,"action1"] = np.nan
      try:
        df_MoD1.at[i,"result1"] = str(action1[2])
      except:
        df_MoD1.at[i,"result1"] = np.nan
      try:
        df_MoD1.at[i,"zone1"] = str(action1[3])
      except:
        df_MoD1.at[i,"zone1"] = np.nan

    for i in range(0,len(df_MoD2)):
      try:
        pre2 = str(df_MoD2.at[i-1,"Motion2"].split("/")[3])
      except:
        pre2 = np.nan
      action2 = df_MoD2.at[i,"Motion2"].split("/")
      try:
        df_MoD2.at[i,"No.2"] = str(action2[0])
      except:
        df_MoD2.at[i,"No.2"] = np.nan
      df_MoD2.at[i,"pre2"] = pre2
      try:
        df_MoD2.at[i,"action2"] = str(action2[1])
      except:
        df_MoD2.at[i,"action2"] = np.nan
      try:
        df_MoD2.at[i,"result2"] = str(action2[2])
      except:
        df_MoD2.at[i,"result2"] = np.nan
      try:
        df_MoD2.at[i,"zone2"] = str(action2[3])
      except:      
        df_MoD2.at[i,"zone2"] = np.nan
    df_MoD1 = pd.concat([play_df["Set"],play_df["Rally"],df_MoD1],axis=1)
    df_MoD2 = pd.concat([play_df["Set"],play_df["Rally"],df_MoD2],axis=1)      
    df_MoD1 = df_MoD1.drop("Motion1",axis=1)
    df_MoD2 = df_MoD2.drop("Motion2",axis=1)
    df_MoD1["Set"] = play_df["Set"][x]
    df_MoD1["Rally"] = play_df["Rally"][x]
    df_MoD2["Set"] = play_df["Set"][x]
    df_MoD2["Rally"] = play_df["Rally"][x]
    df_PlD1 = pd.concat([df_PlD1,df_MoD1])
    df_PlD2 = pd.concat([df_PlD2,df_MoD2])
  df_PlD1.reset_index(drop=True,inplace=True)
  df_PlD2.reset_index(drop=True,inplace=True)
  return df_PlD1,df_PlD2



# 作成play_dからdf作成
def makedf_PlD(play_d):
  play_df = pd.DataFrame(play_d)
  PlD = []
  df_PlD = pd.DataFrame(PlD)

  for x in range(0,len(play_df)):
    motion_d = play_df["Motion"][x].split(",")
    MoD1 = []
    MoD2 = []
    for i in range(0,len(motion_d)):
      if i%2 == 0:
          MoD1.append(motion_d[i])
      elif i%2 == 1:
        MoD2.append(motion_d[i])
    df_MoD1 = pd.DataFrame(MoD1,columns=["Motion1"])
    df_MoD2 = pd.DataFrame(MoD2,columns=["Motion2"])
    for i in range(0,len(df_MoD1)):
      action1 = df_MoD1.at[i,"Motion1"].split("/")
      try:
        pre1 = str(df_MoD1.at[i-1,"Motion1"].split("/")[3])
      except:
        pre1 = np.nan
      try:
        df_MoD1.at[i,"No.1"] = str(action1[0])
      except:
        df_MoD1.at[i,"No.1"] = np.nan
      df_MoD1.at[i,"pre1"] = pre1
      try:
        df_MoD1.at[i,"action1"] = str(action1[1])
      except:
        df_MoD1.at[i,"action1"] = np.nan
      try:
        df_MoD1.at[i,"result1"] = str(action1[2])
      except:
        df_MoD1.at[i,"result1"] = np.nan
      try:
        df_MoD1.at[i,"zone1"] = str(action1[3])
      except:
        df_MoD1.at[i,"zone1"] = np.nan

    for i in range(0,len(df_MoD2)):
      try:
        pre2 = str(df_MoD2.at[i-1,"Motion2"].split("/")[3])
      except:
        pre2 = np.nan
      action2 = df_MoD2.at[i,"Motion2"].split("/")
      try:
        df_MoD2.at[i,"No.2"] = str(action2[0])
      except:
        df_MoD2.at[i,"No.2"] = np.nan
      df_MoD2.at[i,"pre2"] = pre2
      try:
        df_MoD2.at[i,"action2"] = str(action2[1])
      except:
        df_MoD2.at[i,"action2"] = np.nan
      try:
        df_MoD2.at[i,"result2"] = str(action2[2])
      except:
        df_MoD2.at[i,"result2"] = np.nan
      try:
        df_MoD2.at[i,"zone2"] = str(action2[3])
      except:      
        df_MoD2.at[i,"zone2"] = np.nan
    df_MoD = pd.concat([play_df["Set"],play_df["Rally"],df_MoD1,df_MoD2],axis=1)
    df_MoD = df_MoD.drop("Motion1",axis=1).drop("Motion2",axis=1)
    df_MoD["Set"] = play_df["Set"][x]
    df_MoD["Rally"] = play_df["Rally"][x]
    df_PlD = pd.concat([df_PlD,df_MoD])
  df_PlD.reset_index(inplace=True,drop=True)
  pd.set_option("display.max_rows",None)
  pd.set_option("display.max_columns",None)
  return df_PlD

# ローテ指定時の選手の位置…ポジション？
def Position(Number,Rotation) :
  if Rotation == "1":
    return [Number[0],Number[1],Number[2],Number[3],Number[4],Number[5]]
  elif Rotation == "2":
   return [Number[1],Number[2],Number[3],Number[4],Number[5],Number[0]]
  elif Rotation == "3":
    return [Number[2],Number[3],Number[4],Number[5],Number[0],Number[1]]
  elif Rotation == "4":
    return [Number[3],Number[4],Number[5],Number[0],Number[1],Number[2]]
  elif Rotation == "5":
    return [Number[4],Number[5],Number[0],Number[1],Number[2],Number[3]]
  elif Rotation == "6":
    return [Number[5],Number[0],Number[1],Number[2],Number[3],Number[4]]


# ServeTeam = Set_Info[0]["ServeTeam"]
# Rally1 = values["Rally"]
# Set = values["Set"]
# i = 1
# dfから各チームのローテの計算 True or False
def Rot(ServeTeam,Set,Rally1,df):
  bool1,bool2 = 0,0
  
  for i  in range(1,int(Rally1) + 1):
    rally = str(int(i) - 1)
    Rally = str(int(i))
    try:
      prescore1 = len(df[(df["Set"] == Set) & (df["Rally"] == rally)&(df["result1"] == "p")]) + len(df[(df["Set"] == Set) & (df["Rally"] == rally) & (df["result1"] != "p") & (df["result2"] == "m")]) + len(df[(df["Set"] == Set) & (df["Rally"] == rally) & (df["action2"] == "m")])
    except:
      prescore1 = 0
    try:
      prescore2 = len(df[(df["Set"] == Set) & (df["Rally"] == rally) & (df["result2"] == "p")]) + len(df[(df["Set"] == Set) & (df["Rally"] == rally) & (df["result2"] !="p") & (df["result1"] == "m")]) + len(df[(df["Set"] == Set) & (df["Rally"] == rally) & (df["action1"] == "m")])
    except:
      prescore2 = 0
    try:
      score1 = len(df[(df["Set"] == Set) & (df["Rally"] == Rally)&(df["result1"] == "p")]) + len(df[(df["Set"] == Set) & (df["Rally"] == Rally) & (df["result1"] != "p") & (df["result2"] == "m")]) + len(df[(df["Set"] == Set) & (df["Rally"] == Rally) & (df["action2"] == "m")])
    except:
      score1 = 0
    try:
      score2 = len(df[(df["Set"] == Set) & (df["Rally"] == Rally) & (df["result2"] == "p")]) + len(df[(df["Set"] == Set) & (df["Rally"] == Rally) & (df["result2"] !="p") & (df["result1"] == "m")]) + len(df[(df["Set"] == Set) & (df["Rally"] == Rally) & (df["action1"] == "m")])
    except:
      score2 = 0
    if Rally == "1":
      if ServeTeam == "1":
        if score1 == 0 and score2 == 1:
          bool1 += 0
          bool2 += 1
        elif score1 == 1 and score2 == 0:
          bool1 += 0
          bool2 += 0
      elif ServeTeam == "2":
        if score1 == 0 and score2 == 1:
          bool1 += 0
          bool2 += 0
        elif score1 == 1 and score2 == 0:
          bool1 += 1
          bool2 += 0  
    else:
      if prescore1 == 0 and prescore2 == 1:
        if score1 == 0 and score2 == 1:
          bool1 += 0
          bool2 += 0
        elif score1 == 1 and score2 == 0:
          bool1 += 1
          bool2 += 0
      elif prescore1 == 1 and prescore2 == 0:
        if score1 == 0 and score2 == 1:
          bool1 += 0
          bool2 += 1
        elif score1 == 1 and score2 == 0:
          bool1 += 0
          bool2 += 0
  bool1,bool2
  return bool1,bool2


# Number = RotTeam2
# fRotNumber = Rot2
# bool12 = bool2

# 初期ローテ・ローテ番号と ローテ回転回数 = Rot(÷6)から現在のローテを取得
def Rotation(Number,fRotNumber,bool12):
  if (int(bool12)+6)%6 == 0:
    Number1 = [Number[0],Number[1],Number[2],Number[3],Number[4],Number[5]]
  elif (int(bool12)+6)%6 == 1:
    Number1 = [Number[1],Number[2],Number[3],Number[4],Number[5],Number[0]]
  elif (int(bool12)+6)%6 == 2:
    Number1 = [Number[2],Number[3],Number[4],Number[5],Number[0],Number[1]]
  elif (int(bool12)+6)%6 == 3:
    Number1 = [Number[3],Number[4],Number[5],Number[0],Number[1],Number[2]]
  elif (int(bool12)+6)%6 == 4:
    Number1 = [Number[4],Number[5],Number[0],Number[1],Number[2],Number[3]]
  elif (int(bool12)+6)%6 == 5:
    Number1 = [Number[5],Number[0],Number[1],Number[2],Number[3],Number[4]]
  return Number1

# 現在得点の計算
def score_data(Set,df):
  Score1 = len(df[(df["Set"] == Set) & (df["result1"] == "p")]) + len(df[(df["Set"] == Set) & ((df["result1"] != "p") & (df["result2"] == "m"))]) + len(df[(df["Set"] == Set) & (df["action2"] == "m")])
  Score2 = len(df[(df["Set"] == Set) & (df["result2"] == "p")]) + len(df[(df["Set"] == Set) & ((df["result2"] != "p") & (df["result1"] == "m"))]) + len(df[(df["Set"] == Set) & (df["action1"] == "m")])
  return Score1,Score2