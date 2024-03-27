from _code_ver12_1_1.Function import vb_option as vo
from _code_ver12_1_1.Data import vb_file as vf
from _code_ver12_1_1.Data import vb_data2 as vd2

import PySimpleGUI as sg
# 選手交代に非対応により廃バージョン

# 1-1新規で入力
def entry_df():
  Set_Info = []
  Set_Result = []
  Season_path,Tournament_path,date_path,Team1,Team2 = Entry_Info()
  Set = 0
  play_d = []
  df = []
  while True:
    Set_Info1,fRotTeam1,fRotTeam2,fRot1,fRot2 = entry_set(Team1,Team2)
    Set_Info.append(Set_Info1)
    play_d,df,Set_Result1,fRotTeam1,fRotTeam2,fRot1,fRot2,boot = entry_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set,play_d,df,fRotTeam1,fRotTeam2,fRot1,fRot2)
    Set_Result.append(Set_Result1)
    df_Team1,df_Team2 = vd2.makedf_MoD12(play_d)
    if boot == True:
      break
    else:
      Set += 1
      pass
  Set
  return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2,fRotTeam1,fRotTeam2,fRot1,fRot2

# 1-2取得して入力
def entry2_df():
  Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2,fRotTeam1,fRotTeam2,fRot1,fRot2 = entry2_file()
  play_d,df,Set_Result1,fRotTeam1,fRotTeam2,fRot1,fRot2,boot,event = entry2_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set,play_d,df,fRotTeam1,fRotTeam2,fRot1,fRot2)

  Set_Result[Set] = Set_Result1
  if event == " Next ":
    Set += 1
    while True:
      Set_Info1,fRotTeam1,fRotTeam2,fRot1,fRot2 = entry_set(Team1,Team2)
      Set_Info.append(Set_Info1)
      play_d,df,Set_Result1,fRotTeam1,fRotTeam2,fRot1,fRot2,boot = entry_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set,play_d,df,fRotTeam1,fRotTeam2,fRot1,fRot2)
      Set_Result.append(Set_Result1)
      df_Team1,df_Team2 = vd2.makedf_MoD12(play_d)
      if boot == True:
        break
      else:
        Set += 1
        pass

  df_Team1,df_Team2 = vd2.makedf_MoD12(play_d)

  return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2,fRotTeam1,fRotTeam2,fRot1,fRot2


# 試合情報入力
def Entry_Info():
  Info = Info_window()
  while True:
    event,values = Info.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == "Set":
      try:
        Season_path = values["Season"]
        Tournament_path = values["Tournament"]
        date_path = values["Date"]
        Team1 = values["Team1"]
        Team2 = values["Team2"]
      except:
        vo.error_window("<< Information Error >>")
      try:
        data_p,data_p1,data_p2,Team1ab,Team2ab = vf.team_index(Season_path,Tournament_path,Team1,Team2)
      except:
        vo.error_window("<< Information Error >>")
      try:
        Team1ab = data_p1.at[0,"Abbreviation"]
        Info["Team1ab"].update(f"Team1 : {Team1ab}")
      except:
        Info["Team1ab"].update("Team1 Not Found")
      try:
        Team2ab = data_p2.at[0,"Abbreviation"]
        Info["Team2ab"].update(f"Team2 : {Team2ab}")
      except:
        Info["Team2ab"].update("Team2 Not Found")
      Info[" Continue "].update(disabled=False)
    elif event == " Continue ":
      break
  Info.close()
  return Season_path,Tournament_path,date_path,Team1,Team2  

# 
# セット情報入力
  # スタートローテとメンバーから全ローテ作成
def entry_set(Team1,Team2):
  window = Set_Info_window(Team1,Team2)
  
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == " Enter ":
      Set_Number = values["Set"]
      if values["Team1"] == True:
        ServeTeam = "1"
      elif values["Team2"] == True:
        ServeTeam = "2"
      break
  fRotTeam1 = [values["Team1S1"],values["Team1S2"],values["Team1S3"],values["Team1S4"],values["Team1S5"],values["Team1S6"]]
  fRotTeam2 = [values["Team2S1"],values["Team2S2"],values["Team2S3"],values["Team2S4"],values["Team2S5"],values["Team2S6"]]
  fRot1 = values["Rot1"]
  fRot2 = values["Rot2"]  
  window.close()
  Set_Info1 = {
      "Set":Set_Number,
      "ServeTeam":ServeTeam,
      "StartRot1":fRot1,
      "StartRot2":fRot2,
    }
  return Set_Info1,fRotTeam1,fRotTeam2,fRot1,fRot2


