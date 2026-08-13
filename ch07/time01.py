import time as T
num = T.time()
print(num)
# 1785738947.4481163  -->從1970-01-01 00:00:00（電腦世界的起點時間）起到目前的總秒數。

# 轉換成當地時間的結構
local_time = T.localtime(num)
print (local_time)
# 格式化成好看的字串（年-月-日 時:分:秒）
print(T.strftime("%Y-%m-%d %H:%M:%S", local_time))
# 輸出範例: 2026-08-05 10:56:05