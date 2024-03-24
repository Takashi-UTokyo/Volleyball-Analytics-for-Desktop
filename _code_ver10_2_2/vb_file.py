import pandas as pd
import os  
import PySimpleGUI as sg
from time import sleep
# 別ウィンドウで[フォルダー名]、[ファイル名]、[チーム名1]、[チーム名2]を入力したい



def make_main(x=None,y=None):
  main_layout = [[sg.Text("Season : "),sg.Input(key="Season")],[sg.Text("Tournament : "),sg.Input(key="Tournament")],[sg.Text("Date : "),sg.Input(key="Date")],[sg.Text("Teamf : "),sg.Input(key="Teamf")],[sg.Text("Teams : "),sg.Input(key="Teams")],[sg.Button("Search")],[sg.Text(key="reading")],[sg.Text(key="filename")],[sg.Text(key="Team1"),sg.Text(key="Team1ab")],[sg.Text(key="Team2"),sg.Text(key="Team2ab")],[sg.Text(key="index")],[sg.Text(key="pld_Team1")],[sg.Text(key="pld_Team2")]]
  return sg.Window("File Read",main_layout,finalize=True,size=(500,500),location=(x,y))

window = make_main()
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == "Search":
      try:
        Season_path =r"{}".format(values["Season"])
        Tournament_path = r"{}".format(values["Tournament"])
        date_path = r"{}".format(values["Date"])
        Teamf_path = r"{}".format(values["Teamf"])
        Teams_path = r"{}".format(values["Teams"])
        folder_path = Season_path + " " + Tournament_path
        filename_path = date_path +" "+ Teamf_path + " vs " + Teams_path + " " + "Full Score.xlsx"
        path = r"C:\Volleyball"
        file_path = os.path.join(path,folder_path,filename_path)
        df = pd.read_excel(file_path, sheet_name="Full Score",index_col=None)
        sleep(3)
        df = df.drop(columns=df.columns[range(14,30)])
        Team1ab = df.columns[12]
        Team2ab = df.columns[13]
        msg = "<< FileRead Success! >> :"
        window["reading"].update(f"{msg}{folder_path}")
        window["filename"].update(f"File : {filename_path}")
        window["Team1ab"].update(f"Team1ab : {Team1ab}")
        window["Team2ab"].update(f"Team2ab : {Team2ab}")
      except:
        msg = "<< FileRead Failed! - RE-ENTER >>"
        print(msg)
        window["reading"].update(f"{msg}")
# window.close()  

print(msg,file_path)


# 必要情報の抽出

# df = df.drop(columns=df.columns[range(14,30)])
Team1ab = df.columns[12]
Team2ab = df.columns[13]
print("Team1ab:",Team1ab)
print("Team2ab:",Team2ab)
df_Score = pd.concat([df["Set"],df[Team1ab],df[Team2ab]],axis=1).dropna()
df_Team1 = df[df.columns[range(2,7)]]
df_Team2 = df[df.columns[range(7,12)]]
df_Rally = df[df.columns[range(0,2)]]
df_Team1 = pd.concat([df_Rally,df_Team1],axis=1)
df_Team2 = pd.concat([df_Rally,df_Team2],axis=1)

# 各チームのプレーデータフレーム作成



# データ保存に関する処理
  # pythonで入力したデータをcsvまたはxlsxとして保存


# 検索に関する処理
  # プレイヤーデータの読み込み
try:
  data_p = pd.read_excel(r"C:\Volleyball\Player_index\Player_index.xlsx", sheet_name=Tournament_path,index_col=None)
  window["index"].update("<< Player Index Success ! >> ")
except:
  window["index"].update("<< Player Index Failed -- Not Found >>")
try:
  data_p1 = data_p[(data_p["Season"].astype(str)==Season_path) & (data_p["Abbreviation"]==Team1ab)].reset_index(drop=True)
  data_p1.at[0,"Abbreviation"]
  window["pld_Team1"].update(f"Team1 : {Team1ab}")
except:
  window["pld_Team1"].update(f"Team1 : << Not Found >>")
try:
  data_p2 = data_p[(data_p["Season"]==Season_path) & (data_p["Abbreviation"]==Team2ab)].reset_index(drop=True)
  window["pld_Team2"].update(f"Team2 : {Team2ab}")
  data_p2.at[0,"Abbreviation"]
except:
  window["pld_Team2"].update("Team2 : << Not Found >>")

  # 選手の所属データの取得
  # 所属データの検索
