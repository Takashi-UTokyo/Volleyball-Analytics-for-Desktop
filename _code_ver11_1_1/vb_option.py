import pandas as pd
import PySimpleGUI as sg




# エラー画面表示
def errorWin(msg):
  errorWin = error_window(msg)
  while True:
    event,values = errorWin.read()
    if event == sg.WIN_CLOSED or event == "OK":
      break
  return errorWin.close()

# エラーウィンドウ
def error_window(msg):
  error_layout = [[sg.Text(size=(8,3)),sg.Text(msg),sg.Text(size=(8,3))],[sg.Text(size=(10,3)),sg.Text(),sg.Button("OK",key="OK",size=(6,3)),sg.Text(size=(10,3))]]
  return sg.Window("  Error Found  ",error_layout,finalize=True,size=(300,100))

# 完了画面表示
def optionWin(title,msg):
  optionWin = option_window(title,msg)
  while True:
    event,values = optionWin.read()
    if event == sg.WIN_CLOSED or event == "OK":
      break
  return optionWin.close()
# 完了ウィンドウ
def option_window(title,msg):
  option_layout = [[sg.Text(size=(8,3)),sg.Text(msg),sg.Text(size=(8,3))],[sg.Text(size=(10,3)),sg.Text(),sg.Button("OK",key="OK",size=(6,3)),sg.Text(size=(10,3))]]
  return sg.Window(title,option_layout,finalize=True,size=(300,100))

# 確認画面表示
def checkWin(title,msg):
  checkWin = check_window(title,msg)
  while True:
    event,values = checkWin.read()
    if event == "OK":
      res = "OK"
      break
    elif event == sg.WIN_CLOSED or event == "NO":
      res = "NO"
      break
  checkWin.close()
  return res
# 確認ウィンドウ
def check_window(title,msg):
  check_layout = [[sg.Text(size=(8,3)),sg.Text(msg),sg.Text(size=(8,3))],[sg.Text(size=(5,3)),sg.Text(),sg.Button("OK",size=(6,3)),sg.Button("NO",size=(6,3)),sg.Text(size=(5,3))]]
  return sg.Window(title,check_layout,finalize=True,size=(300,100))
