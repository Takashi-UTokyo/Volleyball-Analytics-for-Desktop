# vb_entryの入力途中の情報取得用

import pandas as pd
import sys

play_d1 = [{"Set":1,"Rally":1,"play_data":"12/s//56;8/r/a/32,11/t//51,1/a//6;2/b/t/87,20/d/a/32,8/t//51,14/a/p/65"}]

motion_d = [
        {"Set":1,"Rally":1,"Transition":1,"Motion":1,"motion_data":"12 sa 56"},
        {"Set":1,"Rally":1,"Transition":2,"Motion":1,"motion_data":"8 ra 32"},
        {"Set":1,"Rally":1,"Transition":2,"Motion":2,"motion_data":"11 tb 51"},
        {"Set":1,"Rally":1,"Transition":2,"Motion":3,"motion_data":"1 aa 51"},
        {"Set":1,"Rally":1,"Transition":3,"Motion":1,"motion_data":"2 bta 56"},
        {"Set":1,"Rally":1,"Transition":3,"Motion":2,"motion_data":"20 da 32"},
        {"Set":1,"Rally":1,"Transition":3,"Motion":3,"motion_data":"8 tb 51"},
        {"Set":1,"Rally":1,"Transition":3,"Motion":4,"motion_data":"14 apa 65"}
        ]

command_d01 = [
        {"Set":1,"Rally":1,"Transition":1,"Motion":1,"No":12,"action":"s","result":"a","zone":56,"point":0},
        {"Set":1,"Rally":1,"Transition":2,"Motion":1,"No":8,"action":"r","result":"a","zone":32,"point":0},
        {"Set":1,"Rally":1,"Transition":2,"Motion":2,"No":11,"action":"t","result":"b","zone":51,"point":0},
        {"Set":1,"Rally":1,"Transition":2,"Motion":3,"No":1,"action":"a","result":"a","zone":51,"point":0},
        {"Set":1,"Rally":1,"Transition":3,"Motion":1,"No":2,"action":"b","result":"ta","zone":87,"point":0},
        {"Set":1,"Rally":1,"Transition":3,"Motion":2,"No":20,"action":"d","result":"a","zone":32,"point":0},
        {"Set":1,"Rally":1,"Transition":3,"Motion":3,"No":8,"action":"t","result":"b","zone":51,"point":0},
        {"Set":1,"Rally":1,"Transition":3,"Motion":4,"No":14,"action":"a","result":"a","zone":65,"point":1}
        ]

command_d02 = [
        {"Set":1,"Rally":1,"Transition":1,"Motion":1,"No":12,"action":"s","result":"a","zone":56},
        {"Set":1,"Rally":1,"Transition":2,"Motion":1,"No":8,"action":"r","result":"a","zone":32},
        {"Set":1,"Rally":1,"Transition":2,"Motion":2,"No":11,"action":"t","result":"b","zone":51},
        {"Set":1,"Rally":1,"Transition":2,"Motion":3,"No":1,"action":"a","result":"a","zone":51},
        {"Set":1,"Rally":1,"Transition":3,"Motion":1,"No":2,"action":"b","result":"ta","zone":87},
        {"Set":1,"Rally":1,"Transition":3,"Motion":2,"No":20,"action":"d","result":"a","zone":32},
        {"Set":1,"Rally":1,"Transition":3,"Motion":3,"No":8,"action":"t","result":"b","zone":51},
        {"Set":1,"Rally":1,"Transition":3,"Motion":4,"No":14,"action":"a","result":"a","zone":65}
        ]


def make_commandd1(play_d1):
  for play_d1_ in play_d1:
    command_d1 = []
    play = play_d1_["play_data"]
    trans = play.split(";")
    for i in range(0,len(trans)):
      motion1 = trans[i].split(",")
      for x in range(0,len(motion1)):
        data = motion1[x].split("/")
        if data[2] and data[2] in "p":
          point = 1
        else:
          point = 0

        play_d3_ = {
          "Set":play_d1_["Set"],
          "Rally":play_d1_["Rally"],
          "Transition":i,
          "Motion":x,
          "No":int(data[0]),
          "action":data[1],
          "result":data[2],
          "zone":data[3],
          "point":point
        }
        
        command_d1.append(play_d3_)
  return command_d1

  
