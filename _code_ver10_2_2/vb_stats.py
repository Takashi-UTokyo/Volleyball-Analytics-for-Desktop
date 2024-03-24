from _code_ver10_2_2 import vb_file as vf
import pandas as pd

df = vf.df
df_Team1 = vf.df_Team1
df_Team2 = vf.df_Team2

data_p1 = vf.data_p1
data_p2 = vf.data_p2


# 個人スタッツdf作成

# チーム別スタッツdf作成

def Tstats1():
  num_div1 = df_Team1["No.1"].unique()
  div1 = []
  div1all = []
  df_div1all = pd.DataFrame(div1all,index=["None"])
  data_p1["No"]
  for i in range(0,len(data_p1)):
    if data_p1["No"][i] in num_div1:
      div1.append(data_p1["No"][i])

  for div in div1:
    stat_div1n = {
      "Name":data_p1.loc[data_p1[data_p1["No"]==div].index.tolist()[0],"Player"],
      "No.":(data_p1.loc[data_p1[data_p1["No"]==div].index.tolist()[0],"No"]),
      "Position":data_p1.loc[data_p1[data_p1["No"]==div].index.tolist()[0],"Position"],
    }
    try:
      stat_div1s = {
        "s-All":action1("","",div,"s",""),
        "s-Point":action1("","",div,"s","p"),
        "s-Effective":action1("","",div,"s","effective"),
        "s-Miss":action1("","",div,"s","m"),
        "s-success":effect1(div,"s"),
      }
    except:
      stat_div1s = {
        "s-All":"NaN",
        "s-Point":"NaN",
        "s-Effective":"NaN",
        "s-Miss":"NaN",
        "s-success":"NaN",
      }

    try:
      stat_div1a = {
        "a-All":action1("","",div,"a",""),
        "a-Point":action1("","",div,"a","p"),
        "a-Effective":action1("","",div,"a","effective"),
        "a-Miss":action1("","",div,"a","m"),
        "a-success":effect1(div,"a"),
      }
    except:
      stat_div1a = {
        "a-All":"NaN",
        "a-Point":"NaN",
        "a-Effective":"NaN",
        "a-Miss":"NaN",
        "a-success":"NaN",
      }
    try:
      stat_div1b = {
        "b-All":action1("","",div,"b",""),
        "b-Point":action1("","",div,"b","p"),
        "b-Effective":action1("","",div,"b","t"),
        "b-Miss":action1("","",div,"a","m"),
        "b-success":effect1(div,"b"),
      }
    except:
      stat_div1b = {
        "b-All":"NaN",
        "b-Point":"NaN",
        "b-Effective":"NaN",
        "b-Miss":"NaN",
        "b-success":"NaN",
      }

    try:
      stat_div1r = {
        "r-All":action1("","",div,"r",""),
        "r-A reception":action1("","",div,"r","a"),
        "r-B reception":action1("","",div,"r","b"),
        "r-Miss":action1("","",div,"r","m"),
        "r-success":effect1(div,"b"),
      }
    except:
      stat_div1r = {
        "r-All":"NaN",
        "r-A reception":"NaN",
        "r-B reception":"NaN",
        "r-Miss":"NaN",
        "r-success":"NaN",
      }

    try:
      stat_div1d = {
        "d-All":action1("","",div,"d",""),
        "d-Miss":action1("","",div,"d","m"),
        "d-success":effect1(div,"d"),
      }
    except:
      stat_div1d = {
        "d-All":"NaN",
        "d-Miss":"NaN",
        "d-success":"NaN",
      }

    try:
      stat_div1m = {
        "m-All":action1("","",div,"m",""),
      }
    except:
      stat_div1m = {
        "m-All":"NaN",
      }



    df_div1n = pd.DataFrame(stat_div1n,index=[0])
    df_div1s = pd.DataFrame(stat_div1s,index =[0])
    df_div1a = pd.DataFrame(stat_div1a,index =[0])
    df_div1b = pd.DataFrame(stat_div1b,index =[0])
    df_div1r = pd.DataFrame(stat_div1r,index =[0])
    df_div1d = pd.DataFrame(stat_div1d,index =[0])
    df_div1m = pd.DataFrame(stat_div1m,index =[0])
    df_div1p = pd.concat([df_div1n,df_div1s,df_div1a,df_div1b,df_div1r,df_div1r,df_div1d,df_div1m],axis=1)
    df_div1all = pd.concat([df_div1all,df_div1p])
  # 最終dfの調整
  df_div1all.drop("None",axis=0,inplace=True)
  df_div1all.reset_index(drop=True,inplace=True)
  df_div1all.index = df_div1all.index + 1
  df_div1all["No."] = df_div1all["No."].astype(int)
  return df_div1all

