import decimal

# 宣告兩個浮點數變數數值皆為 2.5
x = 2.5
y = 2.5

# 印出 x 與 y 在記憶體中的唯一識別碼 (位址)
print(id(x), id(y))

# x is y 檢查兩者是否指向「同一個記憶體位址」(True)
# x == y 檢查兩者「數值是否相等」(True)
print(x is y, x == y)  # 輸出: True True

# 建立一個 Decimal 物件，精準表示 2.5
z = decimal.Decimal('2.5')

# 印出 z 在記憶體中的識別碼 (位址會與 x, y 不同)
print(id(z))

# z is x 檢查 z 與 x 是否為同一個物件 (False，因為不同型態且位址不同)
# z == x 檢查 z 與 x 的數值是否相等 (True，因為數學上都是 2.5)
print(z is x, z == x)  # 輸出: False True