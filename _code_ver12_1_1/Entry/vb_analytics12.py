import pandas as pd
from matplotlib import pyplot as plt
from Data.vb_data12 import DataConversion,play_d
from _code_ver12_1_1.Function.vb_window12 import Window0

DtC = DataConversion()

class Fund:
  def __init__(self,play_d:object):
    self._play_d = play_d
    self._command_d = DtC.play2command(self._play_d)
    self._df = pd.DataFrame(self._command_d)
    self.df = self._df
    pass


class Plot(Fund):
  def __init__(self,play_d:object):
    super().__init__(play_d)
    self._xy = pd.DataFrame([("1","6","5"),("9","8","7"),("2","3","4")],index=[7.5,4.5,1.5],columns=[1.5,4.5,7.5])
    pass

  def action(self,set:list,Team:int,action:str,No:list,result:list):
    if Team == 2:
      Team = 0
    if set:
      if No:
        if result:
          df_action = self.df[(self.df["Set"].isin(set))&(self.df["transition"]%2==Team)&(self.df["No"].isin(No))&(self.df["action"]==action)&(self.df["result"].isin(result))].reset_index(drop=True)
        else:
          df_action = self.df[(self.df["Set"].isin(set))&(self.df["transition"]%2==Team)&(self.df["No"].isin(No))&(self.df["action"]==action)].reset_index(drop=True)
      else:
        if result:
          df_action = self.df[(self.df["Set"].isin(set))&(self.df["transition"]%2==Team)&(self.df["action"]==action)&(self.df["result"].isin(result))].reset_index(drop=True)
        else:
          df_action =  self.df[(self.df["Set"].isin(set))&(self.df["transition"]%2==Team)&(self.df["action"]==action)].reset_index(drop=True)
    else:
      if No:
        if result:
          df_action = self.df[(self.df["transition"]%2==Team)&(self.df["No"].isin(No))&(self.df["action"]==action)&(self.df["result"].isin(result))].reset_index(drop=True)
        else:
          df_action = self.df[(self.df["transition"]%2==Team)&(self.df["No"].isin(No))&(self.df["action"]==action)].reset_index(drop=True)
      else:
        if result:
          df_action = self.df[(self.df["transition"]%2==Team)&(self.df["action"]==action)&(self.df["result"].isin(result))].reset_index(drop=True)
        else:
          df_action =  self.df[(self.df["transition"]%2==Team)&(self.df["action"]==action)].reset_index(drop=True)
    return df_action
  
  def zone2xy(self,zone:int):
    zoneL =str(zone)[:2][:1]
    zoneM = str(zone)[:2][1:]
    zone0 = str(zone)[2:]
    if zoneL and zoneM:
      X,x = self._xy.columns[self._xy[self._xy == zoneL].any(axis=0)][0],self._xy.columns[self._xy[self._xy == zoneM].any(axis=0)][0]
      Y,y = self._xy.index[self._xy[self._xy == zoneL].any(axis=1)][0],self._xy.index[self._xy[self._xy == zoneM].any(axis=1)][0]
    elif zoneL == "0":
      X,x = 4.5,4.5
      Y,y = 0,0
    
    X2 = X + (x-4.5)/3
    Y2 = Y + (y-4.5)/3
    if zone0:
      if Y == 7.5:
        Y2 = Y2 + 1.0
      else:
        X2 = X2 + (X - 4.5)/3
    return X2,Y2
  
  def plusxy(self,df_action):
    z = []
    for i in range(len(df_action)):
      x,y = self.zone2xy(df_action.at[i,"zone"])
      z.append((x,y))
    df_z = pd.DataFrame(z,columns=["X","Y"])
    df_action_xy = pd.concat([df_action,df_z],axis=1)
    return df_action_xy

  def XYdata(self,df_action):
    xydata = []
    for k,g in df_action.groupby(["X","Y"]):
      count = len(g)
      if int(k[0]) != float(k[0]):
        xy_d = {
          "X":k[0],
          "Y":k[1],
          "COUNT":count,
        }
        xydata.append(xy_d)
    return xydata

