
# 既存データからのスタッツ作成、視覚化
from _code_ver11_2_1 import vb_option as vo
import pandas as pd
import matplotlib.pyplot as plt

# トスのスロット別割合
def tmakeplot2(df,Team2,set,number):
  try:
    fig,ax = plt.subplots(figsize=(10,10))
    ax.set_facecolor("navajowhite")
    df_plot = df_td2(df,set,number,"")
    ax = plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*300,color="blue")
    df_plot = df_td2(df,set,number,"p")
    ax = plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*300,color="orangered")
    plt.title(f"{Team2} \r\n Set{set} Setting Distribution    No.:{number}\r\n ALL   Left:{slot2(df,set,number,1,'')}%    Center:{slot2(df,set,number,2,'')}%    Right:{slot2(df,set,number,3,'')}% \r\n POINT   Left:{slot2(df,set,number,1,'p')}%    Center:{slot2(df,set,number,2,'p')}%    Right:{slot2(df,set,number,3,'p')}%")
    plt.legend(["All","Point",])
    plt.xlim(-1,9)
    plt.ylim(-1,9)
    plt.grid(True)
    plt.xticks([3,6,9])
    plt.yticks([3,6,9])
    return fig,ax
  except:
    return vo.errorWin("<< Data Not Found >>")
 
# セット・選手・リザルド別にトス配分をX-Y座標に変換
def df_td2(df,set,number,result):
  tdata02 = []
  slots = df["pre2"].unique()
  for slot in slots:
    tzone2(slot,"x")
    tzone2(slot,"y")
    tdata = {
      "X":tzone2(slot,"x"),
      "Y":tzone2(slot,"y"),
      "COUNT":len(df_data2(df,set,slot,number,"a",result)),
    }
    tdata02.append(tdata)
  df_td2 = pd.DataFrame(tdata02,index=None)
  return df_td2



# スロットをトスX-Y座標に変換
def tzone2(slot,xory):
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
def slot2(df,set,number,Side,result):
  if result =='':
    if Side == 1:
      slots = ["51","53"]
    elif Side == 2:
      slots = ["11","21","12","22","a1","a2"]
    elif Side == 3:
      slots = ["c1","c2","c3"]
    y = 0
    for slot in slots:
      x = len(df_data2(df,set,slot,number,"a",""))
      y = y + x
    return round(y/(len(df_data2(df,set,"",number,"a","")))*100,1)
  else:
    if Side == 1:
      slots = ["51","53"]
    elif Side == 2:
      slots = ["11","21","12","22","a1","a2"]
    elif Side == 3:
      slots = ["c1","c2","c3"]
    y = 0
    Z = 0
    for slot in slots:
      x = len(df_data2(df,set,slot,number,"a","p"))
      y = y + x
      z = len(df_data2(df,set,slot,number,"a",""))
      Z = Z + z
    return round(y/Z*100,1)

# データのプロット
def makeplot2(df,Team2,set,slot,number,action):
  try:
    fig,ax = plt.subplots(figsize=(10,10))
    ax.set_facecolor("navajowhite")
    if action == "s":
      df_plot = df1_plot2(df,set,slot,number,"s","")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*500,color="blue",alpha=0.5)
      df_plot = df1_plot2(df,set,slot,number,"s","effective")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="orange")
      df_plot = df1_plot2(df,set,slot,number,"s","p")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*100,color="red")
      df_plot = df1_plot2(df,set,slot,number,"s","m")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*70,color="white")
      plt.title(f"{Team2}:\r\n   Set{set} Serve Course   No.:{number}")
      plt.legend(["All","Effective","Point","Miss"])
      plt.xlim(0,10)
      plt.ylim(0,10)
      plt.grid(True)
      plt.xticks([3,6,9])
      plt.yticks([3,6,9])
      return fig,ax
    if action == "a":
      df_plot = df1_plot2(df,set,slot,number,"a","")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*300,color="lightblue")
      df_plot = df1_plot2(df,set,slot,number,"a","effective")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="lightgreen")
      df_plot = df1_plot2(df,set,slot,number,"a","p")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*100,color="orange")
      df_plot = df1_plot2(df,set,slot,number,"a","m")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*70,color="white")
      df_plot = df2_plot2(df,set,slot,number,"a","")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*300,color="blue",alpha=0.5)
      df_plot = df2_plot2(df,set,slot,number,"a","effective")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="green")
      df_plot = df2_plot2(df,set,slot,number,"a","p")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*100,color="red")
      df_plot = df2_plot2(df,set,slot,number,"a","m")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*70,color="white")

      plt.title(f"{Team2}:\r\n   {set} Spike Course      No.:{number} Slot:{slot}")
      plt.legend(["All","Effective","Point","Miss","bt-All","bt-Effective","bt-Point"])
      plt.xlim(0,10)
      plt.ylim(0,10)
      plt.grid(True)
      plt.xticks([3,6,9])
      plt.yticks([3,6,9])
      return fig,ax  
    if action == "r":
      df_plot = df1_plot2(df,set,slot,number,"r","a")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s = df_plot["COUNT"]*200,color="yellow")
      df_plot = df1_plot2(df,set,slot,number,"r","b")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="orange")
      df_plot = df1_plot2(df,set,slot,number,"r","c")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="red")
      df_plot = df1_plot2(df,set,slot,number,"r","o")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="lightgreen")
      df_plot = df1_plot2(df,set,slot,number,"r","m")
      ax = plt.scatter(df_plot["X"],df_plot["Y"],s=df_plot["COUNT"]*200,color="green")
      plt.title(f"{Team2}:\r\n   {set} Reception Course      No.:{number}")
      plt.legend(["A-pass","B-pass","C-pass","O-pass","Miss"])
      plt.xlim(10,0)
      plt.ylim(10,0)
      plt.grid(True)
      plt.xticks([9,6,3])
      plt.yticks([9,6,3])
      return fig,ax
  except:
    return vo.errorWin("<< Data Not Found >>")


