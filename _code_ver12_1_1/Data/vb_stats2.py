from _code_ver12_1_1.Function import vb_option as vo

import pandas as pd
import numpy as np

# 個人スタッツdf作成

# Team2

# チーム別スタッツdf作成
def Tstats2(data_p2,dfa,set):
  if set:
    df = dfa[dfa["Set"] == set]
  else:
    df = dfa
  num_div2 = df["No.2"].unique()
  div2 = []
  div2all = []
  df_div2all = pd.DataFrame(div2all,index=["None"])
  for i in range(0,len(data_p2)):
    if int(data_p2["No"][i]) in num_div2:
      div2.append(data_p2["No"][i])
  for div in div2:
    stat_div2n = {
      "Name":data_p2.loc[data_p2[data_p2["No"]==str(div)].index.tolist()[0],"Player"],
      "No.":(data_p2.loc[data_p2[data_p2["No"]==str(div)].index.tolist()[0],"No"]),
      "Position":data_p2.loc[data_p2[data_p2["No"]==str(div)].index.tolist()[0],"Position"],
    }
    try:
      stat_div2s = {
        "s-All":action2(df,"","",int(div),"s",""),
        "s-Point":action2(df,"","",int(div),"s","p"),
        "s-Effective":action2(df,"","",int(div),"s","effective"),
        "s-Miss":action2(df,"","",int(div),"s","m"),
        "s-success":effect2(df,int(div),"s"),
      }
    except:
      stat_div2s = {
        "s-All":"NaN",
        "s-Point":"NaN",
        "s-Effective":"NaN",
        "s-Miss":"NaN",
        "s-success":"NaN",
      }

    try:
      stat_div2a = {
        "a-All":action2(df,"","",int(div),"a",""),
        "a-Point":action2(df,"","",int(div),"a","p"),
        "a-Effective":action2(df,"","",int(div),"a","effective"),
        "a-Miss":action2(df,"","",int(div),"a","m"),
        "a-success":effect2(df,int(div),"a"),
      }
    except:
      stat_div2a = {
        "a-All":"NaN",
        "a-Point":"NaN",
        "a-Effective":"NaN",
        "a-Miss":"NaN",
        "a-success":"NaN",
      }
    try:
      stat_div2b = {
        "b-All":action2(df,"","",int(div),"b",""),
        "b-Point":action2(df,"","",int(div),"b","p"),
        "b-Effective":action2(df,"","",int(div),"b","t"),
        "b-Miss":action2(df,"","",int(div),"a","m"),
        "b-success":effect2(df,int(div),"b"),
      }
    except:
      stat_div2b = {
        "b-All":"NaN",
        "b-Point":"NaN",
        "b-Effective":"NaN",
        "b-Miss":"NaN",
        "b-success":"NaN",
      }

    try:
      stat_div2r = {
        "r-All":action2(df,"","",int(div),"r",""),
        "r-A":action2(df,"","",int(div),"r","a"),
        "r-B":action2(df,"","",int(div),"r","b"),
        "r-Miss":action2(df,"","",int(div),"r","m"),
        "r-success":effect2(df,int(div),"r"),
      }
    except:
      stat_div2r = {
        "r-All":"NaN",
        "r-A":"NaN",
        "r-B":"NaN",
        "r-Miss":"NaN",
        "r-success":"NaN",
      }

    try:
      stat_div2d = {
        "d-All":action2(df,"","",int(div),"d",""),
        "d-Miss":action2(df,"","",int(div),"d","m"),
        "d-success":effect2(df,int(div),"d"),
      }
    except:
      stat_div2d = {
        "d-All":"NaN",
        "d-Miss":"NaN",
        "d-success":"NaN",
      }

    try:
      stat_div2m = {
        "m-All":action2(df,"","",int(div),"m",""),
      }
    except:
      stat_div2m = {
        "m-All":"NaN",
      }



    df_div2n = pd.DataFrame(stat_div2n,index=[0])
    df_div2s = pd.DataFrame(stat_div2s,index =[0])
    df_div2a = pd.DataFrame(stat_div2a,index =[0])
    df_div2b = pd.DataFrame(stat_div2b,index =[0])
    df_div2r = pd.DataFrame(stat_div2r,index =[0])
    df_div2d = pd.DataFrame(stat_div2d,index =[0])
    df_div2m = pd.DataFrame(stat_div2m,index =[0])
    df_div2p = pd.concat([df_div2n,df_div2s,df_div2a,df_div2b,df_div2r,df_div2d,df_div2m],axis=1)
    df_div2all = pd.concat([df_div2all,df_div2p],axis=0)
  # 最終dfの調整
  df_div2all.drop("None",axis=0,inplace=True)
  df_div2all.reset_index(drop=True,inplace=True)
  df_div2all.index = df_div2all.index + 1
  stat_t2n = {
    "Name":"All",
    "No.":"NaN",
    "Position":"NaN"
  }
  stat_t2s = {
    "s-All":action2(df,"","","","s",""),
    "s-Point":action2(df,"","","","s","p"),
    "s-Effective":action2(df,"","","","s","effective"),
    "s-Miss":action2(df,"","","","s","m"),
    "s-success":effect2(df,"","s")
  }
  stat_t2a = {
    "a-All":action2(df,"","","","a",""),
    "a-Point":action2(df,"","","","a","p"),
    "a-Effective":action2(df,"","","","a","effective"),
    "a-Miss":action2(df,"","","","a","m"),
    "a-success":effect2(df,"","a")
  }
  stat_t2b = {
    "b-All":action2(df,"","","","b",""),
    "b-Point":action2(df,"","","","b","p"),
    "b-Effective":action2(df,"","","","b","t"),
    "b-Miss":action2(df,"","","","b","m"),
    "b-success":effect2(df,"","b")
  }
  stat_t2r = {
    "r-All":action2(df,"","","","r",""),
    "r-A":action2(df,"","","","r","a"),
    "r-B":action2(df,"","","","r","b"),
    "r-Miss":action2(df,"","","","r","m"),
    "r-success":effect2(df,"","r"),
  }
  stat_t2d = {
    "d-All":action2(df,"","","","d",""),
    "d-Miss":action2(df,"","","","d","m"),
    "d-success":effect2(df,"","d")
  }
  stat_t2m = {
    "m-All":action2(df,"","","","m","")
  }
  df_t2n = pd.DataFrame(stat_t2n,index=[0])
  df_t2s = pd.DataFrame(stat_t2s,index=[0])
  df_t2a = pd.DataFrame(stat_t2a,index=[0])
  df_t2b = pd.DataFrame(stat_t2b,index=[0])
  df_t2r = pd.DataFrame(stat_t2r,index=[0])
  df_t2d = pd.DataFrame(stat_t2d,index=[0])
  df_t2m = pd.DataFrame(stat_t2m,index=[0])
  df_t2 = pd.concat([df_t2n,df_t2s,df_t2a,df_t2b,df_t2r,df_t2d,df_t2m],axis=1)
  df_Tstats2 = pd.concat([df_div2all,df_t2],axis=0)  

  return df_Tstats2

