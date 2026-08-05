#定義一個可以計算兩整數平均值並可傳回計算結果的自定函式, 並完成整個呼叫自定函式的過程。
# 定義計算平均值的函數
def average(n1, n2):
  # 計算兩個數字的平均值
   a = (n1 + n2) / 2
  # 返回平均值
   return a

print('輸入第 1 個整數：' , end='')
# 使用 eval() 讀取使用者輸入的整數
num1 = eval(input())
# 使用 eval() 讀取使用者輸入的整數
num2 = eval(input('輸入第 2 個整數：'))
# 計算平均值
avg = average(num1, num2)
# 輸出結果，保留一位小數
print(f'{num1} 和 {num2} 兩整數平均為：{avg:.1f}', end = '')