# 抽出データをXYプロットデータに変換(non-block-touch)
def df1_plot2(df,set,slot,number,action,result):
  d1_plot = []
  ndata = {"X":0,"Y":0,"COUNT":0,}
  df1_plot2 = pd.DataFrame(ndata,index=[0])
  for k, g in df_data2(df,set,slot,number,action,result).groupby(["X","Y"]):
    count = len(g)
    if int(k[0]) != float(k[0]):
      d1 = {
        "X":k[0],
        "Y":k[1],
        "COUNT":count,
      }
      d1_plot.append(d1)
  df_d1_plot2 = pd.DataFrame(d1_plot) 
  df1_plot2 = pd.concat([df1_plot2,df_d1_plot2])
  return df1_plot2

# 抽出データをXYプロットデータに変換 (block-touch)
def df2_plot2(df,set,slot,number,action,result):
  d2_plot = []
  ndata = {"X":0,"Y":0,"COUNT":0,}
  df2_plot2 = pd.DataFrame(ndata,index=[0])
  for k, g in df_data2(df,set,slot,number,action,result).groupby(["X","Y"]):
    count = len(g)
    if int(k[0]) == float(k[0]):
      d2 = {
        "X":k[0],
        "Y":k[1],
        "COUNT":count,
      }
      d2_plot.append(d2)
  df_d2_plot2 = pd.DataFrame(d2_plot) 
  df2_plot2 = pd.concat([df2_plot2,df_d2_plot2])
  return df2_plot2


  # 抽出データのゾーンを基にX,Y列追加

# 抽出データにx-y座標を追加
def df_data2(df,set,slot,number,action,result):
  df_data = dfaction2(df,set,slot,number,action,result).dropna(subset=["zone2"]).reset_index(drop=True)
  df_data["X"] = [zone(df_data.at[i,"zone2"],"x") for i in list(range(0,len(df_data)))]
  df_data["Y"] = [zone(df_data.at[i,"zone2"],"y") for i in list(range(0,len(df_data)))]
  return df_data

# ゾーンをxy座標に換算
def zone(zone,xory):
  if not str(zone):
    return 0
  elif str(zone)=="0":
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

def dfaction2(df,set,slot,number,action,result):
  if set =="":
    if slot =="":
      if number == "":
        if result == "":
          return (df[(df["action2"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df[(df["action2"] == action)& (df["result1"].isin(["c","o"]))]).reset_index(drop=True)
        else:
          return (df[(df["action2"] == action) & (df["result2"] == result)]).reset_index(drop=True)
      else:
        if result == "":
          return (df[(df["No.2"] == number) & (df["action2"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df[(df["No.2"] == number) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))]).reset_index(drop=True)
        else:
          return (df[(df["No.2"] == number) & (df["action2"] == action) & (df["result2"] == result)]).reset_index(drop=True)
    else:
      if number == "":
        if result == "":
          return (df[(df["pre2"] == slot) & (df["action2"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df[(df["pre2"] == slot) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))]).reset_index(drop=True)
        else:
          return (df[(df["pre2"] == slot) & (df["action2"] == action) & (df["result2"] == result)]).reset_index(drop=True)
      else:
        if result == "":
          return (df[(df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df[(df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))]).reset_index(drop=True)
        else:
          return (df[(df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action) & (df["result2"] == result)]).reset_index(drop=True)
  else:
    if slot == "":
      if number == "":
        if result == "":
          return (df[(df["Set"] == set) & (df["action2"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df[(df["Set"] == set) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))]).reset_index(drop=True)
        else:
          return (df[(df["Set"] == set) & (df["action2"] == action) & (df["result2"] == result)]).reset_index(drop=True)
      else:
        if result == "":
          return (df[(df["Set"] == set) & (df["No.2"] == number) & (df["action2"] == action)]).reset_index(drop=True)
        elif result =="effective":
          return (df[(df["Set"] == set) & (df["No.2"] == number) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))]).reset_index(drop=True)        
        else:
          return (df[(df["Set"] == set) & (df["No.2"] == number) & (df["action2"] == action) & (df["result2"] == result)]).reset_index(drop=True)
    else:
      if number == "":
        if result == "":
          return (df[(df["Set"] == set) & (df["pre2"] == slot) & (df["action2"] == action)]).reset_index(drop=True)
        elif result == "effective":
          return (df[(df["Set"] == set) & (df["pre2"] == slot) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))]).reset_index(drop=True)
        else:
          return (df[(df["Set"] == set) & (df["pre2"] == slot) & (df["action2"] == action) & (df["result2"] == result)]).reset_index(drop=True)
      else:
        if result == "":
          return (df[(df["Set"] == set) & (df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action)]).reset_index(drop=True)
        elif result =="effective":
          return (df[(df["Set"] == set) & (df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))]).reset_index(drop=True)        
        else:
          return (df[(df["Set"] == set) & (df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action) & (df["result2"] == result)]).reset_index(drop=True)







