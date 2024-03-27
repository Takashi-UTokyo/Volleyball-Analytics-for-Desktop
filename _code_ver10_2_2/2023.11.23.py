
# 既存データからのスタッツ作成、視覚化

import numpy as np
import pandas as pd
from itertools import groupby
from pprint import pprint
import matplotlib.pyplot as plt

file_path = r"C:\Volleyball\2023-24 CEV Champions Leauge\2023.11.23 CEV Champions League Piacenza vs Halkbank Fulll Score.xlsx"
Team1 = "ANK"
Team2 = "PIA"



df = pd.read_excel(file_path, sheet_name="Full Score",index_col=None)
df = df.drop(columns=df.columns[range(14,30)])
df
df_Score = pd.concat([df["Set"],df[Team1],df[Team2]],axis=1).dropna()
df_Team1 = df[df.columns[range(2,7)]]
df_Team2 = df[df.columns[range(7,12)]]
df_Rally = df[df.columns[range(0,2)]]

# 各チームのプレーデータフレーム作成
df_Team1 = pd.concat([df_Rally,df_Team1],axis=1)
df_Team2 = pd.concat([df_Rally,df_Team2],axis=1)

# 背番号・アクション・リザルト別にデータから抽出
def action1(number,action,result):
  if result =="all":
    return len(df_Team1[(df_Team1["No."] == number) & (df_Team1["action"] == action)])
  elif result =="effective":
    return len(df_Team1[(df_Team1["No."] == number) & (df_Team1["action"] == action) & ((df["result.1"] == "c")|(df["result.1"] == "o"))])
  elif result == "norm":
    return len(df_Team1[(df_Team1["No."] == number) & (df_Team1["action"] == action) & (df_Team1["result"].isnull())])
  else :
    return len(df_Team1[(df_Team1["No."] == number) & (df_Team1["action"] == action) & (df_Team1["result"] == result)])



# 背番号・アクション別に効果率を計算
def effect1(number,action):

  if action == "s":
    return (action1(number,action,"p")*100+action1(number,action,"effective")*25+action1(number,action,"norm")*0 - action1(number,action,"m")*25)/action1(number,action,"all")
  elif action == "a":
    return (action1(number,action,"p")
             - action1(number,action,"m"))*100 / action1(number,action,"all")
  elif action == "b":
    return (action1(number,action,"p")*100 +action1(number,action,"norm")*50+action1(number,action,"t")*25-action1(number,action,"m")*25)/action1(number,action,"all")
  elif action == "r":
    return (action1(number,action,"a")*100+action1(number,action,"b")*50)/action1(number,action,"all")
  elif action == "d":
    return (action1(number,action,"a")*50+action1(number,action,"b")*50+action1(number,action,"c")*25-action1(number,action,"m")*25-action1(number,action,"o")*25)/action1(number,action,"all")


# 背番号とアクション・リザルトに抽出
def dfaction1(slot,number,action,result):
  if result =="":
    return (df_Team1[(df_Team1["pre"] == slot) & (df_Team1["No."] == number) & (df_Team1["action"] == action)]).reset_index(drop=True)
  else:
    return (df_Team1[(df_Team1["pre"] == slot) & (df_Team1["No."] == number) & (df_Team1["action"] == action) & (df_Team1["result"] == result)]).reset_index(drop=True)

# ゾーンをxy座標に換算
def zone(zone,xory):
  x_mac = str(zone)[:1]
  y_mac = str(zone)[:1]
  x_mic = str(zone)[1:]
  y_mic = str(zone)[1:]
  if x_mac == "2" or x_mac == "9" or x_mac == "1":
    x = 0.5
  elif x_mac == "3"or x_mac =="8"or x_mac =="6":
    x = 3.5
  elif x_mac == "4"or x_mac =="7"or x_mac == "5":
    x = 6.5
  if y_mac == "2"or y_mac == "3"or y_mac =="4":
    y = 0.5
  elif y_mac == "9"or y_mac =="8"or y_mac =="7":
    y = 3.5
  elif y_mac == "1"or y_mac =="6"or y_mac =="5":
    y = 6.5
  if x_mic == "3"or x_mic =="8"or x_mic =="6":
    x = x + 1
  elif x_mic == "4"or x_mic =="7"or x_mic =="5":
    x = x + 2
  if y_mic =="9"or y_mic =="8"or y_mic =="7":
    y = y + 1
  elif y_mic == "1"or y_mic =="6"or y_mic =="5":
    y = y + 2
  if xory =="x":
    return x
  elif xory == "y":
    return y


# 抽出データのゾーンを基にX,Yを計算
dfaction1(2,"a","")
# def df_data(result):
#   df_data = dfaction1(51,2,"a",result).dropna().reset_index(drop=True)
#   df_data["X"] = [zone(df_data.at[i,"zone"],"x") for i in list(range(0,len(df_data)))]
#   df_data["Y"] = [zone(df_data.at[i,"zone"],"y") for i in list(range(0,len(df_data)))]
#   return df_data


# 抽出データをプロットデータに変換
def df_plot1(result):
  def df_data(result):
    df_data = dfaction1(51,2,"a",result).dropna().reset_index(drop=True)
    df_data["X"] = [zone(df_data.at[i,"zone"],"x") for i in list(range(0,len(df_data)))]
    df_data["Y"] = [zone(df_data.at[i,"zone"],"y") for i in list(range(0,len(df_data)))]
    return df_data
  d_plot = []
  for k, g in df_data(result).groupby(["X","Y"]):
    count = len(g)
    d = {
      "X":k[0],
      "Y":k[1],
      "COUNT":count,
    }
    d_plot.append(d)
  df_plot1 = pd.DataFrame(d_plot) 
  return df_plot1

def makeplot():
  df_plot = df_plot1("")
  plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*1000,color="blue")
  df_plot = df_plot1("p")
  plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*100,color="red")
  df_plot = df_plot1("m")
  plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*70,color="white")
  plt.title("Spike Course")
  plt.xlim(0,9)
  plt.ylim(0,9)
  plt.grid(True)
  plt.xticks([1,2,3,4,5,6,7,8,9])
  plt.yticks([1,2,3,4,5,6,7,8,9])
  plt.show()

dfaction1(51,9,"a")
makeplot()