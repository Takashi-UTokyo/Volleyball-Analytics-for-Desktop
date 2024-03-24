
# コードのテスト

# vfrライブラリ読み込み時に [folder,file,Team1,Team2] を入力
from _code_ver10_2_2 import vb_file as vf
from _code_ver10_2_2 import vb_plot as vp
from _code_ver10_2_2 import vb_stats as vs



vf.df
# vb_stats.py プレーの統計値に関するライブラリ
  # チーム別スタッツ作成
vs.Tstats1()




# vb_plot.py プレーの作図に関するライブラリ
  # プレーのコート上への図示(slot,number,action)
  # どこから・誰が・何をしたか…スロット・背番号は選択しなければ("")その項目はすべて選択される
vp.makeplot1("Set1",51,"","a")
  # セット・背番号別  トス配分のコート上への図示
vp.tmakeplot1("","")
vp.slot1("","",1,'p')
