
# 既存データからのスタッツ作成、視覚化
from _code_ver10_2_2 import vb_file as vf
import math
import pandas as pd
import os
from itertools import groupby
import matplotlib.pyplot as plt
# from matplotlib.ticker import MultipleLocater as Ticker


df = vf.df
df_Team1 = vf.df_Team1
df_Team2 = vf.df_Team2
Team1 = vf.Team1
Team2 = vf.Team2
# トスのスロット別割合
def tmakeplot1(set,number):
  ax = plt.axes()
  ax.set_facecolor("navajowhite")
  df_plot = df_td1(set,number,"")
  plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*300,color="blue")
  df_plot = df_td1(set,number,"p")
  plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*300,color="orangered")
  plt.title(f"{set} Setting Distribution    No.:{number}\r\n ALL   Left:{slot1(set,number,1,'')}%    Center:{slot1(set,number,2,'')}%    Right:{slot1(set,number,3,'')}% \r\n POINT   Left:{slot1(set,number,1,'p')}%    Center:{slot1(set,number,2,'p')}%    Right:{slot1(set,number,3,'p')}%")
  plt.legend(["All","Point",])
  plt.xlim(-1,9)
  plt.ylim(-1,9)
  plt.grid(True)
  plt.xticks([3,6,9])
  plt.yticks([3,6,9])
  return plt.show()



# セット・選手・リザルド別にトス配分をX-Y座標に変換
def df_td1(set,number,result):
  tdata01 = []
  slots = df_Team1["pre1"].unique()
  for slot in slots:
    tzone1(slot,"x")
    tzone1(slot,"y")
    tdata = {
      "X":tzone1(slot,"x"),
      "Y":tzone1(slot,"y"),
      "COUNT":len(df_data1(set,slot,number,"a",result)),
    }
    tdata01.append(tdata)
  df_td1 = pd.DataFrame(tdata01,index=None)
  return df_td1



# スロットをトスX-Y座標に変換
def tzone1(slot,xory):
  if str(slot) == "nan":
    return 0
  X = str(slot)[:1]
  Y = str(slot)[1:]
  if X == "5":
    x = 0.5
  elif X == "2":
    x = 3.5
  elif X == "1":
    x = 4.5
  elif X == "a":
    x = 6.5
  elif X == "c":
    x = 8.5
  else:
    x =0
  if Y == "1":
    y = 8.5
  elif Y == "2":
    y = 6.5
  elif Y == "3":
    y = 5
  else:
    y = 0
  if xory == "x":
    return x
  elif xory == "y":
    return y

# レフト・センター・ライトの割合を表示
def slot1(set,number,Side,result):
  if result =='':
    if Side == 1:
      slots = [51,53]
    elif Side == 2:
      slots = [11,21,12,22,"a1","a2"]
    elif Side == 3:
      slots = ["c1","c2","c3"]
    y = 0
    for slot in slots:
      x = len(df_data1(set,slot,number,"a",""))
      y = y + x
  else:
    if Side == 1:
      slots = [51,53]
    elif Side == 2:
      slots = [11,21,12,22,"a1","a2"]
    elif Side == 3:
      slots = ["c1","c2","c3"]
    y = 0
    for slot in slots:
      x = len(df_data1(set,slot,number,"a","p"))
      y = y + x
  return round(y/(len(df_data1(set,"",number,"a","")))*100,1)

# データのプロット
def makeplot1(set,slot,number,action):
  ax = plt.axes()
  ax.set_facecolor("navajowhite")
  if action == "s":
    df_plot = df1_plot1(set,slot,number,"s","")
    plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*500,color="blue",alpha=0.5)
    df_plot = df1_plot1(set,slot,number,"s","effective")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="orange")
    df_plot = df1_plot1(set,slot,number,"s","p")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*100,color="red")
    df_plot = df1_plot1(set,slot,number,"s","m")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*70,color="white")
    plt.title(f"{Team1}:\r\n   {set} Serve Course   No.:{number}")
    plt.legend(["All","Effective","Point","Miss"])
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.grid(True)
    plt.xticks([3,6,9])
    plt.yticks([3,6,9])
    return plt.show()
  if action == "a":
    df_plot = df1_plot1(set,slot,number,"a","")
    plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*300,color="lightblue")
    df_plot = df1_plot1(set,slot,number,"a","effective")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="lightgreen")
    df_plot = df1_plot1(set,slot,number,"a","p")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*100,color="orange")
    df_plot = df1_plot1(set,slot,number,"a","m")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*70,color="white")

    df_plot = df2_plot1(set,slot,number,"a","")
    plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*300,color="blue",alpha=0.5)
    df_plot = df2_plot1(set,slot,number,"a","effective")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="green")
    df_plot = df2_plot1(set,slot,number,"a","p")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*100,color="red")
    df_plot = df2_plot1(set,slot,number,"a","m")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*70,color="white")

    plt.title(f"{Team1}:\r\n   {set} Spike Course      No.:{number} Slot:{slot}")
    plt.legend(["All","Effective","Point","Miss","bt-All","bt-Effective","bt-Point"])
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.grid(True)
    plt.xticks([3,6,9])
    plt.yticks([3,6,9])
    return plt.show()  
  if action == "r":
    df_plot = df1_plot1(set,slot,number,"r","a")
    plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*200,color="yellow")
    df_plot = df1_plot1(set,slot,number,"r","b")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="orange")
    df_plot = df1_plot1(set,slot,number,"r","c")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="red")
    df_plot = df1_plot1(set,slot,number,"r","o")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="lightgreen")
    df_plot = df1_plot1(set,slot,number,"r","m")
    plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="green")
    plt.title(f"{Team1}:\r\n   {set} Reception Course      No.:{number}")
    plt.legend(["A-pass","B-pass","C-pass","O-pass","Miss"])
    plt.xlim(10,0)
    plt.ylim(10,0)
    plt.grid(True)
    plt.xticks([9,6,3])
    plt.yticks([9,6,3])
    return plt.show()


