
# コードのテスト

# 操作画面
from _code_ver11_1_1 import vb_window as vw
from _code_ver11_1_1 import vb_file as vf
# データの入力
# データのプロット
from _code_ver11_1_1 import vb_plot as vp
# スタッツ表
from _code_ver11_1_1 import vb_stats as vs

# vb_stats.py プレーの統計値に関するライブラリ
  # チーム別スタッツ作成
vw.Set_Info
data_p,data_p1,data_p2,Team1ab,Team2ab = vf.player_index(vw.Season_path,vw.Tournament_path,vw.Team1,vw.Team2)
test = vs.Tstats1(data_p1,vw.df,vw.df_Team1,"1")
test.to_csv("Test.csv")
vs.bp1(vw.df,1)

# vb_plot.py プレーの作図に関するライブラリ
  # プレーのコート上への図示(slot,number,action)
  # どこから・誰が・何をしたか…スロット・背番号は選択しなければ("")その項目はすべて選択される
vp.makeplot1(vw.df,vw.df_Team1,vw.Team1,"1","51","14","a")
vp.makeplot1(vw.df,vw.df_Team1,vw.Team1,"1","","12","s")
  # セット・背番号別  トス配分のコート上への図示
vp.tmakeplot1(vw.df,vw.df_Team1,vw.Team1,"","")
# vp.df_data1("","","","s","")
# vp.dfaction1("","","","s","")

vw.Set_Result
vw.Set_Info

