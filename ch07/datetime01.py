#  顯示現在日期(年、月、日) 和目前前時間(時、分、秒)
import datetime as DT
t1 = DT.datetime.now()
print(t1)
print(f'現在日期 : {t1.year} 年 {t1.month} 月 {t1.day} 日')
print(f'目前時間 : {t1.hour} 時 {t1.minute} 分 {t1.second} 秒')
