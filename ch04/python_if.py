  
num = 1 
if(num < 0):   
    print("num是負數")
  
score = 60  
if(score >= 55 and score <= 60 ):
  score = 60  
  print("The score is 60.")
  
text = "Hello World"
if (n := len(text)) > 5:  # 賦值與判斷同時發生
    print(f"字串太長了，共有 {n} 個字")
    
command = input("請輸入指令: ")
while command != "quit":
    print(f"正在執行: {command}")
    command = input("請輸入指令: ") # 必須重複寫這行
    
while (command := input("請輸入指令: ")) != "quit":
    print(f"正在執行: {command}")
    