# 抽出データをXYプロットデータに変換(non-block-touch)
def df1_plot1(set,slot,number,action,result):
  d1_plot = []
  ndata = {"X":0,"Y":0,"COUNT":0,}
  df1_plot1 = pd.DataFrame(ndata,index=[0])
  for k, g in df_data1(set,slot,number,action,result).groupby(["X","Y"]):
    count = len(g)
    if int(k[0]) != float(k[0]):
      d1 = {
        "X":k[0],
        "Y":k[1],
        "COUNT":count,
      }
      d1_plot.append(d1)
  df_d1_plot1 = pd.DataFrame(d1_plot) 
  df1_plot1 = pd.concat([df1_plot1,df_d1_plot1])
  return df1_plot1

# 抽出データをXYプロットデータに変換 (block-touch)
def df2_plot1(set,slot,number,action,result):
  d2_plot = []
  ndata = {"X":0,"Y":0,"COUNT":0,}
  df2_plot1 = pd.DataFrame(ndata,index=[0])
  for k, g in df_data1(set,slot,number,action,result).groupby(["X","Y"]):
    count = len(g)
    if int(k[0]) == float(k[0]):
      d2 = {
        "X":k[0],
        "Y":k[1],
        "COUNT":count,
      }
      d2_plot.append(d2)
  df_d2_plot1 = pd.DataFrame(d2_plot) 
  df2_plot1 = pd.concat([df2_plot1,df_d2_plot1])
  return df2_plot1


  # 抽出データのゾーンを基にX,Y列追加

def df_data1(set,slot,number,action,result):
  df_data = dfaction1(set,slot,number,action,result).dropna(subset=["zone1"]).reset_index(drop=True)
  df_data["X"] = [zone(df_data.at[i,"zone1"],"x") for i in list(range(0,len(df_data)))]
  df_data["Y"] = [zone(df_data.at[i,"zone1"],"y") for i in list(range(0,len(df_data)))]
  return df_data

# ゾーンをxy座標に換算
def zone(zone,xory):
  if str(zone) == "nan":
    return 0
  else:
    x_mac = str(zone)[:1]
    y_mac = str(zone)[:1]
    x_mic = str(zone)[1:]
    y_mic = str(zone)[1:]
    if x_mac in ["2","9","1"]:
      x = 1.5
    elif x_mac in ["3","8","6"]:
      x = 4.5
    elif x_mac in ["4","7","5"]:
      x = 7.5
    if y_mac in ["2","3","4"]:
      y = 1.5
    elif y_mac in ["9","8","7"]:
      y = 4.5
    elif y_mac in ["1","6","5"]:
      y = 7.5
    if x_mic in ["2","9","1"]:
      x = x - 1
    elif x_mic in ["4","7","5"]:
      x = x + 1
    elif x_mic == "" :
      x = x + 0.5
    if y_mic in ["2","3","4"]:
      y = y - 1
    elif y_mic in ["1","6","5"]:
      y = y + 1
    elif y_mic == "o":
      y = y + 2
    elif y_mic == "" :
      y = y + 0.5
    if xory =="x":
      return x
    elif xory == "y":
      return y

# セット項目
def dfaction1(set,slot,number,action,result):
  if set =="":
    if slot =="":
      if number == "":
        if result == "":
          return (df_Team1[(df_Team1["action1"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df_Team1[(df_Team1["action1"] == action)& ((df["result2"] == "c")|(df["result2"] == "o"))]).reset_index(drop=True)
        else:
          return (df_Team1[(df_Team1["action1"] == action) & (df_Team1["result1"] == result)]).reset_index(drop=True)
      else:
        if result == "":
          return (df_Team1[(df_Team1["No.1"] == number) & (df_Team1["action1"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df_Team1[(df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))]).reset_index(drop=True)
        else:
          return (df_Team1[(df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)]).reset_index(drop=True)
    else:
      if number == "":
        if result == "":
          return (df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["action1"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))]).reset_index(drop=True)
        else:
          return (df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)]).reset_index(drop=True)

      else:
        if result == "":
          return (df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action)]).reset_index(drop=True)
        elif result =="effective":
          return (df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))]).reset_index(drop=True)        
        else:
          return (df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)]).reset_index(drop=True)
  else:
    if slot =="":
      if number == "":
        if result == "":
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["action1"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["action1"] == action)& ((df["result2"] == "c")|(df["result2"] == "o"))]).reset_index(drop=True)
        else:
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)]).reset_index(drop=True)
      else:
        if result == "":
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))]).reset_index(drop=True)
        else:
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)]).reset_index(drop=True)
    else:
      if number == "":
        if result == "":
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["action1"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))]).reset_index(drop=True)
        else:
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)]).reset_index(drop=True)

      else:
        if result == "":
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action)]).reset_index(drop=True)
        elif result =="effective":
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))]).reset_index(drop=True)        
        else:
          return (df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)]).reset_index(drop=True)







