def compound_interest(a,b,c):
    return a*pow(1+b/100/12,12*c)
print("== 複利率本利和試算 ==")
invest = eval(input("請輸入本金："))
rate = eval(input("請輸入年利率(%):"))
years = eval(input("幾年後領回："))

print(f" *** {years} 年後領回本利和：{compound_interest(invest, rate, years):.1f} ***")




#輸入兩個整數，使用自定函式算出最大公因數。
def gcd_brute_force(a, b):
    # 1. 先把數字都變成正數，確保負數也能算
    a, b = abs(a), abs(b)
    
    # 2. 處理 0 的特殊狀況
    if(a == 0 and b == 0):
        return 0
    elif (a == 0):
        return b
    elif (b == 0):
        return a
    else:
       # 確保從較小的那個數開始倒數，效率會稍微好一點
       start = min(a, b)
       # 從 start 開始倒數到 1
       for c in range(start, 0, -1):
          # 如果 x 可以同時整除 a 和 b，它就是最大公因數
          if a % c == 0 and b % c == 0:
              return c

x = int(input("輸入第一個整數 a: "))
y = int(input("輸入第二個整數 b: "))
print("a,b 兩整數的 GCD 為", gcd_brute_force(x, y))