# サーブの選手番号から現在のローテーションを逆算　→dfのserve連続値からブレイクの計測
def bp2(Set1,df,fRotTeam02,Set_Info):
  if Set1 == "All":
    serve02 = df[df["action2"] == "s"].reset_index(drop=True)
    bp2 = []
    rot = ["6","5","4","3","2","1"]
    for m in range(1,len(Set_Info)+1):
      serve2 = serve02[serve02["Set"] ==m].reset_index(drop=True)
      fRotTeam2 = fRotTeam02[m-1]
      fRot2 = Set_Info[m-1]["StartRot2"]
      df_fRotTeam2 = pd.DataFrame(fRotTeam2,columns=["sub1","sub2"])
      for i in range(1,len(serve2)):
        if serve2["No.2"][i] == serve2["No.2"][i-1]:
          brot2 = df_fRotTeam2[(df_fRotTeam2["sub1"] == str(serve2["No.2"][i-1])) | (df_fRotTeam2["sub2"] == str(serve2["No.2"][i-1]))].index[0]
          bRot2 = rot[(rot.index(fRot2) + brot2)%6]
          try:
            action = df.at[df[(df["Set"] == serve2["Set"][i-1]) & (df["Rally"] == serve2["Rally"][i-1]) & (df["result2"] == "p")].index[0],"action2"]
          except:
            try:
              action = df.at[df[(df["Set"] == serve2["Set"][i-1]) & (df["Rally"] == serve2["Rally"][i-1]) & (df["result1"] == "m")].index[0],"result1"]
              action = "o"
            except:
              try:
                action = df.at[df[(df["Set"] == serve2["Set"][i-1]) & (df["Rally"] == serve2["Rally"][i-1]) & (df["action1"] == "m")].index[0],"action1"]
                action = "o"
              except:
                action = "error"    
          bp21 = {
            "Rally":serve2.at[i-1,"Rally"],
            "bRot2":bRot2,
            "action":action
          }
          bp2.append(bp21)
        df_ = df[(df["Set"]==serve2["Set"][i])&(df["Rally"]==serve2["Rally"][i])]  
        if i == len(serve2)-1:
          if not (df_[(df_["result2"]=="p")|(df_["action1"]=="m")|(df_["result1"]=="m")]).empty:
            brot2 = df_fRotTeam2[(df_fRotTeam2["sub1"] == str(serve2["No.2"][i])) | (df_fRotTeam2["sub2"] == str(serve2["No.2"][i]))].index[0]
            bRot2 = rot[(rot.index(fRot2) + brot2)%6]
            try:
              action = df.at[df[(df["Set"] == serve2["Set"][i]) & (df["Rally"] == serve2["Rally"][i]) & (df["result2"]=="p")].index[0],"action2"]
            except:
              try:
                action = df.at[df[(df["Set"] == serve2["Set"][i]) & (df["Rally"] == serve2["Rally"][i]) & (df["result1"] == "m")].index[0],"result1"]
                action = "o"
              except:
                try:
                  action = df.at[df[(df["Set"] == serve2["Set"][i]) & (df["Rally"] == serve2["Rally"][i]) & (df["action1"] == "m")].index[0],"action1"]
                  action = "o"
                except:
                  action = "error"    
            bp21 = {
              "Rally":serve2.at[i,"Rally"],
              "bRot2":bRot2,
              "action":action
            }
            bp2.append(bp21)

    df_bp2 = pd.DataFrame(bp2)

  else:
    Set = int(Set1)
    serve2 = df[(df["Set"] == Set) & (df["action2"] == "s")].reset_index(drop=True)
    fRotTeam2 = fRotTeam02[Set-1]
    fRot2 = Set_Info[Set-1]["StartRot2"]
    df_fRotTeam2 = pd.DataFrame(fRotTeam2,columns=["sub1","sub2"])
    bp2 = []
    rot = ["6","5","4","3","2","1"]
    for i in range(1,len(serve2)):
      if serve2["No.2"][i] == serve2["No.2"][i-1]:
        brot2 = df_fRotTeam2[(df_fRotTeam2["sub1"] == str(serve2["No.2"][i-1])) | (df_fRotTeam2["sub2"] == str(serve2["No.2"][i-1]))].index[0]
        bRot2 = rot[(rot.index(fRot2) + brot2)%6]
        try:
          action = df.at[df[(df["Set"] == serve2["Set"][i-1]) & (df["Rally"] == serve2["Rally"][i-1]) & (df["result2"] == "p")].index[0],"action2"]
        except:
          try:
            action = df.at[df[(df["Set"] == serve2["Set"][i-1]) & (df["Rally"] == serve2["Rally"][i-1]) & (df["result1"] == "m")].index[0],"result1"]
            action = "o"
          except:
            try:
              action = df.at[df[(df["Set"] == serve2["Set"][i-1]) & (df["Rally"] == serve2["Rally"][i-1]) & (df["action1"] == "m")].index[0],"action1"]
              action = "o"
            except:
              action = "error"    
        bp21 = {
          "Rally":serve2.at[i-1,"Rally"],
          "bRot2":bRot2,
          "action":action
        }
        bp2.append(bp21)
      
      df_ = df[(df["Set"]==serve2["Set"][i])&(df["Rally"]==serve2["Rally"][i])]
      if i == len(serve2)-1:
        if not df_[(df_["result2"]=="p")|(df_["action1"]=="m")|(df_["result1"]=="m")].empty:
          brot2 = df_fRotTeam2[(df_fRotTeam2["sub1"] == str(serve2["No.2"][i])) | (df_fRotTeam2["sub2"] == str(serve2["No.2"][i]))].index[0]
          bRot2 = rot[(rot.index(fRot2) + brot2)%6]
          try:
            action = df.at[df[(df["Set"] == serve2["Set"][i]) & (df["Rally"] == serve2["Rally"][i]) & (df["result2"] == "p")].index[0],"action2"]
          except:
            try:
              action = df.at[df[(df["Set"] == serve2["Set"][i]) & (df["Rally"] == serve2["Rally"][i]) & (df["result1"] == "m")].index[0],"result1"]
              action = "o"
            except:
              try:
                action = df.at[df[(df["Set"] == serve2["Set"][i]) & (df["Rally"] == serve2["Rally"][i]) & (df["action1"] == "m")].index[0],"action1"]
                action = "o"
              except:
                action = "error"    
          bp21 = {
            "Rally":serve2.at[i,"Rally"],
            "bRot2":bRot2,
            "action":action
          }
          bp2.append(bp21)


    df_bp2 = pd.DataFrame(bp2)
  return df_bp2

