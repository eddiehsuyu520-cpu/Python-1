f, i =1.2345, 12345
print(type(f))                # 顯示浮點數變值 f 的類別         ⇨ <class 'float'>
f2=float(i)                   # 用 float 函式將整數變數 i 轉成成浮點數
print(f2)                     # 顯示 f2 的變數值               ⇨ 12345.0
print(float.is_integer(f))    # 用 is_integer()檢查變數是否為整數 ⇨ False
print(float.is_integer(f2))   # 檢查變數 f2 是否為整數          ⇨ True
print(round(f,2))             # 用 round() 函式將變數 f 四捨五入到小數二位 ⇨ 1.23
print(f)
print(round(f))               # 用 round() 函式將變數 f 四捨五入到整數    ⇨ 1
print(isinstance(f,int))        # 用 isinstance() 檢查變數 f 是否為整數 ⇨ False
print(isinstance(f,float))      # 用 isinstance() 檢查變數 f 是否為浮點數 ⇨ True    