def make_commandd2(play_d1):
  for play_d1_ in play_d1:
    command_d2 = []
    play = play_d1_["play_data"]
    trans = play.split(";")
    for i in range(0,len(trans)):
      motion1 = trans[i].split(",")
      for x in range(0,len(motion1)):
        data = motion1[x].split("/")
        play_d3_ = {
          "Set":play_d1_["Set"],
          "Rally":play_d1_["Rally"],
          "Transition":i,
          "Motion":x,
          "No":int(data[0]),
          "action":data[1],
          "result":data[2],
          "zone":data[3],
        }
        
        command_d2.append(play_d3_)
  return command_d2

if __name__ == "__main__":
  command_d1 = make_commandd1(play_d1)
  command_d2 = make_commandd2(play_d1)
  print(sys.getsizeof(play_d1))
  print(sys.getsizeof(motion_d))
  print(sys.getsizeof(command_d01))
  print(sys.getsizeof(command_d02))
  print(sys.getsizeof(command_d1))
  print(sys.getsizeof(command_d2))
  
      




# アクションごとの得点数表示 → 解析画面に利用

# 得点の推移からローテごとのブレイク計算　→　解析
# トランジットシステム
def makedf_PlD(play_d):
  play_df = pd.DataFrame(play_d)
  df_PlD = pd.DataFrame([])
  for l in range(0,len(play_df)):
    tran_d = play_df["Motion"][l].split(";")
    MoD = [[0,0,0,"0","","","0",0,"0","","","0"]]
    df_MoD = pd.DataFrame(MoD,columns = ["Set","Rally","No.1","pre1","action1","result1","zone1","No.2","pre2","action2","result2","zone2"])
    trans1,trans2 = [],[]
    
    for i in range(0,len(tran_d)):  
    # Team1のtrans
      if i % 2 == 0:
        trans1.append(tran_d[i])
    # Team2のtrans
      elif i % 2 == 1:
        trans2.append(tran_d[i])
    X = len(trans1)
    Y = len(trans2)
    if X > Y:
      Z = X
    else:
      Z = Y
    # z : チェック用
    z = 1
    for z in range(0,Z):
      x = z
      y = z
      try:
        mot1 = trans1[x].split(",")
      except:
        mot1 = ['0/0/0/0']
      if mot1 == ['']:
        mot1 = ['0/0/0/0']
      try:
        mot2 = trans2[y].split(",")
      except:
        mot2 = ['0/0/0/0']
      if mot2 == ['']:
        mot2 = ['0/0/0/0']
      if x == 0:
        m=0
        for i in range(0,len(mot1)):
          action1 = mot1[m].split("/")
          preaction1 = mot1[m-1].split("/")
          for n in range(0,len(action1)):
            if action1[n] == "":
              action1[n] = 0
          df_MoD.at[i,"No.1"] = int(action1[0])
          df_MoD.at[i,"action1"] = str(action1[1])
          df_MoD.at[i,"result1"] = str(action1[2])
          df_MoD.at[i,"zone1"] = str(action1[3])
          m += 1
      else:
        if df_MoD.at[len(df_MoD)-1,"No.1"]==-1:      
          m=0
          for i in range(len(df_MoD)-1,len(df_MoD)-1+len(mot1)):
            action1 = mot1[m].split("/")
            preaction1 = mot1[m-1].split("/")
            for n in range(0,len(action1)):
              if action1[n] == "":
                action1[n] = 0
            df_MoD.at[i,"No.1"] = int(action1[0])
            if action1[1] == "a":
              df_MoD.at[i,"pre1"] = str(preaction1[3])
            df_MoD.at[i,"action1"] = str(action1[1])
            df_MoD.at[i,"result1"] = str(action1[2])
            df_MoD.at[i,"zone1"] = str(action1[3])
            m += 1
        else:    
          m=0
          for i in range(len(df_MoD),len(df_MoD)+len(mot1)):
            action1 = mot1[m].split("/")
            preaction1 = mot1[m-1].split("/")
            for n in range(0,len(action1)):
              if action1[n] == "":
                action1[n] = 0
            df_MoD.at[i,"No.1"] = int(action1[0])
            if action1[1] == "a":
              df_MoD.at[i,"pre1"] = str(preaction1[3])
            df_MoD.at[i,"action1"] = str(action1[1])
            df_MoD.at[i,"result1"] = str(action1[2])
            df_MoD.at[i,"zone1"] = str(action1[3])
            m += 1
      df_MoD[["No.1","No.2"]] = df_MoD[["No.1","No.2"]].fillna(int(0))
      if df_MoD.at[len(df_MoD)-1,"No.2"] == 0:
        df_MoD.at[len(df_MoD)-1,"No.2"] = -1
      if y == 0:
        m=0
        for i in range(0,len(mot2)):
          action2 = mot2[m].split("/")
          preaction2 = mot2[m-1].split("/")
          for n in range(0,len(action2)):
            if action2[n] == "":
              action2[n] = 0
          df_MoD.at[i,"No.2"] = int(action2[0])
          if action2[1] == "a":
            df_MoD.at[i,"pre2"] = str(preaction2[3])
          df_MoD.at[i,"action2"] = str(action2[1])
          df_MoD.at[i,"result2"] = str(action2[2])
          df_MoD.at[i,"zone2"] = str(action2[3])
          m += 1
      else:
        if df_MoD.at[len(df_MoD)-1,"No.2"] == -1:
          m=0
          for i in range(len(df_MoD)-1,len(df_MoD)-1+len(mot2)):
            action2 = mot2[m].split("/")
            preaction2 = mot2[m-1].split("/")
            for n in range(0,len(action2)):
              if action2[n] == "":
                action2[n] = 0
            df_MoD.at[i,"No.2"] = int(action2[0])
            if action2[1] == "a":              
              df_MoD.at[i,"pre2"] = str(preaction2[3])
            df_MoD.at[i,"action2"] = str(action2[1])
            df_MoD.at[i,"result2"] = str(action2[2])
            df_MoD.at[i,"zone2"] = str(action2[3])
            m += 1
        else:
          m=0
          for i in range(len(df_MoD),len(df_MoD)+len(mot2)):
            action2 = mot2[m].split("/")
            preaction2 = mot2[m-1].split("/")
            for n in range(0,len(action2)):
              if action2[n] == "":
                action2[n] = 0
            df_MoD.at[i,"No.2"] = int(action2[0])
            if action2[1] == "a":
              df_MoD.at[i,"pre2"] = str(preaction2[3])
            df_MoD.at[i,"action2"] = str(action2[1])
            df_MoD.at[i,"result2"] = str(action2[2])
            df_MoD.at[i,"zone2"] = str(action2[3])
            m += 1
      df_MoD[["No.1","No.2"]] = df_MoD[["No.1","No.2"]].fillna(int(0))
      if df_MoD.at[len(df_MoD)-1,"No.1"] == 0:
        df_MoD.at[len(df_MoD)-1,"No.1"] = -1
    df_MoD["Set"] = int(play_df["Set"][l])
    df_MoD["Rally"] = int(play_df["Rally"][l])
    df_MoD[["pre1","action1","result1","zone1","pre2","action2","result2","zone2"]] = df_MoD[["pre1","action1","result1","zone1","pre2","action2","result2","zone2"]].fillna("0")
    try:
      df_MoD.at[df_MoD[df_MoD["No.1"] == -1].index[0],"No.1"] = 0
    except:
      pass
    try:
      df_MoD.at[df_MoD[df_MoD["No.2"] == -1].index[0],"No.2"] = 0
    except:
      pass
    df_PlD = pd.concat([df_PlD,df_MoD])
  df_PlD[["No.1","No.2"]] = df_PlD[["No.1","No.2"]].astype(int)
  df_PlD[["pre1","action1","result1","zone1","pre2","action2","result2","zone2"]] = df_PlD[["pre1","action1","result1","zone1","pre2","action2","result2","zone2"]].astype(str)
  pd.set_option('display.width', 100)
  df_PlD.reset_index(inplace=True,drop=True)
  return df_PlD
