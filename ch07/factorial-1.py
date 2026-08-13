#使用階乘函式計算n!=1*2*3*(n-l)*n的結果,其中由使用者輸入。n的輸入值必須大於等於1。

def factorial(n):
    """
    使用迴圈計算 n! (非遞迴寫法)
    n! = 1 * 2 * 3 * ... * (n-1) * n
    """
    # 初始化乘積變數，因為是連乘，所以初始值必須設定為 1 (設為 0 會導致結果全為 0)
    result = 1
    # 使用 for 迴圈產生 1 到 n 的整數序列 
    # range(1, n + 1) 的範圍包含 1，但不包含 (n + 1)，所以正好是 1 ~ n
    for i in range(1, n + 1):
        # 相當於 result = result * i，將每個數字陸續累乘進去
        result *= i
    # 傳回最終計算完成的階乘數值    
    return result
# 使用 while True 建立無限迴圈，直到使用者輸入合格的數字為止
def main():
    # 使用 while 迴圈確保使用者輸入符合規則 (正整數 >= 1)
    while True:
        try:
            # 取得使用者輸入的字串，並嘗試轉為整數 (int)
            user_input = int(input("請輸入一個大於等於 1 的整數 n: "))
            # 檢查輸入的數值是否符合規定 (大於等於 1)
            if user_input >= 1:
                # 輸入數值合格，跳出 while 迴圈
                break
            else:
                # 數值小於 1，提示錯誤並繼續執行迴圈重新要求輸入
                print("【錯誤】輸入值必須大於等於 1，請重新輸入！\n")
               
        except ValueError:
            # 如果使用者輸入非數字（例如字母、小數或空白），int() 會引發 ValueError 錯誤 
            # 透過 except 攔截錯誤，避免程式崩潰
            print("【錯誤】輸入內容非有效整數，請重新輸入！\n")
 
    # 將驗證合格的 user_input 傳入 factorial 函式中計算，並用 ans 接收回傳值
    ans = factorial(user_input)
 
    # 使用 f-string 格式化字串，印出最終計算結果
    print(f"\n計算結果:{user_input}! = {ans}")
# 這是 Python 的最佳實踐（Best Practice）。確保當這個 `.py` 檔被其他程式當作模組（Module）匯入時，不會自動執行 `main()` 的互動輸入流程。
if __name__ == "__main__":
   main()
   
'''Python 內建一個隱形的秘密變數叫做 __name__ [INDEX]。
1.當你直接點右上角三角形（或在終端機 python app.py）執行它時：Python 會自動把這個檔案的 __name__ 設定為 "__main__" [INDEX]。此時 if 條件成立，底下的 main() 就會被乖乖執行 [INDEX]。
2.當這個檔案被別的檔案 import app 時：Python 會把這個檔案的 __name__ 設定為它原本的檔名（例如 "app"） [INDEX]。此時 if 條件不成立，底下的 main() 就會被完全跳過，非常安全 [INDEX]！'''
