import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from _code_ver11_2_1.Function import vb_option as vo
from _code_ver11_2_1.Analytics import vb_stats1 as vs1
from _code_ver11_2_1.Analytics import vb_stats2 as vs2
from _code_ver11_2_1.Analytics import vb_plot1 as vp1
from _code_ver11_2_1.Analytics import vb_plot2 as vp2
from _code_ver11_2_1.Function import vb_file as vf


# 検索初期画面


# チーム選択
def Search_Team():
  window = Team_window()
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == "Submit":
      window.close()
      try:
        df_all = vf.team_search(values["Team"])
        break
      except:
        window = Team_window()
    else:
      window.close()
      break
  return df_all


# ファイル選択(保存ファイルの中から選択したファイルのみ読み込む)
# 解析

# 

# ウィンドウ

# モード選択ウィンドウ
def search_start(x=None,y=None):
  list_mode = ["Search Player","Search Team"]
  layout = [
    [sg.Text("Search Mode Select")],
    [sg.Text(" Mode :"),sg.Listbox(list_mode,key="mode",size=(20,len(list_mode)))],
    [sg.Button("Submit")],
  ]
  return sg.Window("SEARCH MODE",layout,size=(500,300),location=(x,y),finalize=True)


# 　　プレイヤー検索ウィンドウ

#     チーム検索ウィンドウ
def Team_window(x=None,y=None):
  layout = [
    [sg.Text("Team Select")],
    [sg.Text("Team name : "),sg.Input(key="Team",size=(20,1))],
    [sg.Button("Submit")],
  ]
  return sg.Window("Team Search Mode",layout,size=(300,200),finalize=True,location=(x,y))

# 　　ファイル選択ウィンドウ


# 　　解析ウィンドウ


if __name__ == '__main__':
  search_window = search_start()
  while True:
    event,values = search_window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == "Submit":
      if values["mode"][0] == "Search Team":
        search_window.close()
        try:
          df_all = Search_Team()
          break          
        except:
          search_window = search_start()

