
# 
from _code_ver11_3_1 import vb_option as vo
from _code_ver11_3_1.Data import vb_stats1 as vs1
from _code_ver11_3_1.Data import vb_stats2 as vs2
from _code_ver11_3_1.Data import vb_plot1 as vp1
from _code_ver11_3_1.Data import vb_plot2 as vp2
from _code_ver11_3_1 import vb_file as vf

import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


plt.rcParams['font.family'] = 'Arial'
plt.rcParams["font.size"] = 20 


# メインウィンドウ動作
def analy_main(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2):
  data_p,data_p1,data_p2,Team1ab,Team2ab = vf.team_index(Season_path,Tournament_path,Team1,Team2)
  main_window = analy_window(Team1ab,Team2ab,700,200)
  for x in range(0,5):
    try:
      main_window[f"Score{x+1}1"].update(Set_Result[x]["Score1"])
    except:
      main_window[f"Score{x+1}1"].update("0")
    try:
      main_window[f"Score{x+1}2"].update(Set_Result[x]["Score2"])
    except:
      main_window[f"Score{x+1}2"].update("0")
  while True:
    event,values = main_window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
      res = vo.checkWin("Analytics Close","Analytics Close ?")
      if res == "OK":
        break
      else:
        pass
    elif event == "Save":
      res = vo.checkWin("Confirm"," File Save ?")
      if res == "OK":
        vf.fileInfosave(Season_path,Tournament_path,date_path,Team1,Team2,Set_Result)
        vf.filesave(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
        pass
    elif event == "Stats":
      stats_analy(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
      pass
    elif event == "Plot":
      plot_analy(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
      pass
    elif event == "OK":
      score1,score2,serve1,serve2,attack1,attack2,block1,block2,OE1,OE2 = score_action(values['List'],df)
      main_window["Score1"].update(score1)
      main_window["Score2"].update(score2)
      main_window["Serve1"].update(serve1)
      main_window["Serve2"].update(serve2)
      main_window["Attack1"].update(attack1)
      main_window["Attack2"].update(attack2)
      main_window["Block1"].update(block1)
      main_window["Block2"].update(block2)
      main_window["OE1"].update(OE1)
      main_window["OE2"].update(OE2)
      pass
    elif event == "BP":
      bp_analy(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2)
      pass
  main_window.Close()

# メインウィンドウ -セット別項目別得点の表示動作
def score_action(Set,df):
  if Set:
    try:
      set = int(Set[0])
    except:
      set = ""
  elif not Set:
    set = ""
  serve1 = vs1.action1(df,set,"","","s","p")
  serve2 = vs2.action2(df,set,"","","s","p")
  attack1 = vs1.action1(df,set,"","","a","p")
  attack2 = vs2.action2(df,set,"","","a","p")
  block1 = vs1.action1(df,set,"","","b","p")
  block2 = vs2.action2(df,set,"","","b","p")
  OE1 = (vs2.action2(df,set,"","","s","m") + vs2.action2(df,set,"","","a","m") - vs1.action1(df,set,"","","b","p") + vs2.action2(df,set,"","","m",""))
  OE2 = (vs1.action1(df,set,"","","s","m") + vs1.action1(df,set,"","","a","m") - vs2.action2(df,set,"","","b","p") + vs1.action1(df,set,"","","m",""))
  score1 = sum([serve1,attack1,block1,OE1])
  score2 = sum([serve2,attack2,block2,OE2])
  return score1,score2,serve1,serve2,attack1,attack2,block1,block2,OE1,OE2

# ブレイクポイント解析
def bp_analy(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2):
  window = bp_window(Team1,Team2)
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == "OK":
      df_bp1 = vs1.bp1(values["Set"][0],df,fRotTeam01,Set_Info)
      for i in range(1,7):
        for x in ["a","s","b","o","error"]:
          if x == "error":
            number = df_bp1[(df_bp1["bRot1"] == str(i)) & (df_bp1["action"] == x)]
            if len(number) != 0:
              vo.errorWin(f"{Team1} S{i} Error ::Rally{number["Rally"].reset_index(drop=True)[0]}")
          else:
            number = df_bp1[(df_bp1["bRot1"] == str(i)) & (df_bp1["action"] == x)]
            window[f"{x}b1{i}"].update(len(number))
      df_bp2 = vs2.bp2(values["Set"][0],df,fRotTeam02,Set_Info)
      for i in range(1,7):
        for x in ["a","s","b","o","error"]:
          if x == "error":
            number = df_bp2[(df_bp2["bRot2"] == str(i)) & (df_bp2["action"] == x)]
            if len(number) != 0:
              vo.errorWin(f"{Team2} S{i} Error ::Rally{number["Rally"].reset_index(drop=True)[0]}")
          else:
            number = df_bp2[(df_bp2["bRot2"] == str(i)) & (df_bp2["action"] == x)]
            window[f"{x}b2{i}"].update(len(number))
      pass
  window.close()

# プロット解析
def plot_analy(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2):
  window = plot_window(700,200)
  # fig,ax = plt.subplots(figsize=(10,10))
  # ax.set_facecolor("navajowhite")
  def draw_figure(canvas, figure):
    canvas = window["-CANVAS-"].TKCanvas
    figure_canvas = FigureCanvasTkAgg(figure, canvas)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas
  while True:
    event,values = window.read()
    
    if event == "Exit" or event == sg.WINDOW_CLOSED:
      break
    elif event == "Submit":
      if values["Mode"] == ["Serve"]:
        action = "s"
      elif values["Mode"] == ["Attack"]:
        action = "a"
      elif values["Mode"] == ["Reception"]:
        action = "r"
      elif values["Mode"] == ["Setting"]:
        action = "t"
      if not values["Set"] or values["Set"][0] == "None":
        set = ""
      else:
        set = int(values["Set"][0])
      if not values["Slot"] or values["Slot"][0] == "None":
        slot = ""
      else:
        slot = str(values["Slot"][0])
      # try:
      #   set = int(values["Set"][0])
      # except:
      #   set = ""
      # try:
      #   slot = int(values["Slot"][0])
      # except:
      #   slot = ""
      try:
        number = int(values["No."])
      except:
        number = ""
      if action in ["s","a","r"]: 
        if values["Team"] == ["Team1"]:  
          fig,ax = vp1.makeplot1(df,Team1,set,slot,number,action)
          fig_agg = draw_figure(window["-CANVAS-"].TKCanvas,fig)
        elif values["Team"] == ["Team2"]:
          fig,ax = vp2.makeplot2(df,Team2,set,slot,number,action)
          fig_agg = draw_figure(window["-CANVAS-"].TKCanvas,fig)
        window["Save"].update(disabled=False)
        pass
      elif action == "t":
        if values["Team"] == ["Team1"]:
          fig,ax = vp1.tmakeplot1(df,Team1,set,number)
          fig_agg = draw_figure(window["-CANVAS-"].TKCanvas,fig)
        elif values["Team"] == ["Team2"]:
          fig,ax = vp2.tmakeplot2(df,Team2,set,number)
          fig_agg = draw_figure(window["-CANVAS-"].TKCanvas,fig)
        window["Save"].update(disabled=False)
        pass
      else:
        vo.errorWin("<< Figure Cannot Made >>")
        pass
    elif event == "Clear":
      # plt.clf()
      # fig_agg = draw_figure(window["-CANVAS-"].TKCanvas,fig)
      pass
    elif event == "Save":
      pass
  window.close()

# スタッツ解析
def stats_analy(Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,sub_condition1,sub_condition2,fRotTeam01,fRotTeam02,fRot1,fRot2):
  data_p,data_p1,data_p2,Team1ab,Team2ab = vf.team_index(Season_path,Tournament_path,Team1,Team2)
  window = stats_window(Team1,Team2,0,150)
  dfs1 = vs1.Tstats1(data_p1,df,"")
  dfs2 = vs2.Tstats2(data_p2,df,"")
  Tstats1 = [[dfs1.iat[y,x] for x in range(0,len(dfs1.columns))] for y in range(0,len(dfs1)-1)]
  Tstats2 = [[dfs2.iat[y,x] for x in range(0,len(dfs2.columns))] for y in range(0,len(dfs2)-1)]
  window["stats1"].update(Tstats1)
  window["stats2"].update(Tstats2)
  Tstats1all = [[dfs1.iat[len(dfs1)-1,x] for x in range(0,len(dfs1.columns))]]
  Tstats2all = [[dfs2.iat[len(dfs2)-1,x] for x in range(0,len(dfs2.columns))]]
  window["stats1all"].update(Tstats1all)
  window["stats2all"].update(Tstats2all)
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
      break
    elif event == "Display":
      pop_stats(data_p1,data_p2,df,dfs1,dfs2,Team1,Team2,values)
      pass
  window.close()

# ポップスタッツ表
def pop_stats(data_p1,data_p2,df,dfs1,dfs2,Team1,Team2,values):
  columns = ["Name","No.","Position"]
  if values["Set"]:
    set = int(values["Set"])
    dfs1 = vs1.Tstats1(data_p1,df,set)
    dfs2 = vs2.Tstats2(data_p2,df,set)
  else:
    set = ""
    dfs1 = vs1.Tstats1(data_p1,df,set)
    dfs2 = vs2.Tstats2(data_p2,df,set)
  if values["-Serve-"]:
    columnS = ["s-All","s-Point","s-Effective","s-Miss","s-success"]
    for i in range(0,len(columnS)):
      columns.append(columnS[i])
  if values["-Attack-"]:
    columnA = ["a-All","a-Point","a-Effective","a-Miss","a-success"]
    for i in range(0,len(columnA)):
      columns.append(columnA[i])
  if values["-Block-"]:
    columnB = ["b-All","b-Point","b-Effective","b-Miss","b-success"]
    for i in range(0,len(columnB)):
      columns.append(columnB[i])
  if values["-Reception-"]:
    columnR = ["r-All","r-A","r-B","r-Miss","r-success"]
    for i in range(0,len(columnR)):
      columns.append(columnR[i])
  if values["-Dig-"]:
    columnD = ["d-All","d-Miss","d-success"]
    for i in range(0,len(columnD)):
      columns.append(columnD[i])
  if values["-Miss-"]:
    columnM = ["m-All"]
    columns.append(columnM[0])
  try:
    dfs11 = dfs1.loc[:,columns]
    Tstats11 = [[dfs11.iat[y,x] for x in range(0,len(dfs11.columns))] for y in range(0,len(dfs11))]
    dfs21 = dfs2.loc[:,columns]
    Tstats21 = [[dfs21.iat[y,x] for x in range(0,len(dfs21.columns))] for y in range(0,len(dfs21))]
  except:
    vo.errorWin("<< Data Not Found >>")
  else:
    window = stats_pop_window(Tstats11,Tstats21,columns,Team1,Team2,0,300)
    window["Set"].update(set)
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED or event == "-Exit-":
        break
    window.close()
  

#ウィンドウ

# メインウィンドウ
def analy_window(Team1,Team2,x=None,y=None):
  match_col = [
    [sg.Frame('Set Result',[
      [sg.Text(f"  {Team1}  ",key="Team1",font=("Arial",10)),sg.Text("  Set  ",font=("Arial",10)),sg.Text(f"  {Team2}  ",key="Team2",font=("Arial",10))],
      [sg.Text(size=(1,1)),sg.Input(key="Score11",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1)),sg.Text("  1  ",font=("Arial",10)),sg.Text(size=(1,1)),sg.Input(key="Score12",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1))],
      [sg.Text(size=(1,1)),sg.Input(key="Score21",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1)),sg.Text("  2  ",font=("Arial",10)),sg.Text(size=(1,1)),sg.Input(key="Score22",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1))],
      [sg.Text(size=(1,1)),sg.Input(key="Score31",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1)),sg.Text("  3  ",font=("Arial",10)),sg.Text(size=(1,1)),sg.Input(key="Score32",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1))],
      [sg.Text(size=(1,1)),sg.Input(key="Score41",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1)),sg.Text("  4  ",font=("Arial",10)),sg.Text(size=(1,1)),sg.Input(key="Score42",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1))],
      [sg.Text(size=(1,1)),sg.Input(key="Score51",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1)),sg.Text("  5  ",font=("Arial",10)),sg.Text(size=(1,1)),sg.Input(key="Score52",size=(3,3),font=("Arial",10)),sg.Text(size=(1,1))]])
    ]
  ]
  set_listbox = ["All","1","2","3","4","5"]
  set_col = [
    [sg.Frame("Set Detail",[
      [sg.Text("Set : "),sg.Listbox(set_listbox,key="List",font=("Arial",10)),sg.OK(),sg.Button("BP")],
      [sg.Text("Score",font=("Arial",10),size=(5,1)),sg.Input(key="Score1",size=(3,3),font=("Arial",10)),sg.Input(key="Score2",size=(3,3),font=("Arial",10))],
      [sg.Text("             ---------------             ")],
      [sg.Text("Serve",font=("Arial",10),size=(5,1)),sg.Input(key="Serve1",size=(3,3),font=("Arial",10)),sg.Input(key="Serve2",size=(3,3),font=("Arial",10))],
      [sg.Text("Attack",font=("Arial",10),size=(5,1)),sg.Input(key="Attack1",size=(3,3),font=("Arial",10)),sg.Input(key="Attack2",size=(3,3),font=("Arial",10))],
      [sg.Text("Block",font=("Arial",10),size=(5,1)),sg.Input(key="Block1",size=(3,3),font=("Arial",10)),sg.Input(key="Block2",size=(3,3),font=("Arial",10))],
      [sg.Text("OE",font=("Arial",10),size=(5,1)),sg.Input(key="OE1",size=(3,3),font=("Arial",10)),sg.Input(key="OE2",size=(3,3),font=("Arial",10))]])
    ]
  ]

  function_col = [[sg.Button("Stats"),sg.Button("Plot"),sg.Text("                  ")],[sg.Button("Save",key="Save",size=(4,1),font=("Arial",10))]]

  close_col = sg.Column([[sg.Text("")],[sg.Text("                  "),sg.Button("Exit",key="Exit")],[sg.Text("")]])

  left_col = [match_col,function_col]

  main_layout = [[sg.Column(match_col),sg.Column(set_col)],[sg.Column(function_col),close_col]]

  return sg.Window("Match result",main_layout,finalize=True,size=(450,350),location=(x,y))