class Serve(Plot):
  def __init__(self,play_d:list):
    self._action = "s"
    super().__init__(play_d)
    pass

  def floatserve(self,set:list[list,None],Team:int,No:list[list,None]):
    df_serve_fall = self.plusxy(self.action(set,Team,self._action,No,["f","fp","fe"]))
    df_serve_f = df_serve_fall[df_serve_fall["result"]=="f"]
    df_serve_fp = df_serve_fall[df_serve_fall["result"]=="fp"]
    df_serve_fe = df_serve_fall[df_serve_fall["result"]=="fe"]
    float_xy = {"sf":self.XYdata(df_serve_f),"sfp":self.XYdata(df_serve_fp),"sfe":self.XYdata(df_serve_fe)}
    return float_xy
  
  def driveserve(self,set:list[list,None],Team:int,No:list[list,None]):
    df_serve_dall = self.plusxy(self.action(set,Team,self._action,No,["a","ap","ae","b","bp","be"]))
    df_serve_a = df_serve_dall[df_serve_dall["result"].isin(["a"])]
    df_serve_ap = df_serve_dall[df_serve_dall["result"].isin(["ap"])]
    df_serve_ae = df_serve_dall[df_serve_dall["result"].isin(["ae"])]
    df_serve_b = df_serve_dall[df_serve_dall["result"].isin(["b"])]
    df_serve_bp = df_serve_dall[df_serve_dall["result"].isin(["bp"])]
    df_serve_be = df_serve_dall[df_serve_dall["result"].isin(["be"])]
    drive_xy = {"sa":self.XYdata(df_serve_a),"sap":self.XYdata(df_serve_ap),"sae":self.XYdata(df_serve_ae),
              "sb":self.XYdata(df_serve_b),"sbp":self.XYdata(df_serve_bp),"sbe":self.XYdata(df_serve_be)}
    return drive_xy

class Attack(Plot):
  def __init__(self,play_d:list) -> None:
    self._action = "a"
    super().__init__(play_d)
    pass

  def plusslot(self,df_attack,slot:list):
    if df_attack.empty:
      return df_attack
    slot_d = []
    for i in range(len(df_attack)):
      rally = df_attack.at[i,"Rally"]
      trans = df_attack.at[i,"transition"]
      slotlist = self.df[(self.df["Rally"]==rally)&(self.df["transition"]==trans)&(self.df["action"]=="t")].reset_index(drop=True).at[0,"zone"]
      slot_d.append(slotlist)
    df_slot = pd.DataFrame(slot_d,columns=["slot"])
    df_attack_xy = pd.concat([df_attack,df_slot],axis=1)
    if slot:      
      slot_ = DtC.zone2int(slot)
      df_attack_xy = df_attack_xy[(df_attack_xy["slot"].isin(slot_))]
    return df_attack_xy
    

  def spike(self,set:list[list,None],Team:int,No:list[list,None],slot:list[list,None]):
    df_attack_sall = self.plusxy(self.action(set,Team,self._action,No,["a","ap","ae","b","bp","be"]))
    df_attack_sall = self.plusslot(df_attack_sall,slot)
    df_attack_a = df_attack_sall[df_attack_sall["result"].isin(["a"])]
    df_attack_ap = df_attack_sall[df_attack_sall["result"].isin(["ap"])]
    df_attack_ae = df_attack_sall[df_attack_sall["result"].isin(["ae"])]
    df_attack_b = df_attack_sall[df_attack_sall["result"].isin(["b"])]
    df_attack_bp = df_attack_sall[df_attack_sall["result"].isin(["bp"])]
    df_attack_be = df_attack_sall[df_attack_sall["result"].isin(["be"])]
    df_attack_c = df_attack_sall[df_attack_sall["result"].isin(["c"])]
    df_attack_cp = df_attack_sall[df_attack_sall["result"].isin(["cp"])]
    df_attack_ce = df_attack_sall[df_attack_sall["result"].isin(["ce"])]
    spike_xy = {"aa":self.XYdata(df_attack_a),"aap":self.XYdata(df_attack_ap),"aae":self.XYdata(df_attack_ae),"ab":self.XYdata(df_attack_b),"abp":self.XYdata(df_attack_bp),"abe":self.XYdata(df_attack_be),"ac":self.XYdata(df_attack_c),"acp":self.XYdata(df_attack_cp),"ace":self.XYdata(df_attack_ce)}
    return spike_xy
  
  def faint(self,set:list[list,None],Team:int,No:list[list,None],slot:list[list,None]):
    df_attack_fall = self.plusxy(self.action(set,Team,self._action,No,["f","fp","fe"]))
    df_attack_fall = self.plusslot(df_attack_fall,slot)
    df_attack_f = df_attack_fall[df_attack_fall["result"].isin(["f"])]
    df_attack_fp = df_attack_fall[df_attack_fall["result"].isin(["fp"])]
    df_attack_fe = df_attack_fall[df_attack_fall["result"].isin(["fe"])]
    faint_xy = {"af":self.XYdata(df_attack_f),"afp":self.XYdata(df_attack_fp),"afe":self.XYdata(df_attack_fe)}
    return faint_xy
  
  def rebound(self,set:list[list,None],Team:int,No:list[list,None],slot:list[list,None]):
    df_attack_rall = self.plusxy(self.action(set,Team,self._action,No,["r","re"]))
    df_attack_rall = self.plusslot(df_attack_rall,slot)
    df_attack_r = df_attack_rall[df_attack_rall["result"].isin(["r"])]
    df_attack_re = df_attack_rall[df_attack_rall["result"].isin(["re"])]
    rebound_xy = {"ar":self.XYdata(df_attack_r),"are":self.XYdata(df_attack_re)}
    return rebound_xy 

