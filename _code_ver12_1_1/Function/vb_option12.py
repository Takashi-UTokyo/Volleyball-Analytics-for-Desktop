import PySimpleGUI as sg
from _code_ver12_1_1.Function.vb_window12 import Window0


class Option(Window0):
  def __init__(self):
    pass

  def option_update(self,title,msg,func):
    res = self.check(title,msg)
    if res == "OK":
      return func()

  def option(self,title,msg):
    window = self.option_window(title,msg)
    while True:
      event,values = window.read()
      if event ==sg.WIN_CLOSED:
        break
      elif event == "Submit":
        window.close()
        return values["Data"]
    
  def notion(self,title,msg=None):
    if not msg:
      msg = ""
    window = self.option1_window(title,msg)
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        break
      elif event == "OK":
        break
    window.close()
    pass

  def check(self,title,msg):
    window = self.option2_window(title,msg)
    while True:
      event,values = window.read()
      if event == sg.WIN_CLOSED:
        break
      elif event == "OK" or event == "NO":
        break
    window.close()
    return event
