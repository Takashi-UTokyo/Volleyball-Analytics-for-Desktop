from _code_ver12_1_1.Entry.vb_entry12 import Entry_new,Entry_exi
from _code_ver12_1_1.Data.vb_data12 import DataConversion
from _code_ver12_1_1.Data.vb_file12 import File
from _code_ver12_1_1.Entry.vb_analytics12 import Serve,Attack,Block,Reception


file = File()
DtC = DataConversion()
exi = Entry_exi()


exi.exe()


searchset = None
searchrally = None
list(filter(lambda d:d["Set"]==searchset and d["Rally"]==searchrally,exi.play_d))[0]["play_data"]

# list(filter(lambda d:d["Set"]==searchset and d["Rally"]==searchrally,exi.play_d))[0]["play_data"] = ""
file.save_data(exi.match_info,exi.set_info,exi.set_result,exi.play_d)
DtC.play2command(exi.play_d)

log = DtC.play2log(exi.play_d,exi)
for log_ in log:
  print(log_)