# データ入力
# 入力方法  12/s//18;8/r/a/32,11/t//51,1/a/p/65
def entry_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set,play_d,df,fRotTeam1,fRotTeam2,fRot1,fRot2):
  subwindow = entry_sub(450,100)
  subwindow2 = entry_sub2(Team1,Team2,450,320)
  window = entry_main(600,320)
  window["Set"].update(Set_Info[Set]["Set"])
  window["Rally"].update("1")
  df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
  subwindow["-LOG-"].update(df_content)
  for i in range(0,6):
    subwindow2[f"Team1S{i+1}"].update(fRotTeam1[i])
    subwindow2[f"Team2S{i+1}"].update(fRotTeam2[i])
  boot = False
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
      res = vo.checkWin("Exit","<< Exit ? >>")
      if res == "OK":
        boot = True
        break
      elif res == "NO":
        pass
    elif event == " Exit ":
      res = vo.checkWin("Exit","<< Exit ? >>")
      if res == "OK":
        boot = True
        break
      elif res == "NO":
        pass
    elif event == "Submit":
      value = {
        "Set":values["Set"],
        "Rally":values["Rally"],
        "Motion":values["Motion"]
      }
      play_d.append(value)
      try:
        df = vd2.makedf_PlD(play_d)
      except:
        vo.error_window("<< Data Cannot Entered >>")
        continue
      window["Motion"].update("")
      window["Rally"].update(int(values["Rally"])+1)
      subwindow["-LOGpld-"].update(play_d)
      df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
      subwindow["-LOG-"].update(df_content)
      RotTeam_1 = vd2.Rotation(fRotTeam1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
      RotTeam_2 = vd2.Rotation(fRotTeam2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
      for i in range(0,6):
        subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
        subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
      subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
      subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
    elif event == " Search ":
      try:
        search = play_d[play_d.index(list(filter(lambda d : d["Set"]==values["-Set-"] and d["Rally"]==values["-Rally-"] ,play_d))[0])]
        window["-Motion-"].update(search["Motion"])
        window[" Edit "].update(disabled=False)
      except:
        vo.errorWin("<< Motion Not Found >>")  
    elif event == " Edit ":
      edition = {
        "Set":values["-Set-"],
        "Rally":values["-Rally-"],
        "Motion":values["-Motion-"]
      }
      play_d[play_d.index(search)] = edition
      subwindow["-LOGpld-"].update(play_d)
      try:
        df = vd2.makedf_PlD(play_d)
      except:
        vo.errorWin("<< Data Cannot Entered >>")
        continue
      df.reset_index(drop=True,inplace=True)
      df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
      subwindow["-LOG-"].update(df_content)
      window[" Edit "].update(disabled=True)
      window["-Motion-"].update("")
      RotTeam_1 = vd2.Rotation(fRotTeam1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
      RotTeam_2 = vd2.Rotation(fRotTeam2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
      for i in range(0,6):
        subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
        subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
      subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
      subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
    elif event == " Next " :
      break
  Set_Result1 = {
    "Set":Set_Info[Set]["Set"],
    "Score1":vd2.score_data(values["Set"],df)[0],
    "Score2":vd2.score_data(values["Set"],df)[1],
  }
  window.close()
  subwindow.close()
  subwindow2.close()
  if event == " Next " :
    boot = False
  return play_d,df,Set_Result1,fRotTeam1,fRotTeam2,fRot1,fRot2,boot

# 保存データを取得
def entry2_file():
  window = entry2_searchwindow()
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == " Continue ":
      break
    elif event == " Search ":
      try:
        Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2,fRotTeam1,fRotTeam2,fRot1,fRot2,msg = vf.fileopen(values["Season"],values["Tournament"],values["Date"],values["Teamf"],values["Teams"])
        data_p,data_p1,data_p2,Team1ab,Team2ab = vf.team_index(Season_path,Tournament_path,Team1,Team2)
        window["reading"].update(msg)
        if msg == "<< FileRead Success! >> :":
          window[" Continue "].update(disabled=False)
          window["Team1"].update(f"Team1 : {Team1}")
          window["Team2"].update(f"Team2 : {Team2}")
          window["Team1ab"].update(f" : {Team1ab}")
          window["Team2ab"].update(f" : {Team2ab}")
      except:
          vo.errorWin("<< File Not Found >>")
          pass
  window.close()
  return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2,fRotTeam1,fRotTeam2,fRot1,fRot2

# 保存データに続きから入力
def entry2_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set,play_d1,df1,fRotTeam1,fRotTeam2,fRot1,fRot2):
  df = df1
  play_d = play_d1
  subwindow = entry_sub(450,100)
  subwindow2 = entry_sub2(Team1,Team2,450,320)
  window = entry_main(600,320)
  # subwindow["-LOG-"].update(df)
  df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
  df_head = [df.columns.values[z] for z in range(0,len(df.columns))]
  subwindow["-LOG-"].update(df_content)

  subwindow["-LOGpld-"].update(play_d)
  window["Set"].update(df.at[len(df)-1,"Set"])
  window["Rally"].update(df.at[len(df)-1,"Rally"]+1)
  RotTeam_1 = vd2.Rotation(fRotTeam1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],df.at[len(df)-1,"Set"],df.at[len(df)-1,"Rally"],df)[0])
  RotTeam_2 = vd2.Rotation(fRotTeam2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],df.at[len(df)-1,"Set"],df.at[len(df)-1,"Rally"],df)[1])
  for i in range(0,6):
    subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
    subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
  subwindow2["Score1"].update(vd2.score_data(df.at[len(df)-1,"Set"],df)[0])
  subwindow2["Score2"].update(vd2.score_data(df.at[len(df)-1,"Set"],df)[1])
  boot = False
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
      res = vo.checkWin("Exit","<< Exit ? >>")
      if res == "OK":
        boot = True
        break
      elif res == "NO":
        pass
    elif event == " Exit ":
      res = vo.checkWin("Exit","<< Exit ? >>")
      if res == "OK":
        boot = True
        break
      elif res == "NO":
        pass
    elif event == "Submit":
      value = {
        "Set":values["Set"],
        "Rally":values["Rally"],
        "Motion":values["Motion"]
      }
      play_d.append(value)
      try:
        df = vd2.makedf_PlD(play_d)
      except:
        vo.error_window("再入力してください")
        pass
      window["Motion"].update("")
      window["Rally"].update(int(values["Rally"])+1)
      df_content = [[df.iat[y,x] for x in range(0,len(df.columns))] for y in range(0,len(df))]
      subwindow["-LOGpld-"].update(play_d)
      subwindow["-LOG-"].update(df_content)
      RotTeam_1 = vd2.Rotation(fRotTeam1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
      RotTeam_2 = vd2.Rotation(fRotTeam2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
      for i in range(0,6):
        subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
        subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
      subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
      subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
      Score1 = vd2.score_data(values["Set"],df)[0]
      Score2= vd2.score_data(values["Set"],df)[1]
    elif event == " Search ":
      try:
        search = play_d[play_d.index(list(filter(lambda d : d["Set"]==values["-Set-"] and d["Rally"]==values["-Rally-"] ,play_d))[0])]
        window["-Motion-"].update(search["Motion"])
        window[" Edit "].update(disabled=False)
      except:
        vo.errorWin("<< Motion Not Found >>")  
    elif event == " Edit ":
      edition = {
        "Set":values["-Set-"],
        "Rally":values["-Rally-"],
        "Motion":values["-Motion-"]
      }
      play_d[play_d.index(search)] = edition
      subwindow["-LOGpld-"].update(play_d)
      df = vd2.makedf_PlD(play_d)
      df.reset_index(drop=True,inplace=True)
      df_content = [[df.iat[y,x] for x in range(0,len(df.columns))]for y in range(0,len(df))]
      subwindow["-LOG-"].update(df_content)
      window[" Edit "].update(disabled=True)
      window["-Motion-"].update("")
      RotTeam_1 = vd2.Rotation(fRotTeam1,fRot1,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
      RotTeam_2 = vd2.Rotation(fRotTeam2,fRot2,vd2.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
      for i in range(0,6):
        subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
        subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
      subwindow2["Score1"].update(vd2.score_data(values["Set"],df)[0])
      subwindow2["Score2"].update(vd2.score_data(values["Set"],df)[1])
    elif event == " Next " :
      break
  try:
    Set_Result1 = {
      "Set":Set_Info[Set]["Set"],
      "Score1":vd2.score_data(values["Set"],df)[0],
      "Score2":vd2.score_data(values["Set"],df)[1],
    }
  except:
    Set_Result1 = {
      "Set":Set_Info[Set]["Set"],
      "Score1":Score1,
      "Score2":Score2,
    }
  window.close()
  subwindow.close()
  subwindow2.close()
  if event == " Next " :
    boot = False
  window.close()
  subwindow.close()
  return play_d,df,Set_Result1,fRotTeam1,fRotTeam2,fRot1,fRot2,boot,event

# 機能：交代機能
# window = pop_substitute_window(Team1,Team2)


# ウィンドウ

# 試合情報入力ウィンドウ
def Info_window():
  Info_layout = [[sg.Text("Season : "),sg.Input(key="Season",size=(10,5))],[sg.Text("Tournament : "),sg.Input(key="Tournament")],[sg.Text("Date : "),sg.Input(key="Date")],[sg.Text("Team1 : "),sg.Input(key="Team1",size=(9,5))],[sg.Text("Team2 : "),sg.Input(key="Team2",size=(9,5))],[],[sg.Button("Set")],[sg.Button(" Continue ",disabled=True)],[sg.Text("",size=(10,5)),sg.Text("-------Player_index-------",key="Info_Set"),sg.Text("",size=(10,5))],[sg.Text("",key="Team1ab")],[sg.Text(key="Team2ab")]]
  return sg.Window("Entry Match Infomation",Info_layout,finalize=True)


# セット情報入力ウィンドウ
def Set_Info_window(Team1,Team2):
  set_layout = [[sg.Text("Set : "),sg.Input(key="Set",size=(5,2))],[sg.Text("Serve Team : "),sg.Radio(f"{Team1}",key="Team1",group_id="0"),sg.Radio(f"{Team2}",key="Team2",group_id="0")],[sg.Text(f"{Team1} : "),sg.Text("S"),sg.Input(key="Rot1",size=(2,2))],[sg.Text("S1:"),sg.Input(key="Team1S1",size=(2,2)),sg.Text("S6:"),sg.Input(key="Team1S6",size=(2,2)),sg.Text("S5:"),sg.Input(key="Team1S5",size=(2,2))],[sg.Text("S2:"),sg.Input(key="Team1S2",size=(2,2)),sg.Text("S3:"),sg.Input(key="Team1S3",size=(2,2)),sg.Text("S4:"),sg.Input(key="Team1S4",size=(2,2))],[sg.Text(f"{Team2}: "),sg.Text("S"),sg.Input(key="Rot2",size=(2,2))],[sg.Text("S4:"),sg.Input(key="Team2S4",size=(2,2)),sg.Text("S3:"),sg.Input(key="Team2S3",size=(2,2)),sg.Text("S2:"),sg.Input(key="Team2S2",size=(2,2))],[sg.Text("S5:"),sg.Input(key="Team2S5",size=(2,2)),sg.Text("S6:"),sg.Input(key="Team2S6",size=(2,2)),sg.Text("S1:"),sg.Input(key="Team2S1",size=(2,2))],[sg.Text(size=(10,2)),sg.Button(" Enter "),sg.Text(size=(10,2))]]
  return sg.Window("Set Information",set_layout,finalize=True)

# データ入力メインウィンドウ
def entry_main(x=None, y=None):
  main_layout = [[sg.Text("Set: "),sg.Input(key="Set",size=(5,5))],[sg.Text("Rally: #"),sg.Input(key="Rally",size=(5,5))],[sg.Text("Motion: "),sg.Input(key="Motion",size=(200,5))],[sg.Button("Submit")],[],[],[sg.Text("                                  ----------------------------------------------                ")],[sg.Text(size=(25,2)),sg.Text("Data Edition"),sg.Text(size=(25,2))],[sg.Text("Set : "),sg.Input(key="-Set-",size=(5,5)),sg.Text("Rally : #"),sg.Input(key="-Rally-",size=(5,5))],[sg.Text("Motion : "),sg.Input(key="-Motion-",size=(200,10))],[sg.Button(" Search "),sg.Button(" Edit ",disabled=True),sg.Button(" Exit ")],[sg.Text(" Next Set : "),sg.Button(" Next "),sg.Text(key="Save Condition")]]
  return sg.Window("Data Entry",main_layout,finalize=True,size=(500,400),location=(x,y))

# データ入力サブウィンドウ
def entry_sub(x=None,y=None):
  df_content = [[]]
  df_head = ["Set","Rally","No.1","pre1","action1","result1","zone1","No.2","pre2","action2","result2","zone2"]
  # sub_layout = [[sg.Multiline(size=(100,10),key="-LOG-",autoscroll=True)],[sg.Multiline(size=(100,10),key="-LOGpld-",autoscroll=True)]]
  sub_layout = [
    [sg.Table(df_content,df_head,size=(100,10),key="-LOG-",def_col_width=7, vertical_scroll_only=True,font=("Arial",8),auto_size_columns=False)],
    [sg.Multiline(size=(100,10),key="-LOGpld-",autoscroll=True)]
    ]
  return sg.Window("Data Process",sub_layout,finalize=True,size=(800,400),location=(x,y))

# サブサブウィンドウ
  # 取得したセットデータから入力時のローテの表示
  # 
def entry_sub2(Team1,Team2,x=None,y=None):
  sub2_layout = [[sg.Text(f"{Team1} vs {Team2}")],[sg.Input(key="Score1",size=(2,2)),sg.Text(" vs "),sg.Input(key="Score2",size=(2,2))],[sg.Text(f"{Team1} : ")],[sg.Text(),sg.Input(key="Team1S1",size=(2,2)),sg.Text(),sg.Input(key="Team1S6",size=(2,2)),sg.Text(),sg.Input(key="Team1S5",size=(2,2))],[sg.Text(),sg.Input(key="Team1S2",size=(2,2)),sg.Text(),sg.Input(key="Team1S3",size=(2,2)),sg.Text(),sg.Input(key="Team1S4",size=(2,2))],[sg.Text(f"{Team2} : ")],[sg.Text(),sg.Input(key="Team2S4",size=(2,2)),sg.Text(),sg.Input(key="Team2S3",size=(2,2)),sg.Text(),sg.Input(key="Team2S2",size=(2,2))],[sg.Text(),sg.Input(key="Team2S5",size=(2,2)),sg.Text(),sg.Input(key="Team2S6",size=(2,2)),sg.Text(),sg.Input(key="Team2S1",size=(2,2))]]
  return sg.Window("Rotation",sub2_layout,finalize=True,size=(400,400),location=(x,y))

# 保存データ検索画面
def entry2_searchwindow(x=None,y=None):
  main_layout = [[sg.Text("Season : "),sg.Input(key="Season")],[sg.Text("Tournament : "),sg.Input(key="Tournament")],[sg.Text("Date : "),sg.Input(key="Date")],[sg.Text("Teamf : "),sg.Input(key="Teamf")],[sg.Text("Teams : "),sg.Input(key="Teams")],[sg.Button(" Search ")],[sg.Button(" Continue ",disabled=True)],[sg.Text(key="reading")],[sg.Text(key="filename")],[sg.Text(key="Team1"),sg.Text(key="Team1ab")],[sg.Text(key="Team2"),sg.Text(key="Team2ab")],[sg.Text(key="index")],[sg.Text(key="pld_Team1")],[sg.Text(key="pld_Team2")]]
  return sg.Window("File Read",main_layout,finalize=True,size=(500,500),location=(x,y))

# 選手交代機能画面
def pop_substitute_window(Team1,Team2,x=None,y=None):
  layout = [
    [sg.Text(f"{Team1}"),sg.Text("Set : "),sg.Input(key="Set",size=(2,1)),sg.Text("Rally : "),sg.Input(key="Rally",size=(2,1)),sg.Text(f"{Team2}")],
    [sg.Text("Out : No."),sg.Input(key="Out1",size=(2,1)),sg.Text("          "),sg.Text("Out : No."),sg.Input(key="Out2",size=(2,1))],
    [sg.Text("In : No."),sg.Input(key="In1",size=(2,1)),sg.Text("          "),sg.Text("In : No."),sg.Input(key="In2",size=(2,1))],
    [sg.Button("SUB",key="SUB1"),sg.Text("             "),sg.Button("SUB",key="SUB2")]
  ]
  return sg.Window("Substitution Option",layout,finalize=True,size=(300,200),location=(x,y))


