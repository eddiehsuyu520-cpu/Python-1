# 利用列表生成式建立一個長度為 5、裡面初始值都是 `0` 的列表，也就是 `[0, 0, 0, 0, 0]`。
lst = [0 for x in range(5)]
print('請依序輸入5個整數...')
for i in range(5):
  print(f'輸入第 {i+1} 個元素內容：', end = '')
  # 接收使用者在鍵盤輸入的文字，並將它轉成數字。
  lst[i] = eval(input())
print(lst)
# 找出最大值（演算法核心 
max = lst[0] # 先假設第一個元素就是最大的
for item in lst:
  # 如果挑戰者 `item` 比目前的擂台主 `max` 還要大，就把擂台主換人，寫入 `max = item`。
  if max < item : 
     max = item
    
print()
print(f'最大值為 {max}')