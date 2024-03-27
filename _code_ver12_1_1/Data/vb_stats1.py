from _code_ver12_1_1 import vb_option as vo

import pandas as pd
import numpy as np

# 個人スタッツdf作成
# Team1
# チーム別スタッツdf作成

def Tstats1(data_p1,dfa,set):
  if set:
    df = dfa[dfa["Set"] == set]
  else:
    df = dfa
  num_div1 = df["No.1"].unique()
  div1 = []
  div1all = []
  df_div1all = pd.DataFrame(div1all,index=["None"])
  for i in range(0,len(data_p1)):
    if int(data_p1["No"][i]) in num_div1:
      div1.append(data_p1["No"][i])
  for div in div1:
    stat_div1n = {
      "Name":data_p1.loc[data_p1[data_p1["No"]==str(div)].index.tolist()[0],"Player"],
      "No.":(data_p1.loc[data_p1[data_p1["No"]==str(div)].index.tolist()[0],"No"]),
      "Position":data_p1.loc[data_p1[data_p1["No"]==str(div)].index.tolist()[0],"Position"],
    }
    try:
      stat_div1s = {
        "s-All":action1(df,"","",int(div),"s",""),
        "s-Point":action1(df,"","",int(div),"s","p"),
        "s-Effective":action1(df,"","",int(div),"s","effective"),
        "s-Miss":action1(df,"","",int(div),"s","m"),
        "s-success":effect1(df,int(div),"s"),
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
        "a-All":action1(df,"","",int(div),"a",""),
        "a-Point":action1(df,"","",int(div),"a","p"),
        "a-Effective":action1(df,"","",int(div),"a","effective"),
        "a-Miss":action1(df,"","",int(div),"a","m"),
        "a-success":effect1(df,int(div),"a"),
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
        "b-All":action1(df,"","",int(div),"b",""),
        "b-Point":action1(df,"","",int(div),"b","p"),
        "b-Effective":action1(df,"","",int(div),"b","t"),
        "b-Miss":action1(df,"","",int(div),"a","m"),
        "b-success":effect1(df,int(div),"b"),
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
        "r-All":action1(df,"","",int(div),"r",""),
        "r-A":action1(df,"","",int(div),"r","a"),
        "r-B":action1(df,"","",int(div),"r","b"),
        "r-Miss":action1(df,"","",int(div),"r","m"),
        "r-success":effect1(df,int(div),"r"),
      }
    except:
      stat_div1r = {
        "r-All":"NaN",
        "r-A":"NaN",
        "r-B":"NaN",
        "r-Miss":"NaN",
        "r-success":"NaN",
      }

    try:
      stat_div1d = {
        "d-All":action1(df,"","",int(div),"d",""),
        "d-Miss":action1(df,"","",int(div),"d","m"),
        "d-success":effect1(df,int(div),"d"),
      }
    except:
      stat_div1d = {
        "d-All":"NaN",
        "d-Miss":"NaN",
        "d-success":"NaN",
      }

    try:
      stat_div1m = {
        "m-All":action1(df,"","",int(div),"m",""),
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
    df_div1p = pd.concat([df_div1n,df_div1s,df_div1a,df_div1b,df_div1r,df_div1d,df_div1m],axis=1)
    # df_div1p = df_div1p.reset_index()
    df_div1all = pd.concat([df_div1all,df_div1p],axis=0)
  # 最終dfの調整
  df_div1all.drop("None",axis=0,inplace=True)
  df_div1all.reset_index(drop=True,inplace=True)
  df_div1all.index = df_div1all.index + 1
  stat_t1n = {
    "Name":"All",
    "No.":"NaN",
    "Position":"NaN"
  }
  stat_t1s = {
    "s-All":action1(df,"","","","s",""),
    "s-Point":action1(df,"","","","s","p"),
    "s-Effective":action1(df,"","","","s","effective"),
    "s-Miss":action1(df,"","","","s","m"),
    "s-success":effect1(df,"","s")
  }
  stat_t1a = {
    "a-All":action1(df,"","","","a",""),
    "a-Point":action1(df,"","","","a","p"),
    "a-Effective":action1(df,"","","","a","effective"),
    "a-Miss":action1(df,"","","","a","m"),
    "a-success":effect1(df,"","a")
  }
  stat_t1b = {
    "b-All":action1(df,"","","","b",""),
    "b-Point":action1(df,"","","","b","p"),
    "b-Effective":action1(df,"","","","b","t"),
    "b-Miss":action1(df,"","","","b","m"),
    "b-success":effect1(df,"","b")
  }
  stat_t1r = {
    "r-All":action1(df,"","","","r",""),
    "r-A":action1(df,"","","","r","a"),
    "r-B":action1(df,"","","","r","b"),
    "r-Miss":action1(df,"","","","r","m"),
    "r-success":effect1(df,"","r"),
  }
  stat_t1d = {
    "d-All":action1(df,"","","","d",""),
    "d-Miss":action1(df,"","","","d","m"),
    "d-success":effect1(df,"","d")
  }
  stat_t1m = {
    "m-All":action1(df,"","","","m","")
  }
  df_t1n = pd.DataFrame(stat_t1n,index=[0])
  df_t1s = pd.DataFrame(stat_t1s,index=[0])
  df_t1a = pd.DataFrame(stat_t1a,index=[0])
  df_t1b = pd.DataFrame(stat_t1b,index=[0])
  df_t1r = pd.DataFrame(stat_t1r,index=[0])
  df_t1d = pd.DataFrame(stat_t1d,index=[0])
  df_t1m = pd.DataFrame(stat_t1m,index=[0])
  df_t1 = pd.concat([df_t1n,df_t1s,df_t1a,df_t1b,df_t1r,df_t1d,df_t1m],axis=1)
  df_Tstats1 = pd.concat([df_div1all,df_t1],axis=0)  
  return df_Tstats1

# ローテ別ブレイクポイント数 ->廃バージョン
# def bp1(df,rot_number):
#   bpS = []
#   bpopS = []
#   for i in range(1,7):
#     try:
#       rotS = {
#         f"S{i}":len(df[df["action1"] == f"S{i}"].reset_index(drop=True)),
#       }
#     except:
#       rotS = {
#         f"S{i}":0,
#       }
#     try:
#       rotopS = {
#         f"S{i}":len(df[df["action1"] == f"S{i}"].at[0,"action2"]),
#       }
#     except:
#       rotopS = {
#         f"S{i}" :0,
#       }
#     bpS.append(rotS)
#     bpopS.append(rotopS)      
#   return bpS[rot_number],bpopS[rot_number]


# サーブの選手番号から現在のローテーションを逆算　→dfのserve連続値からブレイクの計測
Set1 = "1"
def bp1(Set1,df,fRotTeam01,Set_Info):
  if Set1 == "All":
    serve01 = df[df["action1"] == "s"].reset_index(drop=True)
    bp1 = []
    for m in range(1,len(Set_Info)+1):
      serve1 = serve01[serve01["Set"] == m].reset_index(drop=True)
      fRotTeam1 = fRotTeam01[m-1]
      df_fRotTeam1 = pd.DataFrame(fRotTeam1,columns=["sub1","sub2"])
      
      rot = ["6","5","4","3","2","1"]
      fRot1 = Set_Info[m-1]["StartRot1"]
      i = 8
      for i in range(1,len(serve1)):
        if serve1["No.1"][i] == serve1["No.1"][i-1]:
          brot1 = df_fRotTeam1[(df_fRotTeam1["sub1"] == str(serve1["No.1"][i-1])) | (df_fRotTeam1["sub2"] == str(serve1["No.1"][i-1]))].index[0]
          bRot1 = rot[(rot.index(fRot1) + brot1)%6]
          try:
            action = df.at[df[(df["Set"] == serve1["Set"][i-1]) & (df["Rally"] == serve1["Rally"][i-1]) & (df["result1"] == "p")].index[0],"action1"]
          except:
            try:
              action = df.at[df[(df["Set"] == serve1["Set"][i-1]) & (df["Rally"] == serve1["Rally"][i-1]) & (df["result2"] == "m")].index[0],"result2"]
              action = "o"
            except:
              try:
                action = df.at[df[(df["Set"] == serve1["Set"][i-1]) & (df["Rally"] == serve1["Rally"][i-1]) & (df["action2"] == "m")].index[0],"action2"]
                action = "o"
              except:
                action = "error"
          bp11 = {
            "Rally":serve1.at[i-1,"Rally"],
            "bRot1":bRot1,
            "action":action
          }
          bp1.append(bp11)
        df_ = df[(df["Set"]==serve1["Set"][i])&(df["Rally"]==serve1["Rally"][i])]  
        if i ==len(serve1)-1:
          if not (df_[(df_["result1"]=="p")|(df_["action2"]=="m")|(df_["result2"]=="m")]).empty:
            brot1 = df_fRotTeam1[(df_fRotTeam1["sub1"] == str(serve1["No.1"][i])) | (df_fRotTeam1["sub2"] == str(serve1["No.1"][i]))].index[0]
            bRot1 = rot[(rot.index(fRot1) + brot1)%6]
            try:
              action = df.at[df[(df["Set"] == serve1["Set"][i]) & (df["Rally"] == serve1["Rally"][i]) & (df["result1"]=="p")].index[0],"action1"]
            except:
              try:
                action = df.at[df[(df["Set"] == serve1["Set"][i]) & (df["Rally"] == serve1["Rally"][i]) & (df["result2"] == "m")].index[0],"result2"]
                action = "o"
              except:
                try:
                  action = df.at[df[(df["Set"] == serve1["Set"][i]) & (df["Rally"] == serve1["Rally"][i]) & (df["action2"] == "m")].index[0],"action2"]
                  action = "o"
                except:
                  action = "error"    
            bp11 = {
              "Rally":serve1.at[i,"Rally"],
              "bRot1":bRot1,
              "action":action
            }
            bp1.append(bp11)

    df_bp1 = pd.DataFrame(bp1)
  else:
    Set = int(Set1)
    serve1 = df[(df["Set"] == Set) & (df["action1"] == "s")].reset_index(drop=True)
    fRotTeam1 = fRotTeam01[Set-1]
    df_fRotTeam1 = pd.DataFrame(fRotTeam1,columns=["sub1","sub2"])
    bp1 = []
    rot = ["6","5","4","3","2","1"]
    fRot1 = Set_Info[Set-1]["StartRot1"]
    for i in range(1,len(serve1)):
      if serve1["No.1"][i] == serve1["No.1"][i-1]:
        brot1 = df_fRotTeam1[(df_fRotTeam1["sub1"] == str(serve1["No.1"][i-1])) | (df_fRotTeam1["sub2"] == str(serve1["No.1"][i-1]))].index[0]
        bRot1 = rot[(rot.index(fRot1) + brot1)%6]
        try:
          action = df.at[df[(df["Set"] == serve1["Set"][i-1]) & (df["Rally"] == serve1["Rally"][i-1]) & (df["result1"] == "p")].index[0],"action1"]
        except:
          try:
            action = df.at[df[(df["Set"] == serve1["Set"][i-1]) & (df["Rally"] == serve1["Rally"][i-1]) & (df["result2"] == "m")].index[0],"result2"]
            action = "o"
          except:
            try:
              action = df.at[df[(df["Set"] == serve1["Set"][i-1]) & (df["Rally"] == serve1["Rally"][i-1]) & (df["action2"] == "m")].index[0],"action2"]
              action = "o"
            except:
              action = "error"
        bp11 = {
          "Rally":serve1.at[i-1,"Rally"],
          "bRot1":bRot1,
          "action":action
        }
        bp1.append(bp11)
      df_ = df[(df["Set"]==serve1["Set"][i])&(df["Rally"]==serve1["Rally"][i])]
      if i==len(serve1)-1:
        if not df_[(df_["result1"]=="p")|(df_["action2"]=="m")|(df_["result2"]=="m")].empty:
          brot1 = df_fRotTeam1[(df_fRotTeam1["sub1"] == str(serve1["No.1"][i])) | (df_fRotTeam1["sub2"] == str(serve1["No.1"][i]))].index[0]
          bRot1 = rot[(rot.index(fRot1) + brot1)%6]
          try:
            action = df.at[df[(df["Set"] == serve1["Set"][i]) & (df["Rally"] == serve1["Rally"][i]) & (df["result1"] == "p")].index[0],"action1"]
          except:
            try:
              action = df.at[df[(df["Set"] == serve1["Set"][i]) & (df["Rally"] == serve1["Rally"][i]) & (df["result2"] == "m")].index[0],"result2"]
              action = "o"
            except:
              try:
                action = df.at[df[(df["Set"] == serve1["Set"][i]) & (df["Rally"] == serve1["Rally"][i]) & (df["action2"] == "m")].index[0],"action2"]
                action = "o"
              except:
                action = "error"
          bp11 = {
            "Rally":serve1.at[i,"Rally"],
            "bRot1":bRot1,
            "action":action
          }
          bp1.append(bp11)


    df_bp1 = pd.DataFrame(bp1)
  return df_bp1

# 背番号・アクション・リザルト別にデータから抽出
def action1(df,set,slot,number,action,result):
  if set =="":
    if slot =="":
      if number == "":
        if result == "":
          return len(df[(df["action1"] == action)])
        elif result == "effective":
          return len(df[(df["action1"] == action)& (df["result2"].isin(["c","o"]))])
        else:
          return len(df[(df["action1"] == action) & (df["result1"] == result)])
      else:
        if result == "":
          return len(df[(df["No.1"] == number) & (df["action1"] == action)])
        elif result == "effective":
          return len(df[(df["No.1"] == number) & (df["action1"] == action) & (df["result2"].isin(["c","o"]))])
        else:
          return len(df[(df["No.1"] == number) & (df["action1"] == action) & (df["result1"] == result)])
    else:
      if number == "":
        if result == "":
          return len(df[(df["pre1"] == slot) & (df["action1"] == action)])
        elif result == "effective":
          return len(df[(df["pre1"] == slot) & (df["action1"] == action) & (df["result2"].isin(["c","o"]))])
        else:
          return len(df[(df["pre1"] == slot) & (df["action1"] == action) & (df["result1"] == result)])

      else:
        if result == "":
          return len(df[(df["pre1"] == slot) & (df["No.1"] == number) & (df["action1"] == action)])
        elif result =="effective":
          return len(df[(df["pre1"] == slot) & (df["No.1"] == number) & (df["action1"] == action) & (df["result2"].isin(["c","o"]))])
        else:
          return len(df[(df["pre1"] == slot) & (df["No.1"] == number) & (df["action1"] == action) & (df["result1"] == result)])
  else:
    if slot =="":
      if number == "":
        if result == "":
          return len(df[(df["Set"] == set) & (df["action1"] == action)])
        elif result == "effective":
          return len(df[(df["Set"] == set) & (df["action1"] == action)& (df["result2"].isin(["c","o"]))])
        else:
          return len(df[(df["Set"] == set) & (df["action1"] == action) & (df["result1"] == result)])
      else:
        if result == "":
          return len(df[(df["Set"] == set) & (df["No.1"] == number) & (df["action1"] == action)])
        elif result == "effective":
          return len(df[(df["Set"] == set) & (df["No.1"] == number) & (df["action1"] == action) & (df["result2"].isin(["c","o"]))])
        else:
          return len(df[(df["Set"] == set) & (df["No.1"] == number) & (df["action1"] == action) & (df["result1"] == result)])
    else:
      if number == "":
        if result == "":
          return len(df[(df["Set"] == set) & (df["pre1"] == slot) & (df["action1"] == action)])
        elif result == "effective":
          return len(df[(df["Set"] == set) & (df["pre1"] == slot) & (df["action1"] == action) & (df["result2"].isin(["c","o"]))])
        else:
          return len(df[(df["Set"] == set) & (df["pre1"] == slot) & (df["action1"] == action) & (df["result1"] == result)])
      else:
        if result == "":
          return len(df[(df["Set"] == set) & (df["pre1"] == slot) & (df["No.1"] == number) & (df["action1"] == action)])
        elif result =="effective":
          return len(df[(df["Set"] == set) & (df["pre1"] == slot) & (df["No.1"] == number) & (df["action1"] == action) & (df["result2"].isin(["c","o"]))])        
        else:
          return len(df[(df["Set"] == set) & (df["pre1"] == slot) & (df["No.1"] == number) & (df["action1"] == action) & (df["result1"] == result)])


# 背番号・アクション別に効果率を計算
def effect1(df,number,action):
  if action == "s":
    return (action1(df,"","",number,action,"p")*100+action1(df,"","",number,action,"effective")*25+action1(df,"","",number,action,"norm")*0 - action1(df,"","",number,action,"m")*25)/action1(df,"","",number,action,"")
  elif action == "a":
    return (action1(df,"","",number,action,"p") - action1(df,"","",number,action,"m"))*100 / action1(df,"","",number,action,"")
  elif action == "b":
    return (action1(df,"","",number,action,"p")*100 +action1(df,"","",number,action,"0")*50+action1(df,"","",number,action,"t")*25-action1(df,"","",number,action,"m")*25)/action1(df,"","",number,action,"")
  elif action == "r":
    return (action1(df,"","",number,action,"a")*100+action1(df,"","",number,action,"b")*50)/action1(df,"","",number,action,"")
  elif action == "d":
    return (action1(df,"","",number,action,"a")*50+action1(df,"","",number,action,"b")*50+action1(df,"","",number,action,"c")*25-action1(df,"","",number,action,"m")*25-action1(df,"","",number,action,"o")*25)/action1(df,"","",number,action,"")

