
class DataConversion:
  def __init__(self):
    pass

  def zone2int(self,zone):
    if type(zone) is list:
      zone0 = zone
    else:
      zone0 = [zone]
    zone01 = []
    for zone00 in zone0:
      if type(zone00) is str:
        if "a" in zone00:
          zone1 = -1
        elif "b" in zone00:
          zone1 = -2
        elif "c" in zone00:
          zone1 = -3
        else:
          zone1 = zone00[0]
        zone2 = zone00[1:]
        zone3 = int(str(zone1)+zone2)
      elif type(zone00) is int:
        zone3 = zone00
      zone01.append(zone3)
    if type(zone) is str:
      zone01 = zone01[0]

    return zone01


  def play2trans(self,play_d: list) -> list:
    trans_d = []
    for play_d_ in play_d:
      trans_dall = play_d_["play_data"].split("/")
      for t_number0 in range(0,len(trans_dall)):
        trans_d_ = {
          "Set":play_d_["Set"],
          "Rally":play_d_["Rally"],
          "transition":t_number0+1,
          "trans_data":trans_dall[t_number0]
        }
        trans_d.append(trans_d_)
    return trans_d

  def play2motion(self,play_d: list) -> list: 
    motion_d = []
    for play_d_ in play_d:
      trans_dall = play_d_["play_data"].split("/")
      for t_number0 in range(len(trans_dall)):
        motion_all = trans_dall[t_number0].split(":")
        for m_number0 in range(len(motion_all)):
          motion_d_ = {
            "Set":play_d_["Set"],
            "Rally":play_d_["Rally"],
            "transition":t_number0+1,
            "motion":m_number0+1,
            "motion_data":motion_all[m_number0]
          }
          motion_d.append(motion_d_)
    return motion_d

  def play2command(self,play_d: list) -> list:
    command_d = []
    for play_d_ in play_d:
      trans_dall = play_d_["play_data"].split("/")
      for t_number0 in range(len(trans_dall)):
        motion_dall = trans_dall[t_number0].split(":")
        for m_number0 in range(len(motion_dall)):
          command_dall = motion_dall[m_number0].split(" ")
          if not command_dall[0]:
            command_d_ = {
              "Set":play_d_["Set"],
              "Rally":play_d_["Rally"],
              "transition":t_number0+1,
              "motion":m_number0+1,
              "No":"",
              "action":"",
              "result":"",
              "zone":""
            }
            command_d.append(command_d_)
            continue
          No = int(command_dall[0])
          action = command_dall[1][0]
          result = command_dall[1][1:]
          zone = self.zone2int(command_dall[2])
          command_d_ = {
            "Set":play_d_["Set"],
            "Rally":play_d_["Rally"],
            "transition":t_number0+1,
            "motion":m_number0+1,
            "No":No,
            "action":action,
            "result":result,
            "zone":zone
          }
          command_d.append(command_d_)
    return command_d


  def trans2point(self,play_d: list) -> list:
    trans_d = self.play2trans(play_d)
    point_d = []
    passp = False
    rally = 0
    for t_number0 in range(len(trans_d)):
      if not trans_d[t_number0]:
        continue
      if trans_d[t_number0]["Rally"] == rally:
        continue
      if "p" in trans_d[t_number0]["trans_data"]:
        point=1
        passp = True
      elif "e" in trans_d[t_number0]["trans_data"] and passp:
        continue
      elif "e" in trans_d[t_number0]["trans_data"]:
        point = -1
      else:
        continue

      if trans_d[t_number0]["transition"]%2 ==1:
        if point == 1:
          point1 = 1
          point2 = 0
        elif point == -1:
          point1 = 0
          point2 = 1
      elif trans_d[t_number0]["transition"]%2 ==0:
        if point ==1:
          point1 = 0
          point2 = 1
        elif point == -1:
          point1 = 1
          point2 = 0
      rally = trans_d[t_number0]["Rally"]
      point_d_ = {
        "Set":trans_d[t_number0]["Set"],
        "Rally":trans_d[t_number0]["Rally"],
        "transition":trans_d[t_number0]["transition"],
        "point1":point1,
        "point2":point2
      }
      point_d.append(point_d_)
      pass
    return point_d      
  
  def play2match(self,play_d: list) -> list:
    set_d_3 = []
    for set_number in range(1,play_d[len(play_d)-1]["Set"]+1):
      set_d_0 = list(filter(lambda d:d["Set"]==set_number,play_d))
      set_d_1 = []
      for i in range(0,len(set_d_0)):
        set_d_1.append(set_d_0[i]["play_data"])
      set_d_2 = ".".join(set_d_1)
      set_d_3.append(set_d_2)
    match_d = "!".join(set_d_3)
    return match_d



play_d = [
  {"Set":1,"Rally":1,"play_data":"12 sa 56/8 ra 32:11 tb 51:1 aap 65/20 de 65"},
  {"Set":1,"Rally":2,"play_data":"/8 sa 18/12 ra 32:8 ta 11:2 aap 78"},
  {"Set":1,"Rally":3,"play_data":"2 sae 790"},
  {"Set":1,"Rally":4,"play_data":"/12 sap 78:10 re 770"},
  {"Set":1,"Rally":5,"play_data":"/12 sae 650"},
  {"Set":1,"Rally":6,"play_data":"2 sf 78/2 ra 32:11 ta 22:8 aap 86"},
  {"Set":1,"Rally":7,"play_data":"/1 sa 58/14 ra 32:8 ta 21:2 aa 78/20 bt 87:22 da 32:11 tb c2:1 aap 56/20 de 560"},
  {"Set":1,"Rally":8,"play_data":"8 sf 89/22 ra 32:11 tb 51:2 ar 38/10 ba 33:11 db 97:8 tc 53:2 oo 88/20 da 32:8 tb c1:1 ap 65"},
  {"Set":2,"Rally":1,"play_data":"/12 sa 89/12 ra 32:8 ta 11:2 apa 66"}
  ]

