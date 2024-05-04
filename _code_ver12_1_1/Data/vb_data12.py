
class DataConversion:
  def __init__(self):
    pass

  def zone2int(self,zone):
    if type(zone) is list:
      zone0 = zone
    else:
      zone0 = [zone]
    zone01 = []
    for zone0_ in zone0:
      if type(zone0_) is str:
        if "a" in zone0_:
          zone1 = -1
        elif "b" in zone0_:
          zone1 = -2
        elif "c" in zone0_:
          zone1 = -3
        else:
          zone1 = zone0_[0]
        zone2 = zone0_[1:]
        zone3 = int(str(zone1)+zone2)
      elif type(zone0_) is int:
        zone3 = zone0_
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


  def play2point(self,play_d: list) -> list:
    point_d = []
    for set_number in range(1,play_d[len(play_d)-1]["Set"]+1):
      play_d_ = list(filter(lambda d:d["Set"]==set_number,play_d))
      for r_number in range(1,play_d_[len(play_d_)-1]["Rally"]+1):
        trans_d_ = self.play2trans(list(filter(lambda d: d["Rally"]==r_number,play_d_)))
        if list(filter(lambda d:"p" in d["trans_data"],trans_d_)) and (list(filter(lambda d: "e" in d["trans_data"],trans_d_))):
          d = list(filter(lambda d: "p" in d["trans_data"],trans_d_))[0]
          if d["transition"]%2 == 1:
            point1 = 1
            point2 = 0
          elif d["transition"]%2 == 0:
            point1 = 0
            point2 = 1
          point_d_ = {
            "Set":set_number,
            "Rally":r_number,
            "transition":d["transition"],
            "point1":point1,
            "point2":point2
          }
        elif (d := list(filter(lambda d: "p" in d["trans_data"],trans_d_))):
          if d[0]["transition"]%2 == 1:
            point1 = 1
            point2 = 0 
          elif d[0]["transition"]%2 == 0:
            point1 = 0
            point2 = 1
          point_d_ = {
            "Set":set_number,
            "Rally":r_number,
            "transition":d[0]["transition"],
            "point1":point1,
            "point2":point2
          }
        elif (d := list(filter(lambda d: "e" in d["trans_data"],trans_d_))):
          if d[0]["transition"]%2 == 1:
            point1 = 0
            point2 = 1
          elif d[0]["transition"]%2 == 0:
            point1 = 1
            point2 = 0
          point_d_ = {
            "Set":set_number,
            "Rally":r_number,
            "transition":d[0]["transition"],
            "point1":point1,
            "point2":point2
          }
        point_d.append(point_d_)
    return point_d

  def play2score(self):
    score_d = []
    point_d = self.play2point(self.play_d)
    for set_number in range(1,point_d[len(point_d)-1]["Set"]+1):
      score1 = 0
      score2 = 0
      point_d_ = list(filter(lambda d: d["Set"]==set_number,point_d))
      for r_number in range (0,len(point_d_)):
        score1 += point_d_[r_number]["point1"]
        score2 += point_d_[r_number]["point2"]
      score_d_ = {
        "Set":set_number,
        "score1":score1,
        "score2":score2
      }
      score_d.append(score_d_)
    return score_d
  
  

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

  def match2play(self,match_d: list) -> list:
    play_d = []
    set_d_ = match_d.split("!")
    for set_number0 in range(len(set_d_)):
      play_d_1 = set_d_[set_number0].split(".")
      for rally_number0 in range(len(play_d_1)):
        play_d_ = {
          "Set":set_number0+1,
          "Rally":rally_number0+1,
          "play_data":play_d_1[rally_number0]
        }
        play_d.append(play_d_)
    return play_d
  
  def log_action(self,action):
    if action == "s":
      log_action = "サーブ"
    elif action == "a":
      log_action = "アタック"
    elif action == "t":
      log_action = "トス"
    elif action == "b":
      log_action = "ブロック"
    elif action == "r":
      log_action = "レセプション"
    elif action == "d":
      log_action = "ディグ"
    elif action == "e":
      log_action = "エラー"
    elif action == "o":
      log_action = "返球"
    return log_action
  
  def play2log(self,play_d,cls):
    command_d = self.play2command(play_d)
    point_d = self.play2point(play_d)
    log = []
    command_d_ = command_d[1]
    for command_d_ in command_d:
      if command_d_["transition"]%2==1:
        log_0 = f" {cls.team1_ab} : "
      elif command_d_["transition"]%2==0:
        log_0 = f" {cls.team2_ab} : "
      if command_d_["No"]:
        log_1 = f"  {command_d_["No"]}番の{self.log_action(command_d_["action"])}"
        log.append(log_0)
        log.append(log_1)
      if "p" in command_d_["result"] or "e" in command_d_["result"]:
        point_d_ = list(filter(lambda d: d["Set"]==command_d_["Set"] and d["Rally"]==command_d_["Rally"],point_d))[0]
        if point_d_["point1"]:
          log_2 = f"{cls.team1_ab}のポイント"
          log.append(log_2)
        elif point_d_["point2"]:
          log_2 = f"{cls.team2_ab}のポイント"
          log.append(log_2)
    return log



play_d = [
  {"Set":1,"Rally":1,"play_data":"12 sa 56/8 ra 32:11 tb 51:1 aap 65/20 de 65"},
  {"Set":1,"Rally":2,"play_data":"/8 sa 18/12 ra 32:8 ta 11:2 aap 78"},
  {"Set":1,"Rally":3,"play_data":"2 sae 790"},
  {"Set":1,"Rally":4,"play_data":"/12 sap 78:10 re 770"},
  {"Set":1,"Rally":5,"play_data":"/12 sae 650"},
  {"Set":1,"Rally":6,"play_data":"2 sf 78/2 ra 32:11 ta 22:8 aap 86"},
  {"Set":1,"Rally":7,"play_data":"/1 sa 58/14 ra 32:8 ta 21:2 aa 78/20 bt 87:22 da 32:11 tb c2:1 aap 56/20 de 560"},
  {"Set":1,"Rally":8,"play_data":"8 sf 89/22 ra 32:11 tb 51:2 ar 38/10 ba 33:11 db 97:8 tc 53:2 oo 88/20 da 32:8 tb c1:1 ap 65"},
  {"Set":2,"Rally":1,"play_data":"/12 sa 89/12 ra 32:8 ta 11:2 apa 66"},
  {"Set":2,"Rally":2,"play_data":"12 sa 56/8 ra 3:11 tb 51:1 aap 56"}
  ]


self = DataConversion()
self.play2command(play_d)

# class A():
#   def __init__(self):
#     self.team1_ab = "AA"
#     self.team2_ab = "BB"
#     pass
# a = A()


# log = self.play2log(play_d,a)
# self.play2command(play_d)
# for log_ in log:
#   print(log_)