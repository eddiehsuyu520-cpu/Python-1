st1 = '人之初,性本善,性相近,習相遠'
arr1 = st1.split(',')
print(arr1) # 印出 ['人之初', '性本善', '性相近', '習相遠']
'''，印出中括號是因為 split() 方法會將原本的字串切開，並打包成一個「列表（List）」物件。'''

arr2 = ['苟不教', '性乃遷', '教之道', '貴以專']
# 連結字元為一個空格。連結字元會成為連結字元的一部分。
st2 = ' '.join(arr2)
print(st2)            # 印出 苟不教 性乃遷 教之道 貴以專
'''換成波浪號：st2 = '~'.join(arr2)👉 印出：苟不教~性乃遷~教之道~貴以專'''

lst = []
# 計算輸入字元總長度
count = eval(input('請輸入lst串列的元素數量：'))
print('請依序填入各元素的內容...') 
# 會產生一個從 0 開始、長度為 count 的數字序列
for i in range(count):
    print(f'輸入第 {i+1} 個元素內容：' , end = '')
    num = eval(input())
    lst.append(num)
   
print('lst串列的元素內容：')
for x in lst:
    print(x, end = ' ')