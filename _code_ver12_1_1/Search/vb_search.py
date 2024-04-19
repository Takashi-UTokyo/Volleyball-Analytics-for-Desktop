import PySimpleGUI as sg
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from _code_ver12_1_1.Function import vb_option as vo
from _code_ver12_1_1.Data import vb_stats1 as vs1
from _code_ver12_1_1.Data import vb_stats2 as vs2
from _code_ver12_1_1.Data import vb_plot1 as vp1
from _code_ver12_1_1.Data import vb_plot2 as vp2
from _code_ver12_1_1.Data import vb_file as vf


Team = 'Allianz Milano'
df_search = vf.team_search_option(Team)


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
        df_search = vf.team_search_option(values["Team"])
        filelist = choose_file(df_search)
        df_all = vf.team_search(Team,filelist)
        break
      except:
        window = Team_window()
    else:
      window.close()
      break
  return df_all


# ファイル選択(保存ファイルの中から選択したファイルのみ読み込む)
def choose_file(df_search):
  window,file_info = choose_file_window(df_search)
  filepath0 = r"C:\Volleyball"
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == "Submit":
      filelist = []
      for value in values['-List-']:
        file = file_info[file_info.index(list(filter(lambda d:r'{season} {tournament}\{date} {teamf} vs {teams} Full scorepy.xlsx'.format(season=d['season'],tournament=d['tournament'],date=d['date'],teamf=d['teamf'],teams=d['teams'])==value,file_info))[0])]
        filelist.append(file)
      break
  window.close()
  return filelist



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
def choose_file_window(df_search):
  filelist = []
  file_info = []
  for i in range(len(df_search)):
    season = df_search.at[i,"Season"]
    tournament = df_search.at[i,"Tournament"]
    date = df_search.at[i,"date"]
    teamf = df_search.at[i,"Teamf"]
    teams = df_search.at[i,"Teams"]
    filename = r"{season} {tournament}\{date} {teamf} vs {teams} Full scorepy.xlsx".format(season=season,tournament=tournament,date=date,teamf=teamf,teams=teams)
    filelist.append(filename)
    fileinfo = {
      'season':season,
      'tournament':tournament,
      'date':date,
      'teamf':teamf,
      'teams':teams
    }
    file_info.append(fileinfo)
  layout = [
    [sg.Text("file list :")],
    [sg.Listbox(filelist,select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,size=(60,len(filelist)),key="-List-")],
    [sg.Button("Submit")]
  ]
  return sg.Window("file for Analytics",layout,finalize=True),file_info




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
  df_all

