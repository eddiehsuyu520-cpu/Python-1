# -*- coding: utf-8 -*-
"""
Python 元組（Tuple）與列表（List）綜合操作教學範例
這個程式完整說明了不可變性、解構、記憶體交換及轉型機制。
"""

print("=== 1. 元組建立與解構賦值 ===")
tuple1 = ('東', '南', '西')
print(f"初始 tuple1 內容: {tuple1}，型別為: {type(tuple1)}")

# 解構賦值：將元組內的元素，按順序一次性指派給多個變數
East, South, West = tuple1
print(f"解構成功 -> 變數 South 的值為: {South}")
print("說明: 左側變數數量 (3個) 必須與元組元素數量 (3個) 完全一致，否則會報錯。\n")


print("=== 2. 元組的串接與逗號的秘密 ===")
# 錯誤示範：tuple2 = tuple1 + ('北') -> 會報錯，因為 ('北') 會被視為一般字串(str)
# 正確示範：必須加上逗號 ('北',) 才會被 Python 判定為「單元素元組」
tuple2 = tuple1 + ('北',)
print(f"串接後的 tuple2: {tuple2}")
print("說明: 元組具不可變性 (Immutable)，無法原地修改。此處是用 + 號在記憶體產生全新元組。\n")

#Tuple 的「不可變性（Immutable）」指的是一旦建立，你就不能去修改「同一個 Tuple 物件內部」的元素。
print("=== 3. 神奇的變數數值交換 (Tuple Swapping) ===")
print(f"交換前 -> tuple1: {tuple1}, tuple2: {tuple2}")
# Python 獨特的優雅寫法，底層先將右側打包成臨時元組，再解構賦值給左側
tuple1, tuple2 = tuple2, tuple1
print(f"交換後 -> tuple1: {tuple1}, tuple2: {tuple2}")
print("說明: 不需要宣告暫存變數 temp，即可完成兩個變數指向的記憶體位址對調。\n")


print("=== 4. 計算長度與記憶體回收 ===")
print(f"交換後的 tuple1 長度為: {len(tuple1)}")

# del 會刪除變數名稱，釋放該變數對記憶體物件的引用
del tuple2
print("說明: tuple2 變數已被 del 徹底刪除。此時若執行 print(tuple2) 將會引發 NameError 崩潰。\n")


print("=== 5. 繞道修改：元組與列表的互轉 ===")
# 步驟 A: 將不可變的元組轉為可變的列表
list1 = list(tuple1)
# 步驟 B: 使用列表的 append() 方法在末尾添加元素 (此方法原地修改，回傳 None)
list1.append('東北')
print(f"修改中的 list1: {list1}，型別為: {type(list1)}")
# 步驟 C: 將修改完的列表再轉回元組，並覆蓋原變數
tuple1 = tuple(list1)
print(f"最終轉換回來的 tuple1: {tuple1}，型別為: {type(tuple1)}")
print("說明: 這是突破元組不可變性限制的標準『繞道』手法。\n")


print("=== 6. 索引、成員檢查與迴圈迭代 ===")
# 索引取值：Python 索引一律從 0 開始
print(f"第一個元素 (索引 0): {tuple1[0]}")

# 成員檢查：使用 in 關鍵字，會回傳布林值 (True/False)，效率極高
is_exist = '東北' in tuple1
print(f"'東北' 是否在 tuple1 中？ {is_exist}")

# 迴圈迭代：
print("迴圈印出所有元素 (以逗號分隔): ", end="")
for t in tuple1:
    # end=',' 代表印完該元素後不要換行，改用逗號結尾
    print(t, end=',')
print("\n\n程式示範結束。")
