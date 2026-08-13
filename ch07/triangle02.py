#求三角形面積函式主體建立時,兩個虛引數底與高皆指定預設值。當呼叫該函式時,分別以不傳遞實引數、只傳遞一個實引數或傳遞兩個實引數,來觀察呼叫函式的執行情況。 

# 定義計算三角形面積的函數
def triangle(B = 6, H = 6):
  # 計算三角形面積 = (底 * 高) / 2
  print()
  # 輸出三角形的底與高
  print(f'三角形的底為{B}, 高為{H}')
  # 計算三角形面積
  A = B * H / 2
  # 輸出三角形面積
  return A
 
# 使用函數 triangle 計算三角形面積
# 設定三角形的底
base = 10
# 設定三角形的高
high = 5
# 呼叫函數 triangle 並傳入底與高，將計算結果存入 area1 變數中
area1 = triangle(base, high)
# 輸出三角形面積結果
print(f'三角形的面積為 {area1}')
# 使用函數 triangle 計算三角形面積，僅傳入底，使用預設高
base = 10
# 設定三角形的高
area2 = triangle(base)
# 輸出三角形面積結果
print(f'三角形的面積為 {area2}')
# 使用函數 triangle 計算三角形面積，使用預設底與高
area3 = triangle()
# 輸出三角形面積結果
print(f'三角形的面積為 {area3}')
