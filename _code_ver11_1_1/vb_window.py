from _code_ver11_1_1 import vb_entry as ve
from _code_ver11_1_1 import vb_file as vf
from _code_ver11_1_1 import vb_option as vo
from _code_ver11_1_1 import vb_data as vd
from _code_ver11_1_1 import vb_plot as vp
from _code_ver11_1_1 import vb_stats as vs



import PySimpleGUI as sg


# 入力・検索の選択画面
def Start_window():
  listbox = ["ENTRY MODE","SEARCH MODE"]
  start_layout = [[sg.Text(size=(15,1)),sg.Text(" --VOLLEYBALL ANALYTICS-- ",size=(25,1)),sg.Text(size=(15,1))],[sg.Text(size=(20,2))],[sg.Text("MODE : "),sg.Listbox(listbox,size=(20,len(listbox)+1),key="LIST")],[sg.Text(size=(20,1)),sg.Button("SELECT"),sg.Text(size=(20,1))]]
  return sg.Window("  VOLLEYBALL ANALYTICS  ",start_layout,size=(500,300),finalize=True)

# 1入力に対応
def select_start():
  entryS = entry_selectwindow()
  while True:
    event,values = entryS.read()
    if event == "Select":
      break
  entryS.close()
  if values["List"] == ["New Entry"]:
    Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2 = ve.entry_df()
  elif values["List"] == ["Saved Data Entry"]:
    Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,play_d,df,df_Team1,df_Team2 = ve.entry2_df()
  return Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2

# 入力選択ウィンドウ
def entry_selectwindow():
  listbox = ["New Entry","Saved Data Entry"]
  entry2_layout = [[sg.Text("Option"),sg.Listbox(listbox,size=(10,3),key="List")],[sg.Button("Select")]]
  return sg.Window("Entry Option",entry2_layout,size=(300,200),finalize=True)

# 1--1 新規入力後データ分析
  # リザルトホーム画面 -- vb_plotの選択
    # dfとスコア、スタッツ表、ブレイクポイント
  # データの保存



# 2検索に対応



# 
# def make_main(x=None,y=None):
#   main_layout = [[sg.Text("Season : "),sg.Input(key="Season")],[sg.Text("Tournament : "),sg.Input(key="Tournament")],[sg.Text("Date : "),sg.Input(key="Date")],[sg.Text("Teamf : "),sg.Input(key="Teamf")],[sg.Text("Teams : "),sg.Input(key="Teams")],[sg.Button(" Search ")],[sg.Button(" Continue ",disabled=True)],[sg.Text(key="reading")],[sg.Text(key="filename")],[sg.Text(key="Team1"),sg.Text(key="Team1ab")],[sg.Text(key="Team2"),sg.Text(key="Team2ab")],[sg.Text(key="index")],[sg.Text(key="pld_Team1")],[sg.Text(key="pld_Team2")]]
#   return sg.Window("File Read",main_layout,finalize=True,size=(500,500),location=(x,y))


# 実行
start = Start_window()
while True:
  event,values = start.read()
  if event == sg.WIN_CLOSED:
    break
  elif event == "SELECT":
    break
start.close()
if values["LIST"] == ["ENTRY MODE"] :
  Season_path,Tournament_path,date_path,Team1,Team2,Set_Info,Set_Result,Set,play_d,df,df_Team1,df_Team2 = select_start()