# プロット画面
def plot_window(x=None,y=None):
  listbox_Team = ["Team1","Team2"]
  listbox_mode = ["Serve","Attack","Reception","Setting"]
  listbox_set = ["None","1","2","3","4","5"]
  listbox_slot = ["None","51","21","11","a1","c1","52","22","12","a2","c2","53","13","c3"]
  plot_col = [[sg.Text("Plot Analytics")],
              [sg.Text("Team : "),sg.Listbox(listbox_Team,key="Team")],
              [sg.Text("Mode : "),sg.Listbox(listbox_mode,key="Mode")],
              [sg.Text("Set : "),sg.Listbox(listbox_set,key="Set")],
              [sg.Text("Slot : "),sg.Listbox(listbox_slot,key="Slot")],
              [sg.Text("No. : "),sg.Input(key="No.",size=(3,3)),sg.Button("Submit",key="Submit"),sg.Button("Clear",key="Clear"),sg.Button("Exit",key="Exit"),sg.Button("Save",key="Save",disabled=True)],
              [sg.Canvas(key="-CANVAS-",size=(100,100))]
              ]
  return sg.Window("Plot Analytics",plot_col,size=(1000,1000),finalize=True,location=(x,y),resizable = True)

# スタッツ画面
def stats_window(Team1,Team2,x=None,y=None):
  Tstats1 = [[]]
  Tstats2 = [[]]
  Tstats1all = [[]]
  Tstats2all = [[]]
  head_stats = ["Name","No.","Position","s-All","s-Point","s-Effective","s-Miss","s-success","a-All","a-Point","a-Effective","a-Miss","a-success","b-All","b-Point","b-Effective","b-Miss","b-success","r-All","r-A","r-B","r-Miss","r-success","d-All","d-Miss","d-success","m-All"]
  option_col = [
    [sg.Text("Stats Analytics")],
    [sg.Text("Set : "),sg.Input(key="Set",size=(2,1)),sg.Button("Display",key="Display"),sg.Button("Exit",key="Exit")],
    [sg.Checkbox("Serve",key="-Serve-"),sg.Checkbox("Attack",key="-Attack-"),sg.Checkbox("Block",key="-Block-"),sg.Checkbox("Reception",key="-Reception-"),sg.Checkbox("Dig",key="-Dig-"),sg.Checkbox("Miss",key="-Miss-")]
  ]
  stats1 = [
    [sg.Text(f"{Team1}")],
    [sg.Table(Tstats1,head_stats,background_color='white',text_color='black',key="stats1",font=("Arial",8),def_col_width=6,auto_size_columns=False)],
    [sg.Table(Tstats1all,head_stats,background_color='white',size=(1,1),text_color='black',key="stats1all",font=("Arial",8),def_col_width=6,auto_size_columns=False)]      
  ]
  stats2 = [
    [sg.Text(f"{Team2}")],
    [sg.Table(Tstats2,head_stats,background_color='white',text_color='black',key="stats2",font=("Arial",8),def_col_width=6,auto_size_columns=False)],
    [sg.Table(Tstats2all,head_stats,background_color='white',size=(1,1),text_color='black',key="stats2all",font=("Arial",8),def_col_width=6,auto_size_columns=False)]
  ]
  main_layout = [option_col,stats1,stats2]
  return sg.Window("Stats Analytics",main_layout,finalize=True,location=(x,y))
