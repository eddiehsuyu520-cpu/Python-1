#建立Triple()函式,傳入的引數為串列名稱,並傳入的串列各元素變成三倍。觀察函式呼叫前、呼叫時、呼叫後,其相對的串列實引數與串列虛引數之間的變化情況。

def Triple(lst):
  for i in range(len(lst)):
     lst[i] = lst[i] * 3
  print('執行 Triple() 函式 ------')
  print(f'串列 lst = {lst}')
  print()
 
arr = [2, 4, 6, 8, 10]
print('呼叫 Triple() 函式前 ------')
print(f'串列 arr = {arr}')
print()
Triple(arr)
print('呼叫 Triple() 函式後 ------')
print(f'串列 arr = {arr}')
