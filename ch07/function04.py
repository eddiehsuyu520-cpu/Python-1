# 定義一個能傳入字元和字元數的自定函式,該函式的任務是將所傳入的字元,以所傳入的字元數在函式定義主體內顯示出來,沒有傳回值。呼叫時,實引數分別使用變數、常值、運算式來傳入。# 定義函數 printChar，輸出指定字元 ch，重複 n 次
def printChar(ch, n):
   # 使用 for 迴圈重複輸出字元 ch，重複 n 次
   for i in range(n):
       # 使用 f-string 格式化輸出字元 ch，並指定不換行
       print (f'{ch}', end = '')
    # 在輸出完畢後換行    
   print()    
# 使用函數 printChar，輸出字元 'A' 重複 12 次
ch1 = 'A'
# 使用變數 n1 設定重複次數為 12
n1 = 12
# 使用函數 printChar，輸出字元 'A' 重複 12 次
printChar(ch1, n1)  # 實引數使用變數
# 使用函數 printChar，輸出字元 '$' 重複 15 次
printChar('$', 15)  # 實引數使用常值
# 使用函數 printChar，輸出字元 'B' 重複 16 次
printChar('B', n1+4)  # 實引數使用常值