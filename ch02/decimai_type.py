import decimal           # 匯入 decimal 模組
f1,f2=10.0,3.0           # 宣告 f1、f2 變數並指定變數值為浮點數 10.0 和 3.0
d1=decimal.Decimal(10)   # 使用 Decimal() 方法宣告 d1 為 decimal 型別，值為 10
d2=decimal.Decimal('3.0')
print(type(d1))          # 顯示 d1 變數的類別   ⇨ <class 'decimal.Decimal'>
print(f1/f2)             # 顯示 f1 除以 f2 的值 ⇨ 3.3333333333333335
print(d1/d2)             # 顯示 d1 除以 d2 的值 ⇨ 3.333333333333333333333333333
d3=decimal.Decimal('2.345') # 宣告 d3 為 decimal 型別變數，值為字串常值 '2.345'
d4=decimal.Decimal('6.78')
print(d3+d4)             # 有效位數為三位       ⇨ 9.125
print(d3*d4)             # 有效位數為五位 (3+2)  ⇨ 15.89910