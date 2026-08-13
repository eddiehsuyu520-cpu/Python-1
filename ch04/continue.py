s = input("請輸入一個字串: ")
for ch in s:
  if ( ch > '9' or ch < '0' ) :
      continue
  print(ch , end = ' ')
  
  #在 Python 的 for 迴圈中，ch 是一個「自動迭代變數」。
  # 每一輪迴圈啟動時，Python 會自動從字串 s 中依序抓出一個字元，然後自動塞給 ch。