# 作成play_dからdf_Team1,df_Team2作成
def makedf_MoD12(play_d):
  df_Team1 = makedf_PlD(play_d)[["Set","Rally","No.1","pre1","action1","result1","zone1"]]
  df_Team2 = makedf_PlD(play_d)[["Set","Rally","No.2","pre2","action2","result2","zone2"]]
  return df_Team1,df_Team2


# ローテ指定時の選手の位置…ポジション？　．．．廃止バージョン
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
# Set1 = values["Set"]
# i = 1
# dfから各チームのローテ回転数の計算 
def Rot(ServeTeam,Set1,Rally1,df):
  bool1,bool2 = 0,0
  Set = int(Set1)
  for i  in range(1,int(Rally1) + 1):
    rally = int(i) - 1
    Rally = int(i)
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
    if Rally == 1:
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

def Rotation(frotation,fRot,bool12):
  rot = ["6","5","4","3","2","1"]
  rNumber0 = rot.index(fRot)
  rNumber = rNumber0 + bool12
  sRot = rot[(rNumber+6)%6]
  if (int(bool12)+6)%6 == 0:
    RotTeam_ = [frotation[0],frotation[1],frotation[2],frotation[3],frotation[4],frotation[5]]
  elif (int(bool12)+6)%6 == 1:
    RotTeam_ = [frotation[1],frotation[2],frotation[3],frotation[4],frotation[5],frotation[0]]
  elif (int(bool12)+6)%6 == 2:
    RotTeam_ = [frotation[2],frotation[3],frotation[4],frotation[5],frotation[0],frotation[1]]
  elif (int(bool12)+6)%6 == 3:
    RotTeam_ = [frotation[3],frotation[4],frotation[5],frotation[0],frotation[1],frotation[2]]
  elif (int(bool12)+6)%6 == 4:
    RotTeam_ = [frotation[4],frotation[5],frotation[0],frotation[1],frotation[2],frotation[3]]
  elif (int(bool12)+6)%6 == 5:
    RotTeam_ = [frotation[5],frotation[0],frotation[1],frotation[2],frotation[3],frotation[4]]
  return RotTeam_,sRot


