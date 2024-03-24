from _code_ver11_1_1 import vb_plot as vp
from _code_ver11_1_1 import vb_stats as vs

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
    df_MoD["Set"] = play_df["Set"][x]
    df_MoD["Rally"] = play_df["Rally"][x]
    df_PlD = pd.concat([df_PlD,df_MoD])
  df_PlD.reset_index(inplace=True,drop=True)
  return df_PlD

# スコア
def score_data(df,df_Team1,df_Team2,set):
    Score1 = vs.action1(df,df_Team1,set,"","","s","p") + vs.action1(df,df_Team1,set,"","","a","p") + (vs.action2(df,df_Team2,set,"","","a","m") - vs.action1(df,df_Team1,set,"","","b","p")) +vs.action2(df,df_Team2,set,"","","s","m") + vs.action2(df,df_Team2,set,"","","m","")
    Score2 = vs.action2(df,df_Team2,set,"","","s","p") + vs.action2(df,df_Team2,set,"","","a","p") + (vs.action1(df,df_Team1,set,"","","a","m") - vs.action2(df,df_Team2,set,"","","b","p")) + vs.action1(df,df_Team1,set,"","","s","m") + vs.action1(df,df_Team1,set,"","","s","m") + vs.action1(df,df_Team1,set,"","","m","")
    return Score1,Score2

# 入力データからスタッツ表作成

# 入力データから

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