class Block(Plot):
  def __init__(self,play_d):
    self._action = "b"
    super().__init__(play_d)

  def plusslot(self,df_block,slot:list):
    if df_block.empty:
      return df_block
    slot_d = []
    for i in range(len(df_block)):
      rally = df_block.at[i,"Rally"]
      trans = df_block.at[i,"transition"]
      slotlist = self.df[(self.df["Rally"]==rally)&(self.df["transition"]==trans-1)&(self.df["action"]=="t")].reset_index(drop=True).at[0,"zone"]
      slot_d.append(slotlist)
    df_slot = pd.DataFrame(slot_d,columns=["slot"])
    df_block_xy = pd.concat([df_block,df_slot],axis=1)
    if slot:      
      slot_ = DtC.zone2int(slot)
      df_block_xy = df_block_xy[(df_block_xy["slot"].isin(slot_))]
    return df_block_xy
  
  def block(self,set:list[list,None],Team:int,No:list[list,None],slot:list[list,None]):
    df_block_ball = self.plusxy(self.action(set,Team,self._action,No,["a","b","p","e"]))
    df_block_ball = self.plusslot(df_block_ball,slot)
    df_block_ba = df_block_ball[df_block_ball["result"].isin(["a"])]
    df_block_bb = df_block_ball[df_block_ball["result"].isin(["b"])]
    df_block_bp = df_block_ball[df_block_ball["result"].isin(["p"])]
    df_block_be = df_block_ball[df_block_ball["result"].isin(["e"])]
    block_xy = {"ba":self.XYdata(df_block_ba),"bb":self.XYdata(df_block_bb),"bp":self.XYdata(df_block_bp),"be":self.XYdata(df_block_be)}
    return block_xy

  def blocktouch(self,set:list[list,None],Team:int,No:list[list,None],slot:list[list,None]):
    df_block_tall = self.plusxy(self.action(set,Team,self._action,No,["t","te"]))
    df_block_tall = self.plusslot(df_block_tall,slot)
    df_block_t = df_block_tall[df_block_tall["result"].isin(["t"])]
    df_block_te = df_block_tall[df_block_tall["result"].isin(["te"])]
    blocktouch_xy = {"bt":self.XYdata(df_block_t),"bte":self.XYdata(df_block_te)}
    return blocktouch_xy
  
class Reception(Plot):
  def __init__(self,play_d):
    self._action = "r"
    self.play_d = super().__init__(play_d)
    pass

  def pluscatch(self,df_rec,catch):
    if df_rec.empty:
      return df_rec
    catch_d = []
    for i in range(len(df_rec)):
      rally = df_rec.at[i,"Rally"]
      trans = df_rec.at[i,"transition"]
      catchlist = df_rec[(self.df["Rally"]==rally)&(self.df["transition"])&(self.df["action"]=="s")].reset_index(srop=True).at[0,"zone"]
      catch_d.append(catchlist)
    df_catch = pd.DataFrame(catch_d)
    df_rec_xy = pd.concat([df_rec,df_catch],axis=1)
    if catch:
      df_rec_xy

      

  def reception(self,set:list[list,None],Team:int,No:list[list,None]):
    df_rec_rall = self.plusxy(self.action(set,Team,self._action,No,""))

    pass

# set,No,result : [,,] or []
# Team : 1 or 2

if __name__ == "__main__":

  serve = Serve(play_d)
  
  serve.floatserve([],2,[6,7,8])
  serve.floatserve([1],1,[])
  serve.driveserve([1],1,[])
  
  attack = Attack(play_d)
  attack.spike([],1,[],[11,21])
  attack.faint([1],1,"","")
  attack.rebound([1],1,"","")
  
  set = ""
  Team = 1
  No = ""
  slot = [51]

  self = Block(play_d)
  
  block = Block(play_d)
  block.block(set,Team,No,slot)
  block.blocktouch("",1,"",[51])



class Stats(Fund):
  def __init__(self):
    super().__init__(play_d)
    pass

class BreakPoint:
  def __init__(self):
    pass

class Analytics(Window0):
  def __init__(self):
    pass

  def analy_main(self):
    self.analy_window()
    pass

