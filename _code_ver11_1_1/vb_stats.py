from _code_ver11_1_1 import vb_option as vo

import pandas as pd


# 個人スタッツdf作成

# Team1
# チーム別スタッツdf作成
def Tstats1(data_p1,dfa,df_Team1a,set):
  if not set:
    df_Team1 = df_Team1a[df_Team1a["Set"] == set]
    df = dfa[dfa["Set"] == set]
  else:
    df_Team1 = df_Team1a
    df = dfa
  num_div1 = df_Team1["No.1"].unique()
  div1 = []
  div1all = []
  df_div1all = pd.DataFrame(div1all,index=["None"])
  for i in range(0,len(data_p1)):
    if data_p1["No"][i] in num_div1:
      div1.append(data_p1["No"][i])
  for div in div1:
    stat_div1n = {
      "Name":data_p1.loc[data_p1[data_p1["No"]==str(div)].index.tolist()[0],"Player"],
      "No.":(data_p1.loc[data_p1[data_p1["No"]==str(div)].index.tolist()[0],"No"]),
      "Position":data_p1.loc[data_p1[data_p1["No"]==str(div)].index.tolist()[0],"Position"],
    }
    try:
      stat_div1s = {
        "s-All":action1(df,df_Team1,"","",str(div),"s",""),
        "s-Point":action1(df,df_Team1,"","",str(div),"s","p"),
        "s-Effective":action1(df,df_Team1,"","",str(div),"s","effective"),
        "s-Miss":action1(df,df_Team1,"","",str(div),"s","m"),
        "s-success":effect1(df,df_Team1,str(div),"s"),
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
        "a-All":action1(df,df_Team1,"","",str(div),"a",""),
        "a-Point":action1(df,df_Team1,"","",str(div),"a","p"),
        "a-Effective":action1(df,df_Team1,"","",str(div),"a","effective"),
        "a-Miss":action1(df,df_Team1,"","",str(div),"a","m"),
        "a-success":effect1(df,df_Team1,str(div),"a"),
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
        "b-All":action1(df,df_Team1,"","",str(div),"b",""),
        "b-Point":action1(df,df_Team1,"","",str(div),"b","p"),
        "b-Effective":action1(df,df_Team1,"","",str(div),"b","t"),
        "b-Miss":action1(df,df_Team1,"","",str(div),"a","m"),
        "b-success":effect1(df,df_Team1,str(div),"b"),
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
        "r-All":action1(df,df_Team1,"","",str(div),"r",""),
        "r-A reception":action1(df,df_Team1,"","",str(div),"r","a"),
        "r-B reception":action1(df,df_Team1,"","",str(div),"r","b"),
        "r-Miss":action1(df,df_Team1,"","",str(div),"r","m"),
        "r-success":effect1(df,df_Team1,str(div),"b"),
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
        "d-All":action1(df,df_Team1,"","",str(div),"d",""),
        "d-Miss":action1(df,df_Team1,"","",str(div),"d","m"),
        "d-success":effect1(df,df_Team1,str(div),"d"),
      }
    except:
      stat_div1d = {
        "d-All":"NaN",
        "d-Miss":"NaN",
        "d-success":"NaN",
      }

    try:
      stat_div1m = {
        "m-All":action1(df,df_Team1,"","",str(div),"m",""),
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
  return df_div1all

# ローテ別ブレイクポイント数
def bp1(df,rot_number):
  bpS = []
  bpopS = []
  for i in range(1,7):
    try:
      rotS = {
        f"S{i}":len(df[df["action1"] == f"S{i}"].reset_index(drop=True)),
      }
    except:
      rotS = {
        f"S{i}":0,
      }
    try:
      rotopS = {
        f"S{i}":len(df[df["action1"] == f"S{i}"].at[0,"action2"]),
      }
    except:
      rotopS = {
        f"S{i}" :0,
      }
    bpS.append(rotS)
    bpopS.append(rotopS)      
  return bpS[rot_number],bpopS[rot_number]


# 背番号・アクション・リザルト別にデータから抽出

def action1(df,df_Team1,set,slot,number,action,result):
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
def effect1(df,df_Team1,number,action):
  if action == "s":
    return (action1(df,df_Team1,"","",number,action,"p")*100+action1(df,df_Team1,"","",number,action,"effective")*25+action1(df,df_Team1,"","",number,action,"norm")*0 - action1(df,df_Team1,"","",number,action,"m")*25)/action1(df,df_Team1,"","",number,action,"")
  elif action == "a":
    return (action1(df,df_Team1,"","",number,action,"p") - action1(df,df_Team1,"","",number,action,"m"))*100 / action1(df,df_Team1,"","",number,action,"")
  elif action == "b":
    return (action1(df,df_Team1,"","",number,action,"p")*100 +action1(df,df_Team1,"","",number,action,"norm")*50+action1(df,df_Team1,"","",number,action,"t")*25-action1(df,df_Team1,"","",number,action,"m")*25)/action1(df,df_Team1,"","",number,action,"")
  elif action == "r":
    return (action1(df,df_Team1,"","",number,action,"a")*100+action1(df,df_Team1,"","",number,action,"b")*50)/action1(df,df_Team1,"","",number,action,"")
  elif action == "d":
    return (action1(df,df_Team1,"","",number,action,"a")*50+action1(df,df_Team1,"","",number,action,"b")*50+action1(df,df_Team1,"","",number,action,"c")*25-action1(df,df_Team1,"","",number,action,"m")*25-action1(df,df_Team1,"","",number,action,"o")*25)/action1(df,df_Team1,"","",number,action,"")

# Team2
# チーム別スタッツdf作成

# 
def action2(df,df_Team2,set,slot,number,action,result):
  if set == "":
    if slot == "":
      if number == "":
        if result == "":
          return len(df_Team2[df_Team2["action2"] == action])
        elif result == "effective":
          return len(df_Team2[(df_Team2["action2"] == action) & ((df["result1"] == "c")|(df["result1"] == "o"))])
        else:
          return len(df_Team2[(df_Team2["action2"] == action) & (df_Team2["result2"] == result)])
      else:
        if result =="":
          return len(df_Team2[((df_Team2["No.2"] == number) & (df_Team2["action2"] == action))])
        elif result == "effective":
          return len(df_Team2[(df_Team2["No.2"]) & (df_Team2["action2"] == action) & ((df_Team2["result2"] == "c")|(df_Team2["result2"] == "o"))])
        else:
          return len(df_Team2[(df_Team2["No.2"] == number) & (df_Team2["action2"] == action) & (df_Team2["result2"] == result)])
    else:
      if number == "":
        if result == "":
          return len(df_Team2[(df_Team2["pre2"] == slot) & (df_Team2["action2" == number])])
        elif result == "effective":
          return len(df_Team2[(df_Team2["pre2"] == slot) & (df_Team2["No.2"] == number) & ((df_Team2["result2"] == "c")|(df_Team2["result2"] == "o"))])
        else:
          return len(df_Team2[(df_Team2["pre2"] == slot) & (df_Team2["No.2"] == number) & (df_Team2["result"] == result)])
      else:      
        return len(df_Team2[(df_Team2["pre2"] == slot) & (df_Team2["No.2"] == number) & (df_Team2["action2"] == action) & (df_Team2["result"] == result)])
  else:
    if slot == "":
      if number == "":
        if result == "":
          return len(df_Team2[(df_Team2["Set"] == set) & (df_Team2["action2"] == action)])
        elif result == "effective":
          return len(df_Team2[(df_Team2["Set"] == set) & (df_Team2["action2"] == action) & ((df_Team2["result2"] == "c")|(df_Team2["result2"] == "o"))])
        else:
          return len(df_Team2[(df_Team2["Set"] == set) & (df_Team2["action2"] == action) & (df_Team2["result2"] == result)])
      else:
        return len(df_Team2[(df_Team2["Set"] == set) & (df_Team2["No.2"] == number) & (df_Team2["action2"] == action) & (df_Team2["result2"] == result)])
    else:
      return len(df_Team2[(df_Team2["Set"] == set) & (df_Team2["pre2"] == slot) & (df_Team2["No.2"] == number) & (df_Team2["action2"] == action) & (df_Team2["result2"] == result)])


# 効果率

def effect2(df,df_Team2,number,action):
  if action == "s":
    return (action2(df,df_Team2,"","",number,action,"p")*100+action2(df,df_Team2,"","",number,action,"effective")*25+action2(df,df_Team2,"","",number,action,"norm")*0 - action2(df,df_Team2,"","",number,action,"m")*25)/action2(df,df_Team2,"","",number,action,"")
  elif action == "a":
    return (action2(df,df_Team2,"","",number,action,"p") - action2(df,df_Team2,"","",number,action,"m"))*100 / action2(df,df_Team2,"","",number,action,"")
  elif action == "b":
    return (action2(df,df_Team2,"","",number,action,"p")*100 +action2(df,df_Team2,"","",number,action,"norm")*50+action2(df,df_Team2,"","",number,action,"t")*25-action2(df,df_Team2,"","",number,action,"m")*25)/action2(df,df_Team2,"","",number,action,"")
  elif action == "r":
    return (action2(df,df_Team2,"","",number,action,"a")*100+action2(df,df_Team2,"","",number,action,"b")*50)/action2(df,df_Team2,"","",number,action,"")
  elif action == "d":
    return (action2(df,df_Team2,"","",number,action,"a")*50+action2(df,df_Team2,"","",number,action,"b")*50+action2(df,df_Team2,"","",number,action,"c")*25-action2(df,df_Team2,"","",number,action,"m")*25-action2(df,df_Team2,"","",number,action,"o")*25)/action2(df,df_Team2,"","",number,action,"")
