# 宣告三角形的底（x）與高（h）
x = 25.6
h = 10.84

# 計算三角形面積：底 * 高 / 2
area = x * h / 2

# 使用 f-string 格式化輸出，:.2f 代表顯示到小數點後第二位
print(f'三角形底為{x:.2f}、高為{h:.2f},面積等於{area:.2f}')


# 宣告兩個變數
x = 10
y = 4

# 使用 .format() 進行算術運算與輸出
print('{} + {} = {}'.format(x, y, x + y))   # 加法
print('{} - {} = {}'.format(x, y, x - y))   # 減法
print('{} * {} = {}'.format(x, y, x * y))   # 乘法
print('{} / {} = {}'.format(x, y, x / y))   # 除法（浮點數除法）
print('{} // {} = {}'.format(x, y, x // y)) # 整數除法（只取商數）
print('{} % {} = {}'.format(x, y, x % y))   # 餘數（取餘數）


# 宣告攝氏溫度
celsius = 128

# 依公式計算華氏溫度
fahrenheit = celsius * 9 / 5 + 32

# 格式化輸出說明：
# {:4d}   -> 顯示整數，並且至少佔 4 個字元空間。
# {:08.3f} -> 總寬度 8 位（整數 4 位 + 小數點 1 位 + 小數 3 位 = 8 位），空白處補 0。
print('攝氏{:4d} 度 =  華氏{:08.3f} 度'.format(celsius, fahrenheit))
