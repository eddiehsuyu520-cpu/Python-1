select = int(input("====================\n1.新增/修改字典\n2.刪除單字\n3.單字查詢\n4.結束程式\n請輸入選項(1~4):"))

#請輸入文章：高高興興，興高采烈。
article_tuple = tuple(input("請輸入文章："))
article_set = set(article_tuple)
for i in article_set:
  print(f"「{i}」 使用{article_tuple.count(i)}次")



 #請撰寫一程式，模擬大樂透開奬，產生7個1~49之間不重複的號碼。
import random

numbers = random.sample(range(1, 50), 7)
print(f"本期大樂透號碼：\n{' '.join(map(str, sorted(numbers)))}")