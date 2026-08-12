list1 = [10, 20, 30]
print(list1)             # 輸出: [10, 20, 30]

list2tuple = tuple(list1)
print(list2tuple)        # 輸出: (10, 20, 30) (轉換成不可變的 tuple)

tuple2list = list(list2tuple)
tuple2list.append(40)    # 列表變成 [10, 20, 30, 40]
tuple2list.pop(1)        # 刪除索引 1 的元素（也就是 20）
print(tuple2list)        # 輸出: [10, 30, 40]

print(len(list1))        # 輸出: 3
print(len(list2tuple))   # 輸出: 3
print(len(tuple2list))   # 輸出: 3

tuple2list.append(30)    # 在末尾加上 30，列表變成 [10, 30, 40, 30]
print(tuple2list)        # 輸出: [10, 30, 40, 30]
print(tuple2list.count(30)) # 輸出: 2 (數字 30 出現了兩次)

# list.sort() 方法是一個「原地（In-place）修改」的操作，它不會回傳任何新的列表，其預設回傳值就是 None。
# append()為了避免開發者混淆，其回傳值（Return Value）也都是空值 None。
print(tuple2list.sort()) # 輸出: None
print(sorted(tuple2list))

tuple2list.append(5)
tuple2list.sort()  # 先做排序，這行不印
print(tuple2list)  # 輸出: [10, 30, 30, 40]

# Python 遵循一個重要的程式設計原則：「修改資料的動作（命令）」與「獲取資料的動作（查詢）」應該分開。
mylist = [1, 2, 3]
new_list = mylist.append(4)  # 試圖把結果存下來
print(new_list)              # 輸出: None
print(mylist)                # 輸出: [1, 2, 3, 4] （原本的列表其實已經變了）

