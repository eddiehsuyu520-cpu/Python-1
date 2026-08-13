x=5         # 指定 x 變數值為常值 5
y=x         # 指定 y 變數值為變數 x 的值
print('x=', id(x), 'y=', id(y))  # 顯示變數 x, y 的記憶體位置
x=3+y       # 指定 x 變數值為運算式 3+y 的結果
print('x=', id(x), 'y=', id(y))  # 顯示變數 x, y 的記憶體位置
a,b=2,3
print('a=', id(a), 'b=', id(b))
a,b=b,a     # a,b 變數值交換
print('a=', id(a), 'b=', id(b))