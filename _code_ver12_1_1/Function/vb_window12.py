import PySimpleGUI as sg

class Window0:
  def __init__(self):
    pass

  def Info_window(self):
    Info_layout = [[sg.Text("Season : "),sg.Input(key="Season",size=(10,5))],[sg.Text("Tournament : "),sg.Input(key="Tournament")],[sg.Text("Date : "),sg.Input(key="Date")],[sg.Text("Team1 : "),sg.Input(key="Team1",size=(18,5))],[sg.Text("Team2 : "),sg.Input(key="Team2",size=(18,5))],[],[sg.Button("Set")],[sg.Button(" Continue ",disabled=True)],[sg.Text("",size=(10,5)),sg.Text("-------Player_index-------",key="Info_Set"),sg.Text("",size=(10,5))],[sg.Text("",key="Team1ab")],[sg.Text(key="Team2ab")]]
    return sg.Window("Entry Match Infomation",Info_layout,finalize=True)
  
  def Info_window2(self):
    Info_layout = [[sg.Text("Season : "),sg.Input(key="Season",size=(10,5))],[sg.Text("Tournament : "),sg.Input(key="Tournament")],[sg.Text("Date : "),sg.Input(key="Date")],[sg.Text("Team1 : "),sg.Input(key="Team1",size=(18,5))],[sg.Text("Team2 : "),sg.Input(key="Team2",size=(18,5))],[],[sg.Button("Search")],[sg.Button(" Continue ",disabled=True)],[sg.Text("",size=(10,5)),sg.Text("-------Player_index-------",key="Info_Set"),sg.Text("",key="FileFound",size=(10,5))],[sg.Text("",key="Team1ab")],[sg.Text(key="Team2ab")]]
    return sg.Window("Existed-match data",Info_layout,finalize=True)

  def Set_Info_window(self):
    Team1ab = self.team1_ab
    Team2ab = self.team2_ab
    set_layout = [
      [sg.Text("Set : "),sg.Input(key="Set",size=(5,2))],
      [sg.Text("Serve Team : "),sg.Radio(f"{Team1ab}",key="Team1",group_id="0"),sg.Radio(f"{Team2ab}",key="Team2",group_id="0")],
      [sg.Text(f"{Team1ab} : "),sg.Text("S"),sg.Input(key="Rot1",size=(2,2))],
      [sg.Text("S1:"),sg.Input(key="Team1S1",size=(2,2)),sg.Text("S6:"),sg.Input(key="Team1S6",size=(2,2)),sg.Text("S5:"),sg.Input(key="Team1S5",size=(2,2))],
      [sg.Text("S2:"),sg.Input(key="Team1S2",size=(2,2)),sg.Text("S3:"),sg.Input(key="Team1S3",size=(2,2)),sg.Text("S4:"),sg.Input(key="Team1S4",size=(2,2))],
      [sg.Text(f"{Team2ab}: "),sg.Text("S"),sg.Input(key="Rot2",size=(2,2))],
      [sg.Text("S4:"),sg.Input(key="Team2S4",size=(2,2)),sg.Text("S3:"),sg.Input(key="Team2S3",size=(2,2)),sg.Text("S2:"),sg.Input(key="Team2S2",size=(2,2))],
      [sg.Text("S5:"),sg.Input(key="Team2S5",size=(2,2)),sg.Text("S6:"),sg.Input(key="Team2S6",size=(2,2)),sg.Text("S1:"),sg.Input(key="Team2S1",size=(2,2))],
      [sg.Text(key="msg")],
      [sg.Text(size=(10,2)),sg.Button(" Enter "),sg.Text(size=(10,2))]
      ]
    return sg.Window("Set Information",set_layout,finalize=True)
  
  def option_window(self,title,msg):
    layout = [
      [sg.Text(title)],
      [sg.Text(msg),sg.Input(size=(12,5),key="Data")],
      [sg.Button("Submit")]
    ]
    return sg.Window("Option",layout,finalize=True,size=(200,200))
  
  def option1_window(self,title,msg):
    layout = [
      [sg.Text(title)],
      [sg.Text(msg)],
      [sg.Button("OK")]
    ]
    return sg.Window("Notion",layout,finalize=True,size=(200,200))
  
  def option2_window(self,title,msg):
    layout = [
      [sg.Text(title)],
      [sg.Text(msg)],
      [sg.Button("OK"),sg.Button("NO")]
    ]
    return sg.Window("Check",layout,finalize=True,size=(200,200))
  
  # データ入力メインウィンドウ
  def entry_main(self,x=None, y=None):
    main_layout = [
      [sg.Text("Set: "),sg.Input(key="Set",size=(5,5))],
      [sg.Text("Rally: #"),sg.Input(key="Rally",size=(5,5))],
      [sg.Text("Play_data: "),sg.Input(key="play_data",size=(200,5))],
      [sg.Button("Submit"),sg.Button("SUB")],
      [],[],
      [sg.Text("                                  ----------------------------------------------                ")],
      [sg.Text(size=(25,2)),sg.Text("Data Edition"),sg.Text(size=(25,2))],
      [sg.Text("Set : "),sg.Input(key="-Set-",size=(5,5)),sg.Text("Rally : #"),sg.Input(key="-Rally-",size=(5,5))],
      [sg.Text("Play_data : "),sg.Input(key="-play_data-",size=(200,10))],
      [sg.Button(" Search "),sg.Button(" Edit ",disabled=True)],
      [sg.Button("Save",disabled=True),sg.Button(" Exit ")],
      [sg.Text(" Next Set : "),sg.Button(" Next "),sg.Text(key="Save Condition")]
      ]
    return sg.Window("Data Entry",main_layout,finalize=True,size=(500,400),location=(x,y))

  # データ入力サブウィンドウ
  def entry_sub(self,x=None,y=None):
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
  def entry_sub2(self,x=None,y=None):
    Team1ab = self.team1_ab
    Team2ab = self.team2_ab
    sub2_layout = [
      [sg.Text(f"{Team1ab} vs {Team2ab}")],
      [sg.Input(key="Score1",size=(2,2)),sg.Text(" vs "),sg.Input(key="Score2",size=(2,2))],
      [sg.Text(f"{Team1ab} : "),sg.Radio("Serve",key="Serve1",group_id = "Serve")],
      [sg.Text("S "),sg.Input(key="Rot1",size=(2,2))],
      [sg.Text(),sg.Input(key="Team1S1",size=(2,2)),sg.Text(),sg.Input(key="Team1S6",size=(2,2)),sg.Text(),sg.Input(key="Team1S5",size=(2,2))],
      [sg.Text(),sg.Input(key="Team1S2",size=(2,2)),sg.Text(),sg.Input(key="Team1S3",size=(2,2)),sg.Text(),sg.Input(key="Team1S4",size=(2,2))],
      [sg.Text(f"{Team2ab} : "),sg.Radio("Serve",key="Serve2",group_id = "Serve")],
      [sg.Text("S "),sg.Input(key="Rot2",size=(2,2))],
      [sg.Text(),sg.Input(key="Team2S4",size=(2,2)),sg.Text(),sg.Input(key="Team2S3",size=(2,2)),sg.Text(),sg.Input(key="Team2S2",size=(2,2))],
      [sg.Text(),sg.Input(key="Team2S5",size=(2,2)),sg.Text(),sg.Input(key="Team2S6",size=(2,2)),sg.Text(),sg.Input(key="Team2S1",size=(2,2))]
      ]
    return sg.Window("Rotation",sub2_layout,finalize=True,size=(400,400),location=(x,y))
  
  def index_window(self,x=None,y=None):
    player_heading = ["player_number","player_position","player_name"]
    player_index = ["","",""]
    layout = [
      [sg.Text(" Season : "),sg.Input(key="season",size=(10,5))],
      [sg.Text(" Tournament : "),sg.Input(key="tournament",size=(18,5))],
      [sg.Text(" Team : "),sg.Input(key="team",size=(18,5)),sg.Text(key="team_ab")],
      [sg.Button("Search")],
      [sg.Text(key="IndexFound")],
      [sg.Table(player_index,player_heading,key="index_table")],
      [sg.Text("Number : "),sg.Input(key="player_number",size=(5,5))],
      [sg.Text("Position : "),sg.Input(key="player_position",size=(5,5))],
      [sg.Text("Name : "),sg.Input(key="player_name",size=(18,5))],
      [sg.Button("Submit"),sg.Button("Delete"),sg.Button("Exit")]
    ]
    return sg.Window("Index Create",layout,finalize=True)
  
  def substitution_window(self,x=None,y=None):   
    layout = [
      [sg.Text(f"{self.team1_ab}"),sg.Text("Set : "),sg.Input(key="Set",size=(2,1)),sg.Text("Rally : "),sg.Input(key="Rally",size=(2,1)),sg.Text(f"{self.team2_ab}")],
      [sg.Text("Out : No."),sg.Input(key="Out1",size=(2,1)),sg.Text("          "),sg.Text("Out : No."),sg.Input(key="Out2",size=(2,1))],
      [sg.Text("In : No."),sg.Input(key="In1",size=(2,1)),sg.Text("          "),sg.Text("In : No."),sg.Input(key="In2",size=(2,1))],
      [sg.Button("SUB",key="SUB1"),sg.Text("             "),sg.Button("SUB",key="SUB2")]
    ]
    return sg.Window("Substitution Option",layout,finalize=True,size=(300,200),location=(x,y))

  def analy_window(x=None,y=None):
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