# 現在得点の計算
def score_data(Set1,df):
  Set = int(Set1)
  Score1 = len(df[(df["Set"] == Set) & (df["result1"] == "p")]) + len(df[(df["Set"] == Set) & ((df["result1"] != "p") & (df["result2"] == "m"))]) + len(df[(df["Set"] == Set) & (df["action2"] == "m")])
  Score2 = len(df[(df["Set"] == Set) & (df["result2"] == "p")]) + len(df[(df["Set"] == Set) & ((df["result2"] != "p") & (df["result1"] == "m"))]) + len(df[(df["Set"] == Set) & (df["action1"] == "m")])
  return Score1,Score2

# 最新得点チーム Team1 or Team2
def score_Team(Set1,Rally1,df):
  Set = int(Set1)
  Rally = int(Rally1)
  score1 = len(df[((df["Set"] == Set) & (df["Rally"] == Rally) & (df["result1"] == "p")) | ((df["Set"] == Set) & (df["Rally"] == Rally) & (df["result1"] != "p") & (df["result2"] == "m")) | ((df["Set"] == Set) & (df["Rally"] == Rally) & (df["action2"] == "m"))])
  score2 = len(df[((df["Set"] == Set) & (df["Rally"] == Rally) & (df["result2"] == "p")) | ((df["Set"] == Set) & (df["Rally"] == Rally) & (df["result2"] != "p") & (df["result1"] == "m")) | ((df["Set"] == Set) & (df["Rally"] == Rally) & (df["action1"] == "m"))])
  if score1 == 1 and score2 == 0:
    return "Team1"
  elif score2 == 1 and score1 == 0:
    return "Team2"
    