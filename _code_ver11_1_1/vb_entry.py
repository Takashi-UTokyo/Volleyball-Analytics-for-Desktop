from _code_ver11_1_1 import vb_option as vo
from _code_ver11_1_1 import vb_file as vf
from _code_ver11_1_1 import vb_data1 as vd1
import PySimpleGUI as sg


# 1-1新規で入力
def entry_df():
  Set_Info = []
  Set_Result = []
  Season_path,Tournament_path,date_path,Team1,Team2 = Entry_Info()
  Set = 0
  play_d = []
  df = []
  while True:
    Set_Info1,RotTeam1,RotTeam2,Rot1,Rot2 = entry_set(Team1,Team2)
    Set_Info.append(Set_Info1)
    play_d,df,Set_Result1,boot = entry_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set,play_d,df,RotTeam1,RotTeam2,Rot1,Rot2)
    Set_Result.append(Set_Result1)
    df_Team1,df_Team2 = vd1.makedf_MoD12(play_d)
    if boot == True:
      break
    else:
      Set += 1
      pass
  Set
  return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2

# 1-2取得して入力
def entry2_df():
  Season_path,Tournament_path,date_path,Team1,Team2,play_d,df,df_Team1,df_Team2 = entry2_file()
  play_d,df = entry2_data(Season_path,Tournament_path,date_path,Team1,Team2,play_d,df)
  df_Team1,df_Team2 = vd1.makedf_MoD12(play_d)

  return Season_path,Tournament_path,date_path,Team1,Team2,play_d,df,df_Team1,df_Team2




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
  RotTeam1 = [values["Team1S1"],values["Team1S2"],values["Team1S3"],values["Team1S4"],values["Team1S5"],values["Team1S6"]]
  RotTeam2 = [values["Team2S1"],values["Team2S2"],values["Team2S3"],values["Team2S4"],values["Team2S5"],values["Team2S6"]]
  Rot1 = values["Rot1"]
  Rot2 = values["Rot2"]  
  window.close()
  Set_Info1 = {
      "Set":Set_Number,
      "ServeTeam":ServeTeam,
      "StartRot1":Rot1,
      "StartRot2":Rot2,
    }
  return Set_Info1,RotTeam1,RotTeam2,Rot1,Rot2


