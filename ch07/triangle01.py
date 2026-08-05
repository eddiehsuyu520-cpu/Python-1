# 定義計算三角形面積的函數，接收底(B)與高(H)兩個參數
def triangle(B, H):
    # 計算三角形面積：面積 = (底 * 高) / 2
    A = B * H / 2
    # 回傳計算出來的三角形面積
    return A
    
# 設定三角形的底邊長
base = 10
# 設定三角形的高度
height = 5
# 呼叫函數 triangle 並傳入底與高，將計算結果存入 area 變數中
area = triangle(base, height)
# 印出三角形面積結果
print(f"底為 {base}、高為 {height} 的三角形面積為 : {area}")