# 
def action2(df,set,slot,number,action,result):
  if set == "":
    if slot == "":
      if number == "":
        if result == "":
          return len(df[df["action2"] == action])
        elif result == "effective":
          return len(df[(df["action2"] == action) & (df["result1"].isin(["c","o"]))])
        else:
          return len(df[(df["action2"] == action) & (df["result2"] == result)])
      else:
        if result =="":
          return len(df[(df["No.2"] == number) & (df["action2"] == action)])
        elif result == "effective":
          return len(df[(df["No.2"] == number) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))])
        else:
          return len(df[(df["No.2"] == number) & (df["action2"] == action) & (df["result2"] == result)])
    else:
      if number == "":
        if result == "":
          return len(df[(df["pre2"] == slot) & (df["action2"] == action)])
        elif result == "effective":
          return len(df[(df["pre2"] == slot) & (df["No.2"] == number) & (df["result1"].isin(["c","o"]))])
        else:
          return len(df[(df["pre2"] == slot) & (df["No.2"] == number) & (df["result2"] == result)])
      else: 
        if result == "":
          return len(df[(df["pre2"] == slot) & (df["No.2"] == number)])
        elif result == "effective":
          return len(df[(df["pre2"] == slot) & (df["No.2"] == number) & (df["result1"].isin(["c","o"]))])
        else:     
          return len(df[(df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action) & (df["result2"] == result)])
  else:
    if slot == "":
      if number == "":
        if result == "":
          return len(df[(df["Set"] == set) & (df["action2"] == action)])
        elif result == "effective":
          return len(df[(df["Set"] == set) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))])
        else:
          return len(df[(df["Set"] == set) & (df["action2"] == action) & (df["result2"] == result)])
      else:
        if result == "":
          return len(df[(df["Set"] == set) & (df["No.2"] == number) & (df["action2"] == action)])
        elif result == "effective":
          return len(df[(df["Set"] == set) & (df["No.2"] == number) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))])
        else:
          return len(df[(df["Set"] == set) & (df["No.2"] == number) & (df["action2"] == action) & (df["result2"] == result)])
    else:
      if number == "":
        if result == "":
          return len(df[(df["Set"] == set) & (df["pre2"] == slot) & (df["action2"] == action)])
        elif result == "effective":
          return len(df[(df["Set"] == set) & (df["pre2"] == slot) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))])
        else:
          return len(df[(df["Set"] == set) & (df["pre2"] == slot) & (df["action2"] == action) & (df["result2"] == result)])
      else:
        if result == "":
          return len(df[(df["Set"] == set) & (df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action)])
        elif result == "effective":
          return len(df[(df["Set"] == set) & (df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action) & (df["result1"].isin(["c","o"]))])
        else:
          return len(df[(df["Set"] == set) & (df["pre2"] == slot) & (df["No.2"] == number) & (df["action2"] == action) & (df["result2"] == result)])


# 効果率

def effect2(df,number,action):
  if action == "s":
    return (action2(df,"","",number,action,"p")*100+action2(df,"","",number,action,"effective")*25+action2(df,"","",number,action,"norm")*0 - action2(df,"","",number,action,"m")*25)/action2(df,"","",number,action,"")
  elif action == "a":
    return (action2(df,"","",number,action,"p") - action2(df,"","",number,action,"m"))*100 / action2(df,"","",number,action,"")
  elif action == "b":
    return (action2(df,"","",number,action,"p")*100 +action2(df,"","",number,action,"0")*50+action2(df,"","",number,action,"t")*25-action2(df,"","",number,action,"m")*25)/action2(df,"","",number,action,"")
  elif action == "r":
    return (action2(df,"","",number,action,"a")*100+action2(df,"","",number,action,"b")*50)/action2(df,"","",number,action,"")
  elif action == "d":
    return (action2(df,"","",number,action,"a")*50+action2(df,"","",number,action,"b")*50+action2(df,"","",number,action,"c")*25-action2(df,"","",number,action,"m")*25-action2(df,"","",number,action,"o")*25)/action2(df,"","",number,action,"")
