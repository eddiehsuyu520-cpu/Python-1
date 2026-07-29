# ── 1. 基礎數字字串轉型 (int, float) ───────────────────────
print(" ── 1. 基礎數字字串轉型 (int, float) ───────────────────────")
# 同時宣告兩個字串變數
s1, s2 = '123', '12.34'

# 將整數字串 s1 轉成整數型態
print(int(s1), type(int(s1)))         # 輸出: 123 <class 'int'>

# 將浮點數字串 s2 轉成浮點數型態
print(float(s2), type(float(s2)))     # 輸出: 12.34 <class 'float'>

# 將整數字串 s1 轉成浮點數（尾巴會自動補上 .0）
print(float(s1), type(float(s1)))     # 輸出: 123.0 <class 'float'>
print(s1, type(s1))     #  輸出: 123 <class 'str'>


# ── 2. 神奇的 eval 函式基礎應用 ────────────────────────────
print("\n ── 2. 神奇的 eval 函式基礎應用 ────────────────────────────")
# eval() 會自動分析字串內容，是整數就轉 int，是小數就轉 float
print(eval(s1), type(eval(s1)), eval(s2), type(eval(s2)))
# 輸出: 123 <class 'int'> 12.34 <class 'float'>


# ── 3. eval 執行字串內的數學運算式 ──────────────────────────
print("\n ── 3. eval 執行字串內的數學運算式 ──────────────────────────")
# 💡 機制：eval('s1+s2') 會把字串當作程式碼跑，等同於執行 s1 + s2 兩個字串拼接
# 拼接結果為 '12312.34'，再被外層的 eval() 分析成浮點數，因此型態是 float（原講義寫 str 是錯的喔！）
print(eval('s1+s2'), type(eval('s1+s2')))  # 輸出: 12312.34 <class 'float'>

# eval 直接執行字串內的 print() 指令
eval('print(s1+s2)')                  # 輸出: 12312.34

# eval 直接執行內含數學加法的 print() 指令
eval('print(2+3)')                    # 輸出: 5
