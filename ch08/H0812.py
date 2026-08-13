import re

dict_ec = {}
while True:
    select = int(input("====================\n1.新增/修改字典\n2.刪除單字\n3.單字查詢\n4.結束程式\n請輸入選項(1~4):"))
    if select == 1:
        char = input("請輸入英文單字:")
        if re.match(r"^[a-zA-Z\s]+$", char):
          if char in dict_ec:
              print(f"「{char}」的中文解釋為：{dict_ec[char]}")
          else:
              chinese = input("請輸入中文解釋:")
              if(re.search(r"[\u4e00-\u9fa5]", chinese)):
                  dict_ec[char] = chinese
                  print(f"「{char}」已新增/修改為：{dict_ec[char]}")
              else:
                  print("輸入的中文解釋不合法，請重新輸入")
        else:
          print("輸入的英文單字不合法，請重新輸入")
    elif select == 2:
        char = input("請輸入要刪除的英文單字:")
        if re.match(r"^[a-zA-Z\s]+$", char):
              if char in dict_ec:
                  del dict_ec[char]
                  print(f"「{char}」已刪除")
              else:
                  print(f"「{char}」不存在")
        else:
          print("輸入的英文單字不合法，請重新輸入")
    elif select == 3:
        char = input("請輸入要查詢的英文單字:")
        if re.match(r"^[a-zA-Z\s]+$", char):
              if char in dict_ec:
                  print(f"「{char}」的中文解釋為：{dict_ec[char]}")
              else:
                  print(f"「{char}」不存在")
        else:
          print("輸入的英文單字不合法，請重新輸入")
    elif select == 4:
        print("程式結束")
        break
      
#請輸入文章：高高興興，興高采烈。
article_tuple = tuple(input("請輸入文章："))
article_set = set(article_tuple)
for i in article_set:
  print(f"「{i}」 使用{article_tuple.count(i)}次")



 #請撰寫一程式，模擬大樂透開奬，產生7個1~49之間不重複的號碼。
import random

numbers = random.sample(range(1, 50), 7)
print(f"本期大樂透號碼：\n{' '.join(map(str, sorted(numbers)))}")