# ブレイクポイントdf作成


# 背番号・アクション・リザルト別にデータから抽出
# セット・スロット・背番号・アクション・リザルト別に抽出したい

def action1(set,slot,number,action,result):
  if set =="":
    if slot =="":
      if number == "":
        if result == "":
          return len(df_Team1[(df_Team1["action1"] == action)])
        elif result == "effective":
          return len(df_Team1[(df_Team1["action1"] == action)& ((df["result2"] == "c")|(df["result2"] == "o"))])
        else:
          return len(df_Team1[(df_Team1["action1"] == action) & (df_Team1["result1"] == result)])
      else:
        if result == "":
          return len(df_Team1[(df_Team1["No.1"] == number) & (df_Team1["action1"] == action)])
        elif result == "effective":
          return len(df_Team1[(df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))])
        else:
          return len(df_Team1[(df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)])
    else:
      if number == "":
        if result == "":
          return len(df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["action1"] == action)])
        elif result == "effective":
          return len(df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))])
        else:
          return len(df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)])

      else:
        if result == "":
          return len(df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action)])
        elif result =="effective":
          return len(df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))])
        else:
          return len(df_Team1[(df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)])
  else:
    if slot =="":
      if number == "":
        if result == "":
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["action1"] == action)])
        elif result == "effective":
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["action1"] == action)& ((df["result2"] == "c")|(df["result2"] == "o"))])
        else:
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)])
      else:
        if result == "":
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action)])
        elif result == "effective":
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))])
        else:
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)])
    else:
      if number == "":
        if result == "":
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["action1"] == action)])
        elif result == "effective":
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))])
        else:
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)])
      else:
        if result == "":
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action)])
        elif result =="effective":
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & ((df["result2"] == "c")|(df["result2"] == "o"))])        
        else:
          return len(df_Team1[(df_Team1["Set"] == set) & (df_Team1["pre1"] == slot) & (df_Team1["No.1"] == number) & (df_Team1["action1"] == action) & (df_Team1["result1"] == result)])


# 背番号・アクション別に効果率を計算
def effect1(number,action):
  if action == "s":
    return (action1("","",number,action,"p")*100+action1("","",number,action,"effective")*25+action1("","",number,action,"norm")*0 - action1("","",number,action,"m")*25)/action1("","",number,action,"")
  elif action == "a":
    return (action1("","",number,action,"p")
             - action1("","",number,action,"m"))*100 / action1("","",number,action,"")
  elif action == "b":
    return (action1("","",number,action,"p")*100 +action1("","",number,action,"norm")*50+action1("","",number,action,"t")*25-action1("","",number,action,"m")*25)/action1("","",number,action,"")
  elif action == "r":
    return (action1("","",number,action,"a")*100+action1("","",number,action,"b")*50)/action1("","",number,action,"")
  elif action == "d":
    return (action1("","",number,action,"a")*50+action1("","",number,action,"b")*50+action1("","",number,action,"c")*25-action1("","",number,action,"m")*25-action1("","",number,action,"o")*25)/action1("","",number,action,"")