# スタッツポップ画面
def stats_pop_window(Tstats11,Tstats21,columns,Team1,Team2,x=None,y=None):
  layout = [
    [sg.Text("Set : "),sg.Text("",key="Set"),sg.Text("       "),sg.Button("Exit",key="-Exit-")],
    [sg.Text(f"{Team1}")],
    [sg.Table(Tstats11,columns,key="-Stats1-",font=("Arial",8),def_col_width=6,auto_size_columns=False )],
    [sg.Text(f"{Team2}")],
    [sg.Table(Tstats21,columns,key="-Stats1-",font=("Arial",8),def_col_width=6,auto_size_columns=False )]
  ]
  return sg.Window("Stats",layout,finalize=True,location=(x,y))

# ブレイクポイント画面
def bp_window(Team1,Team2,x=None,y=None):
  set_listbox = ["All","1","2","3","4","5"]
  credit = [
    [sg.Text(f"{Team1}  vs  {Team2}"),sg.Text("    Set : "),sg.Listbox(set_listbox,key="Set"),sg.OK()]
  ]
  col1 = [
    [sg.Text(f"{Team1}")],
    [sg.Text("     "),sg.Text("attack"),sg.Text("serve"),sg.Text("block"),sg.Text("OE")],
    [sg.Text("S1 : "),sg.Input(key="ab11",size=(2,2)),sg.Input(key="sb11",size=(2,2)),sg.Input(key="bb11",size=(2,2)),sg.Input(key="ob11",size=(2,2))],
    [sg.Text("S2 : "),sg.Input(key="ab12",size=(2,2)),sg.Input(key="sb12",size=(2,2)),sg.Input(key="bb12",size=(2,2)),sg.Input(key="ob12",size=(2,2))],
    [sg.Text("S3 : "),sg.Input(key="ab13",size=(2,2)),sg.Input(key="sb13",size=(2,2)),sg.Input(key="bb13",size=(2,2)),sg.Input(key="ob13",size=(2,2))],
    [sg.Text("S4 : "),sg.Input(key="ab14",size=(2,2)),sg.Input(key="sb14",size=(2,2)),sg.Input(key="bb14",size=(2,2)),sg.Input(key="ob14",size=(2,2))],
    [sg.Text("S5 : "),sg.Input(key="ab15",size=(2,2)),sg.Input(key="sb15",size=(2,2)),sg.Input(key="bb15",size=(2,2)),sg.Input(key="ob15",size=(2,2))],
    [sg.Text("S6 : "),sg.Input(key="ab16",size=(2,2)),sg.Input(key="sb16",size=(2,2)),sg.Input(key="bb16",size=(2,2)),sg.Input(key="ob16",size=(2,2))]
  ]
  col2 = [
    [sg.Text(f"{Team2}")],
    [sg.Text("     "),sg.Text("attack"),sg.Text("serve"),sg.Text("block"),sg.Text("OE")],
    [sg.Text("S1 : "),sg.Input(key="ab21",size=(2,2)),sg.Input(key="sb21",size=(2,2)),sg.Input(key="bb21",size=(2,2)),sg.Input(key="ob21",size=(2,2))],
    [sg.Text("S2 : "),sg.Input(key="ab22",size=(2,2)),sg.Input(key="sb22",size=(2,2)),sg.Input(key="bb22",size=(2,2)),sg.Input(key="ob22",size=(2,2))],
    [sg.Text("S3 : "),sg.Input(key="ab23",size=(2,2)),sg.Input(key="sb23",size=(2,2)),sg.Input(key="bb23",size=(2,2)),sg.Input(key="ob23",size=(2,2))],
    [sg.Text("S4 : "),sg.Input(key="ab24",size=(2,2)),sg.Input(key="sb24",size=(2,2)),sg.Input(key="bb24",size=(2,2)),sg.Input(key="ob24",size=(2,2))],
    [sg.Text("S5 : "),sg.Input(key="ab25",size=(2,2)),sg.Input(key="sb25",size=(2,2)),sg.Input(key="bb25",size=(2,2)),sg.Input(key="ob25",size=(2,2))],
    [sg.Text("S6 : "),sg.Input(key="ab26",size=(2,2)),sg.Input(key="sb26",size=(2,2)),sg.Input(key="bb26",size=(2,2)),sg.Input(key="ob26",size=(2,2))]
  ]
  main_layout = [credit,[sg.Column(col1),sg.Column(col2)]]
  return sg.Window("Break Point", main_layout,finalize=True,location=(x,y))

# フルデータ画面