# データ入力
# 入力方法  12/s//18,8/r/a/32,,11/t//51,,1/a/p/65
def entry_data(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set,play_d,df,RotTeam1,RotTeam2,Rot1,Rot2):
  subwindow = entry_sub()
  subwindow2 = entry_sub2(Team1,Team2)
  window = entry_main()
  window["Set"].update(Set_Info[Set]["Set"])
  window["Rally"].update("1")
  for i in range(0,6):
    subwindow2[f"Team1S{i+1}"].update(RotTeam1[i])
    subwindow2[f"Team2S{i+1}"].update(RotTeam2[i])
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
      df = vd1.makedf_PlD(play_d)
      window["Motion"].update("")
      window["Rally"].update(int(values["Rally"])+1)
      subwindow["-LOGpld-"].update(play_d)
      subwindow["-LOG-"].update(df)
      RotTeam_1 = vd1.Rotation(RotTeam1,Rot1,vd1.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
      RotTeam_2 = vd1.Rotation(RotTeam2,Rot2,vd1.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
      for i in range(0,6):
        subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
        subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
      subwindow2["Score1"].update(vd1.score_data(values["Set"],df)[0])
      subwindow2["Score2"].update(vd1.score_data(values["Set"],df)[1])
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
      df = vd1.makedf_PlD(play_d)
      subwindow["-LOG-"].update(df)
      window[" Edit "].update(disabled=True)
      window["-Motion-"].update("")
      RotTeam_1 = vd1.Rotation(RotTeam1,Rot1,vd1.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[0])
      RotTeam_2 = vd1.Rotation(RotTeam2,Rot2,vd1.Rot(Set_Info[Set]["ServeTeam"],values["Set"],values["Rally"],df)[1])
      for i in range(0,6):
        subwindow2[f"Team1S{i+1}"].update(RotTeam_1[i])
        subwindow2[f"Team2S{i+1}"].update(RotTeam_2[i])
      subwindow2["Score1"].update(vd1.score_data(values["Set"],df)[0])
      subwindow2["Score2"].update(vd1.score_data(values["Set"],df)[1])
    elif event == " Next " :
      break
  Set_Result1 = {
    "Set":Set_Info[Set]["Set"],
    "Score1":vd1.score_data(values["Set"],df)[0],
    "Score2":vd1.score_data(values["Set"],df)[1],
  }
  window.close()
  subwindow.close()
  subwindow2.close()
  if event == " Next " :
    boot = False
  return play_d,df,Set_Result1,boot

# 保存データを取得
def entry2_file():
  window = entry2_searchwindow()
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == " Continue ":
      break
    elif event == " Search ":
      Season_path,Tournament_path,date_path,Team1,Team2,play_d,df,df_Team1,df_Team2,msg,index = vf.fileopen(values["Season"],values["Tournament"],values["Date"],values["Teamf"],values["Teams"])
      data_p,data_p1,data_p2,Team1ab,Team2ab = vf.team_index(Season_path,Tournament_path,Team1,Team2)
      window["reading"].update(msg)
      if msg == "<< FileRead Success! >> :":
        window[" Continue "].update(disabled=False)
        window["index"].update(index)
        window["Team1"].update(f"Team1 : {Team1}")
        window["Team2"].update(f"Team2 : {Team2}")
        window["Team1ab"].update(f" : {Team1ab}")
        window["Team2ab"].update(f" : {Team2ab}")
  window.close()
  return Season_path,Tournament_path,date_path,Team1,Team2,play_d,df,df_Team1,df_Team2

# 保存データに続きから入力
def entry2_data(Season_path,Tournament_path,date_path,Team1,Team2,play_d1,df1):
  df = df1
  play_d = play_d1
  subwindow = entry_sub()
  window = entry_main()
  subwindow["-LOG-"].update(df)
  subwindow["-LOGpld-"].update(play_d)
  window["Set"].update(df.at[len(df)-1,"Set"])
  window["Rally"].update(df.at[len(df)-1,"Rally"]+1)
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == " Exit ":
      res = vo.checkWin("Exit","<< Exit ?>>")
      if res == "OK":
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
      df = vd1.makedf_PlD(play_d)
      window["Motion"].update("")
      window["Rally"].update(int(values["Rally"])+1)
      subwindow["-LOGpld-"].update(play_d)
      subwindow["-LOG-"].update(vd1.makedf_PlD(play_d))
    elif event == " Search ":
      try:
        search = play_d[play_d.index(list(filter(lambda d : d['Set']==int(values["-Set-"]) and d['Rally']==int(values["-Rally-"]) ,play_d))[0])]
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
      df = vd1.makedf_PlD(play_d)
      subwindow["-LOG-"].update(df)
      window[" Edit "].update(disabled=True)
      window["-Motion-"].update("")
    elif event == " Save ":
      vf.filesave(Season_path,Tournament_path,date_path,Team1,Team2,play_d,df)
  window.close()
  subwindow.close()
  return play_d,df



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
  sub_layout = [[sg.Multiline(size=(100,10),key="-LOG-",autoscroll=True)],[sg.Multiline(size=(100,10),key="-LOGpld-",autoscroll=True)]]
  return sg.Window("Data Process",sub_layout,finalize=True,size=(800,400),location=(x,y))

# サブサブウィンドウ
  # 取得したセットデータから入力時のローテの表示
  # 
def entry_sub2(Team1,Team2):
  sub2_layout = [[sg.Text(f"{Team1} vs {Team2}")],[sg.Input(key="Score1",size=(2,2)),sg.Text(" vs "),sg.Input(key="Score2",size=(2,2))],[sg.Text(f"{Team1} : ")],[sg.Text(),sg.Input(key="Team1S1",size=(2,2)),sg.Text(),sg.Input(key="Team1S6",size=(2,2)),sg.Text(),sg.Input(key="Team1S5",size=(2,2))],[sg.Text(),sg.Input(key="Team1S2",size=(2,2)),sg.Text(),sg.Input(key="Team1S3",size=(2,2)),sg.Text(),sg.Input(key="Team1S4",size=(2,2))],[sg.Text(f"{Team2} : ")],[sg.Text(),sg.Input(key="Team2S4",size=(2,2)),sg.Text(),sg.Input(key="Team2S3",size=(2,2)),sg.Text(),sg.Input(key="Team2S2",size=(2,2))],[sg.Text(),sg.Input(key="Team2S5",size=(2,2)),sg.Text(),sg.Input(key="Team2S6",size=(2,2)),sg.Text(),sg.Input(key="Team2S1",size=(2,2))]]
  return sg.Window("Rotation",sub2_layout,finalize=True,size=(400,400))


# 保存データ検索画面
def entry2_searchwindow(x=None,y=None):
  main_layout = [[sg.Text("Season : "),sg.Input(key="Season")],[sg.Text("Tournament : "),sg.Input(key="Tournament")],[sg.Text("Date : "),sg.Input(key="Date")],[sg.Text("Teamf : "),sg.Input(key="Teamf")],[sg.Text("Teams : "),sg.Input(key="Teams")],[sg.Button(" Search ")],[sg.Button(" Continue ",disabled=True)],[sg.Text(key="reading")],[sg.Text(key="filename")],[sg.Text(key="Team1"),sg.Text(key="Team1ab")],[sg.Text(key="Team2"),sg.Text(key="Team2ab")],[sg.Text(key="index")],[sg.Text(key="pld_Team1")],[sg.Text(key="pld_Team2")]]
  return sg.Window("File Read",main_layout,finalize=True,size=(500,500),location=(x,y))



